from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^delete$', views.delete),
    url(r'^users_courses$', views.users_courses, name='users_courses'),
    url(r'^add_user$', views.add_user, name='add_user')
]
