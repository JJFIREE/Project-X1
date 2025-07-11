from django.urls import re_path, path  # ✅ re_path instead of url
from . import views

app_name = 'projects'

urlpatterns = [
    re_path(r"^$", views.ListProjects, name="all"),
    re_path(r"^new/$", views.CreateProject.as_view(), name="create"),
    re_path(r"^issues/in/(?P<pk>\d+)/$", views.SingleProject.as_view(), name="single"),
    re_path(r"join/(?P<pk>\d+)/$", views.JoinProject.as_view(), name="join"),
    re_path(r"leave/(?P<pk>\d+)/$", views.LeaveProject.as_view(), name="leave"),
    re_path(r"delete/(?P<pk>\d+)/$", views.DeleteProject.as_view(), name="delete"),
    re_path(r"tagged/(?P<pk>\d+)/$", views.tagged, name="tagged"),
    re_path(r"complete/(?P<pk>\d+)/$", views.CompleteProject, name="complete"),
    re_path(r"joinper/(?P<pk>\d+)/$", views.CloseOrOpenJoin, name="joinper"),
    
    re_path(r"project_detail_api/(?P<pk>\d+)/$", views.project_detail_api, name="project_detail_api"),
    path('project_github_post/<str:pk>/<str:owner>/<str:repo>/', views.project_github_post, name="project_github_post"),
    re_path(r"projects_list_api/$", views.projects_list_api, name="projects_list_api"),
]
