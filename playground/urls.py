from django.urls import path
from . import views


#url conf module
urlpatterns = [
    path('', views.index, name = 'list'),
    path('updateTask/<str:primaryKey>/', views.updateTask, name = 'update_task'),
    path('deleteTask/<str:primaryKey>/', views.deleteTask, name = 'delete_task')
]