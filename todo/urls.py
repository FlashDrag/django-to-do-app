from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_list, name='get_todo_list'),
    path('toggle/<int:item_id>', views.toggle_item, name='toggle'),
    path('delete/<int:item_id>', views.delete_item, name='delete'),
    path('edit/<int:item_id>', views.edit_item, name='edit'),
]
