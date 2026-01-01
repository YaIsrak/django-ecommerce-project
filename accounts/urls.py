from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup, name='sign_up'),
    path('sign-in/', views.signin, name='sign_in'),
    path('sign-out/', views.signout, name='sign_out'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('forgot-password/', views.forgot_password, name='forgot_password'),
]
