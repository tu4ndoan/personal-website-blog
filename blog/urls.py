from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^post/add/$', views.PostCreate.as_view(), name='post-add'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
    url(r'^post/(?P<pk>[0-9]+)/update/$', views.PostUpdate.as_view(), name='post-update'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

]