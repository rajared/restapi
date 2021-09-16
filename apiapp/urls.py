from django.contrib import admin
from django.urls import path
from .views import *
from apiapp import views

urlpatterns =[
    path('',home),
    path('get1/',get1),
    path('add1/',post1),
    path('update1/<int:id>/',update1),
    path('delete1/<int:id>/',delete1),
    path('list/',views.Music_get_list_or_create_operations_view.as_view()),
    path('single/<int:pk>',views.Music_urd_operations_view.as_view()),

]