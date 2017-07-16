from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Category
from .forms import CategoryForm
from posts.models import Post

# Create your views here.


def index(request):
    def posts_of(cat):
        return Post.objects.filter(category=cat).order_by('-creation_datetime')[:3]

    categories_posts = {category: posts_of(category) for category in Category.objects.all()}
    return render(request, 'categories/index.html', {'object': categories_posts})


class NewCategory(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('settings:login')
    model = Category
    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories:index')


class EditCategory(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('settings:login')
    model = Category
    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories:index')


class RemoveCategory(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('settings:login')
    model = Category
    template_name = 'categories/delete_form.html'
    success_url = reverse_lazy('categories:index')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error_posts = Post.objects.filter(category=self.object.id)
            return render(request, self.template_name, {'message': 'You can\'t delete this category, because it is referenced by the following posts.',
                                                        'error_posts': error_posts})


def show_category(request, pk):
    category_info = Category.objects.get(pk=pk)
    posts_list = Post.objects.filter(category=pk).order_by('-last_update_datetime')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'categories/view.html', {'object': category_info, 'posts': posts})
