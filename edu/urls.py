from django.conf.urls import url
from . import views

app_name = 'edu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^contactUs/$', views.contactUs, name='contactUs'),
    url(r'^logout/$', views.logout_view, name='logout'),
]