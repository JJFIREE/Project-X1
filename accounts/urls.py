from django.contrib import admin
from django.urls import re_path  # ✅ use re_path instead of url
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r"^register/$", views.register, name='register'),
    re_path(r"^login/$", views.loginUser, name='login'),
    re_path(r"^logout/$", views.logoutUser, name='logout'),
    re_path(r"^profile/(?P<pk>\d+)/$", views.profile_page, name='profile'),
    re_path(r"^deluser/$", views.delete_user, name="deluser"),
    re_path(r"^profile_api/(?P<pk>\d+)/$", views.profile_api, name='profile_api'),
]
