from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.NewCategory.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditCategory.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.RemoveCategory.as_view(), name='delete'),
    url(r'^view/(?P<pk>\d+)/$', views.show_category, name='view'),
]