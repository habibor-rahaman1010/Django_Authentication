from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todos.as_view(), name = 'home'),
    path('add/todo/', views.AddTodoForm.as_view(), name = 'addtodo'),
    path('update/todo/<int:pk>', views.TodoUpdate.as_view(), name = 'updatetodo'),
    path('delete/todo/<int:pk>', views.DeleteTodo.as_view(), name = 'deletetodo'),
    path('finish/todo/<int:pk>', views.FinishTodo.as_view(), name = 'finish'),
    path('complete/todo/', views.CompleteTask.as_view(), name = 'completetask'),
    path('uncomplete/todo/', views.UnCompleteTask.as_view(), name = 'uncompletetask'),
    path('complete/<int:pk>/', views.CompleteTaskView.as_view(), name='completetask'),
]