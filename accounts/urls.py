from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('auth/', include('djoser.urls.jwt')),
]