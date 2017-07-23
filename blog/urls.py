from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article'),
    url(r'^article/edit/(?P<article_id>[0-9]+)$',views.article_edit,name='edit'),
    url(r'^index/edit/action/',views.edit_action,name='edit_action'),
    # url(r'^article/edit_action/$',views.edit_action,name='edit_action'),
]
