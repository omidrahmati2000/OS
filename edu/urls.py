from django.conf.urls import url

from . import views

app_name = 'edu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^contactUs/$', views.contactUs, name='contactUs'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^course/$', views.course, name='course'),
    url(r'^courses/$', views.showCourses, name='showCourse'),
    url(r'^setting/$', views.setting, name='setting'),
    url(r'^panel/$', views.profile, name='panel'),
]

