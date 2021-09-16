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
    path('list/',views.Musiclistview.as_view()),
    path('create/',views.Musiccreateview.as_view()),
    path('retrieve/<int:pk>/',views.Musicgetview.as_view()),
    path('destroy/<int:pk>/',views.Musicdestroyview.as_view()),
    path('update/<int:pk>/',views.Musicupdateview.as_view()),

]