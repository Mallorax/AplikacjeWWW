from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_view, name='index'),
    # views for tasks
    path('task-list/', views.tasks_list, name="tasks_list"),
    path('task-details/<str:pk>/', views.task_detail, name="tasks_details"),
    path('task-create/', views.task_create, name="tasks_create"),
    path('task-update/<str:pk>/', views.task_update, name="tasks_update"),
    path('task-delete/<str:pk>/', views.task_delete, name="tasks_delete"),
]
