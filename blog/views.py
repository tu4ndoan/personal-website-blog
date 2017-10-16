from django.views import generic
from .models import BlogPost, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from .forms import CommentForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    model = BlogPost
    context_object_name = "blogpost_list"
    template_name = 'blog/index.html'
    paginate_by = 10


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'


class PostCreate(CreateView):
    model = BlogPost
    fields = ['post_title', 'content', 'feature_image', 'hooker']
# when create a blog, we should add an image, tags, and category


class PostUpdate(UpdateView):
    model = BlogPost
    fields = ['post_title', 'content', 'feature_image', 'hooker']


class PostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:index")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'blog/index.html')
            else:
                return render(request, 'blog/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'blog/login.html', {'error_message': 'Invalid login'})
    return render(request, 'blog/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('blog:index')


def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # commit = False means ??
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:index')
