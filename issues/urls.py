from django.urls import re_path 
from . import views

app_name = 'Issues'

urlpatterns = [
    re_path(r"^$", views.IssueList.as_view(), name="all"),
    re_path(r"new/$", views.CreateIssue.as_view(), name="create"),
    re_path(r"by/(?P<pk>\d+)/$", views.IssueDetail, name="single"),
    re_path(r"delete/(?P<pk>\d+)/$", views.DeleteIssue.as_view(), name="delete"),
    re_path(r"join/(?P<pk>\d+)/$", views.JoinIssue.as_view(), name="join"),
    re_path(r"leave/(?P<pk>\d+)/$", views.LeaveIssue.as_view(), name="leave"),   
    re_path(r"solve/(?P<pk>\d+)/$", views.SolveIssue, name="solve"),
    re_path(r"update/(?P<pk>\d+)/$", views.UpdateIssue, name="update"),  
    re_path(r'add_like/(?P<pk>\d+)/$', views.add_like, name='add_like'),
    re_path(r"accept/(?P<pk>\d+)/$", views.accept_answer, name="accept"),
    
    re_path(r"issues_list_api/$", views.issues_list_api, name="issues_list_api"),
    re_path(r"issue_detail_api/(?P<pk>\d+)/$", views.issue_detail_api, name="issue_detail_api"),
    re_path(r"answers_list_api/$", views.answers_list_api, name="answers_list_api"),
]
