from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, CodeView, UserPasswordChange

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('code/', CodeView.as_view(), name='code'),

    path('password_change/', UserPasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy("users:password_reset_done")), name='password_reset_form'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html",
                                          success_url=reverse_lazy("users:password_reset_complete"),
                                          ), name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
]
