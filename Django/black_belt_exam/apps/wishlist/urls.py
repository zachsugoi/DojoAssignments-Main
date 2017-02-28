from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^wish_items/(?P<id>\d+)$', views.wish_items, name='wish_items'),
    url(r'^create$', views.create, name='create'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish, name='add_wish'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^create_product$', views.create_product, name='create_product')
]
