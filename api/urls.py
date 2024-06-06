from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.authentication,name='authentication'),
    path('AddTasks',views.AddTask,name='addtask'),
    path('ViewTasks',views.ViewTasks,name='viewtasks'),
]