from django.urls import path

from todo import views

urlpatterns = [

    path('todolist/', views.todo_list),
    path('todolist/<int:pk>/', views.todo_detail),

]
