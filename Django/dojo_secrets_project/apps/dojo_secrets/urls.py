from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.log_reg, name='log_reg'),
    url(r'^secrets$', views.index, name='index'),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^secret$', views.secret, name='secret'),
    url(r'^like$', views.like, name='like'),
    url(r'^delete$', views.delete, name='delete')
]
