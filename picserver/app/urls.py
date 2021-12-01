from django.urls import path
from .views import activate,sendEmail,appi,api,imageApi,register, Home,login,requestDataJson,chatView,responseDataJson,imageApi,imageView,imageResponse,userProfile, chatGen,dashBoard, addImage

urlpatterns = [
    path('email/', sendEmail),
    path('email/app/', appi),
    path('api', api),
    path('api/file/', imageApi),

    path('',Home),
    path('imageView/<int:id>', imageView),

    path('profile/<str:username>', userProfile),

    path('login/', login),
    path('register/', register),
    path('activate/', activate),

    path('chatApi/<int:id>', requestDataJson),
    path('chat/<int:id>', chatView),
    path('chatResponse/<int:id>',responseDataJson),
    path('chatgen/<str:username>', chatGen),

    path('imageApi', imageApi),
    path('imageResponse/<int:id>', imageResponse),

    path('dashboard/',dashBoard),
    path('upload/', addImage),
]