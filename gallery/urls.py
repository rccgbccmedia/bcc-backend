from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('images/all/', views.ImageView.as_view({'get': 'list'}), name='all-images'),
    path('images/add/', views.ImageView.as_view({'post': 'create'}), name='add-image'),
    path('images/<int:pk>/',views.ImageView.as_view({'get': 'retrieve'}), name='get-image'),
    path('images/delete/<int:pk>/',views.ImageView.as_view({'get': 'destroy'}), name='delete-image'),


    path('videos/all/', views.VideoView.as_view({'get': 'list'}), name='all-video'),
    path('videos/add/', views.VideoView.as_view({'post': 'create'}), name='add-image'),
    path('videos/<int:pk>/',views.VideoView.as_view({'get': 'retrieve'}), name='get-video'),
    path('videos/delete/<int:pk>/',views.VideoView.as_view({'get': 'destroy'}), name='delete-video'),
]
