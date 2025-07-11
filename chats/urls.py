from django.urls import path
from . import views

app_name = 'Chats'

urlpatterns = [
    path('all/', views.all, name="all"),
]
