from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/(?P<pk>\d+)/$', views.ShowUser.as_view(), name='view'),
    url(r'^view/$', views.ShowUser.as_view(), name='view_self'),
    url(r'^edit/$', views.UserProfileEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.RemoveUser.as_view(), name='delete'),
]