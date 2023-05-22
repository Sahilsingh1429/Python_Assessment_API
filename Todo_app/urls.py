from django.urls import path
from .views import *
urlpatterns = [
   path('create_todos/',CreateToDo.as_view(),name='create_todos'),
   path('get_todos/<int:tid>',GetToDo.as_view(),name='get_todos'),
   path('update_todos/<int:tid>',UpdateToDo.as_view(),name='update_todos'),
   path('delete_todos/<int:tid>',DeleteToDo.as_view(),name='delete_todos'),
   path('all_todos/',AllToDo.as_view(),name='all_todos')
]