from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db import transaction
from django.db.models import Count, Q
from django.contrib.auth.models import User
from django.views.generic import View, ListView, CreateView
from .forms import BlogSettingsForm, LoginForm, RegisterForm
from .models import Blog
from posts.models import Post
from categories.models import Category
from profiles.models import Profile

# Create your views here.


@login_required(login_url=reverse_lazy('settings:login'))
def blog_settings(request):
    current_config = Blog.objects.last()
    if request.method == 'GET':
        form = BlogSettingsForm(instance=current_config)
    else:
        form = BlogSettingsForm(request.POST, request.FILES,
                                instance=current_config)
        if form.is_valid():
            form.save()
            return redirect('settings:index')
    return render(request, 'settings/blog_settings.html', {'form': form})


class IndexList(ListView):
    model = Post
    template_name = 'settings/blog_index.html'
    context_object_name = 'index_elements'
    paginate_by = 6
    ordering = ['-creation_datetime']

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(
            times=Count('post__category')).order_by('-times')[:3]
        return context


class Login(View):
    form = LoginForm()
    message = None
    template = 'settings/blog_login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_next_url())
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login(request, user)
            return redirect(self.get_next_url())
        else:
            self.message = 'Wrong username or password.'
            return render(request, self.template, self.get_context())

    def get_context(self):
        return {'form': self.form, 'message': self.message}

    def get_next_url(self):
        return self.request.GET.get('next', 'settings:index')


class Register(CreateView):
    success_url = reverse_lazy('settings:login')
    model = User
    template_name = 'settings/blog_register.html'
    form_class = RegisterForm

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password1'])
        self.object.save()
        profile = Profile(user=self.object)
        profile.save()
        return HttpResponseRedirect(self.get_success_url())


def logout(request):
    logout_django(request)
    return redirect('settings:index')


def search(request):
    if request.method == 'GET':
        string = request.GET.get('search_string')
        posts = Post.objects.filter(title__icontains=string)[:20]
        categories = Category.objects.filter(Q(name__icontains=string) | Q(description__icontains=string))[:20]
        users = User.objects.filter(Q(username__icontains=string) | Q(profile__name__icontains=string))[:20]

        context = {'posts_list': posts,
                   'categories_list': categories,
                   'users_list': users}

        return render(request, 'settings/blog_search.html', context)
