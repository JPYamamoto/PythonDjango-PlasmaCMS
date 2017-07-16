from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.NewPost.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditPost.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.RemovePost.as_view(), name='delete'),
    url(r'^view/(?P<pk>\d+)/$', views.show_post, name='view'),
]