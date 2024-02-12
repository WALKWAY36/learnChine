from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('chat/', views.chat, name="chat"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),

    path('activity/', views.activityPage, name="activity"),

    path('dict1/', views.dict1, name="dict1"),
    path('dict2/', views.dict2, name="dict2"),
    path('dict3/', views.dict3, name="dict3"),
    path('dict4/', views.dict4, name="dict4"),

    path('task1/', views.task1, name="task1"),
    path('task2/', views.task2, name="task2"),
    path('task3/', views.task3, name="task3"),
    path('task4/', views.task4, name="task4"),
]



