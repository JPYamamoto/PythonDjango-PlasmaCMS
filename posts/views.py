from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
import json

# Create your views here.


def index(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-last_update_datetime')[:12]
        slider_posts = posts[:5]
        posts = [posts[x:x+3] for x in range(0, len(posts), 3)]
        return render(request, 'posts/index.html', {'posts': posts, 'slider': slider_posts})
    else:
        posts_list = Post.objects.all().order_by('-last_update_datetime')
        posts_list = [posts_list[x:x + 3] for x in range(0, len(posts_list), 3)]
        page = request.POST.get('page', 1)

        paginator = Paginator(posts_list, 4)

        try:
            posts_list = paginator.page(page)
        except PageNotAnInteger:
            posts_list = paginator.page(1)
            page = 1
        except EmptyPage:
            posts_list = []

        html = render_to_string('posts/index_page.html', {'posts_list': posts_list, 'MEDIA_URL': settings.MEDIA_URL})
        more_pages = True
        try:
            paginator.page(int(page)+1)
        except EmptyPage:
            more_pages = False

        response = {'html': html, 'more_pages': more_pages}
        return HttpResponse(json.dumps(response), content_type="application/json")


class NewPost(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('settings:login')
    model = Post
    form_class = PostForm
    template_name = 'posts/form.html'
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.last_update_datetime = timezone.now()
        return super(NewPost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('settings:login')
    model = Post
    form_class = PostForm
    template_name = 'posts/form.html'

    def form_valid(self, form):
        form.instance.last_update_datetime = timezone.now()
        return super(EditPost, self).form_valid(form)

    def get_success_url(self, **kwargs):
            return reverse_lazy('posts:view', args=(self.object.id,))


class RemovePost(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('settings:login')
    model = Post
    template_name = 'posts/delete_form.html'
    success_url = reverse_lazy('posts:index')


def show_post(request, pk):
    if request.method == 'POST':
        form_comment = CommentForm(request.POST)

        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.user = request.user
            comment.save()

            success = True
            response = {'comment_id': comment.id,
                        'user_id': str(reverse_lazy('profiles:view', kwargs={'pk': comment.user.pk})),
                        'user_name': comment.user.username,
                        'user_image': comment.user.profile.image.url,
                        'date': comment.creation_datetime.strftime("%B %d, %Y"),
                        'title': comment.title,
                        'content': comment.content
                        }
        else:
            success = False
            response = form_comment.errors

        context = {'success': success, 'response': response}
        return HttpResponse(json.dumps(context), content_type='application/json')
    else:
        post = get_object_or_404(Post, pk=pk)
        if post.allow_comments:
            form_comment = CommentForm()
        else:
            form_comment = None
        context = {'post': post,
                   'form_comment': form_comment,
                   'comments': Comment.objects.filter(post=pk).order_by('-creation_datetime')
                   }
        return render(request, 'posts/view.html', context)


class RemoveComment(DeleteView):
    model = Comment
    template_name = 'posts/delete_form.html'
    success_url = reverse_lazy('posts:index')
