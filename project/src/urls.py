from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.login, name = "login"),
    url(r'^home/$', views.home, name = "home"),
    url(r'^logout/$', views.logout, name = "logout"),
]	