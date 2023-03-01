"""
    ToDo task URLs
"""


from django.urls import path

from tasks.views import (
    TodoItemListView,
    TodoItemCreateView,
    TodoItemUpdateView,
    TodoItemDeleteView
)

urlpatterns = [
    path("todo/list", TodoItemListView.as_view(), name="all_todo_list"),
    path("todo/create", TodoItemCreateView.as_view(), name="create_a_new_todo"),
    path("todo/update/<int:pk>", TodoItemUpdateView.as_view(), name="update_todo"),
    path("todo/delete/<int:pk>", TodoItemDeleteView.as_view(), name="delete_todo"),
]
