from django.urls import path
from . import views
app_name = 'task'
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/edit/', views.edit_task, name='edit_task'),
    path('tasks/edit/<int:id>/',views.edit_task, name='edit_task'),
     path('tasks/delete/',views.delete_task, name='delete_task'),
]
