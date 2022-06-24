from django.contrib import admin
from django.urls import path
from .import views




urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('info_form',views.info_form,name="info_form"),
    path('show_data',views.show_data.as_view(),name="show_data"),
    path('<int:pk>/delete',views.delete.as_view(),name="delete"),
    path('upload',views.upload,name="upload"),
    path('signin/',views.signinn,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('upload_form/',views.upload_form,name="upload_form"),
  
]