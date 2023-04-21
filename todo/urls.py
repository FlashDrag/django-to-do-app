from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_list, name='get_todo_list'),
    path('add/', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit')
]
