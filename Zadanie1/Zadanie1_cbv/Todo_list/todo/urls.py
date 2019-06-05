from django.urls import path

from todo import views

urlpatterns = [

    path('todolist/', views.TodoListView.as_view(), name = views.TodoListView.name),
    path('todolist/<int:pk>/', views.TodoDetailView.as_view(), name = views.TodoDetailView.name),
    path('', views.ApiRoot.as_view(), name = views.ApiRoot.name)

]
