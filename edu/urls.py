from django.conf.urls import url
from . import views

app_name = 'edu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/request$', views.addUser, name='register_request'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/$', views.loginRequest, name='login_request'),
]