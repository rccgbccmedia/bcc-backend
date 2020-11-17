from django.urls import path, include
from . import views
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                                PasswordResetConfirmView, PasswordResetView,
                                UserDetailsView)


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('user/',views.UserDetailsView.as_view(), name='user-details'),
    path('all-users/', views.ListUsersView.as_view(), name='all-users'),
    path('login/', views.UserLoginView.as_view(), name= 'user-register'),
    path('password/reset/', views.PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(),name='password_reset_confirm')
    # path('auth/', include('djoser.urls.jwt')),
]