
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, signup, login_view, logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html',
             success_url = 'home'), name='change-password'),
    path('change_password/home', home, name='home'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
             template_name='registration/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
