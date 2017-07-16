from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError

from .forms import UserProfileForm, UserForm
from .models import Profile
from posts.models import Post

# Create your views here.


class ShowUser(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('settings:login')
    model = User
    template_name = 'profiles/view.html'

    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)

        if pk is not None:
            queryset = queryset.filter(pk=pk)

        if pk is None:
            pk = self.request.user.pk
            queryset = queryset.filter(pk=pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super(ShowUser, self).get_context_data(**kwargs)
        try:
            posts = Post.objects.filter(author=self.request.user)
        except Post.DoesNotExist:
            posts = None
        context['posts'] = posts
        return context


class UserProfileEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('settings:login')
    model = Profile
    second_model = User
    template_name = 'profiles/form.html'
    form_class = UserProfileForm
    second_form_class = UserForm
    success_url = reverse_lazy('profiles:view_self')

    def get_context_data(self, **kwargs):
        context = super(UserProfileEdit, self).get_context_data(**kwargs)

        profile = self.get_object()
        user_account = self.second_model.objects.get(id=profile.user_id)

        if 'form' not in context:
            context['form'] = self.form_class(instance=profile)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=user_account)
        return context

    def get_object(self, queryset=None):
        current_user, created = Profile.objects.get_or_create(
            user_id=self.request.user.id)
        pk = current_user.pk
        return get_object_or_404(Profile, pk=pk)


class RemoveUser(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('settings:login')
    model = User
    template_name = 'profiles/delete_form.html'
    success_url = reverse_lazy('settings:index')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error_posts = Post.objects.filter(author=self.object.id)
            return render(request, self.template_name, {'message': 'You can\'t delete this user, because it is referenced by the following posts.',
                                                        'error_posts': error_posts})
