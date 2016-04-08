from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.login, name = "login"),
    url(r'^home/$', views.home, name = "home"),
    url(r'^seeker/$', views.seeker, name = "seeker"),
    url(r'^helper/$', views.helper, name = "helper"),
    url(r'^logout/$', views.logout, name = "logout"),
    url(r'^register/$', views.PersonRegistration, name="register"),
]	