from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('images/all/', views.ImageView.as_view({'get': 'list'}), name='all-images'),
    path('images/add/', views.ImageView.as_view({'post': 'create'}), name='add-image'),
    path('images/<int:pk>/',views.ImageView.as_view({'get': 'retrieve'}), name='get-video'),
    path('images/delete/<int:pk>/',views.ImageView.as_view({'get': 'destroy'}), name='delete-video'),


    path('video/all/', views.ImageView.as_view({'get': 'list'}), name='all-video'),
    path('video/add/', views.ImageView.as_view({'post': 'create'}), name='add-image'),
    path('video/<int:pk>/',views.ImageView.as_view({'get': 'retrieve'}), name='get-video'),
    path('video/delete/<int:pk>/',views.ImageView.as_view({'get': 'destroy'}), name='delete-video'),
]
