from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('user/',views.UserDetailsView.as_view(), name='user-details'),
    path('login/', views.UserLoginView.as_view(), name= 'user-register',)
    # path('auth/', include('djoser.urls.jwt')),
]