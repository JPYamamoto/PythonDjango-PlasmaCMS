from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^settings/$', views.blog_settings, name='blog_settings'),
    url(r'^$', views.IndexList.as_view(), name='index'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^search/$', views.search, name='search'),
]