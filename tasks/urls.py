from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_view, name='index'),
    # views for tasks
    path('task-list/', views.TasksListView.as_view(), name="tasks_list"),
    path('task-details/<str:pk>/', views.task_detail, name="tasks_details"),
    path('task-create/', views.task_create, name="tasks_create"),
    path('task-update/<str:pk>/', views.task_update, name="tasks_update"),
    path('task-delete/<str:pk>/', views.task_delete, name="tasks_delete"),
    # views for people
    path('person-list/', views.PeopleListView.as_view(), name="person_list"),
    path('person-details/<str:pk>/', views.person_detail, name="person_details"),
    path('person-create/', views.person_create, name="person_create"),
    path('person-update/<str:pk>/', views.person_update, name="person_update"),
    path('person-delete/<str:pk>/', views.person_delete, name="person_delete"),
]
