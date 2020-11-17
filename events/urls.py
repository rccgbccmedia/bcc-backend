from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('events/all/', views.EventView.as_view({'get': 'list'}), name='all-events'),
    path('events/create/', views.EventView.as_view({'post': 'create'}), name='create-event'),
    path('events/<int:pk>/',views.EventView.as_view({'get': 'retrieve'}), name='get-event'),
    path('events/delete/<int:pk>/',views.EventView.as_view({'get': 'destroy'}), name='delete-event'),
    path('events/update/<int:pk>/',views.EventView.as_view({'put': 'update'}), name='update-event'),
    path('events/<int:pk>/rsvp/',views.RsvpView.as_view({'post': 'create'}), name='attend-event'),
    path('rsvp/',views.RsvpView.as_view({'get': 'list'}), name='my-events')
   
]