from django.views import generic
from .models import BlogPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return BlogPost.objects.all()


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

"""
class LoginView(View):

    def post(self, request):
        username= request.POST('username')
        password = request.POST('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'blog/index.html')
            else:
                return render(request, 'blog/login.html', {'error_message': 'Account disabled'})
        else:
            return render(request, 'blog/login.html', {'error_message': 'Invalid login'})
        return render(request, 'blog/login.html')
"""


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


class LandingPageView(View):
    template_name = 'blog/index.html'

