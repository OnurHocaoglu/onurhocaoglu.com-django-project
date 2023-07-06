from django.urls import path

from account.views import user_login, user_logout, user_register

app_name = 'account'

urlpatterns = [
    path("login", user_login, name="user_login"),
    path("register", user_register, name="user_register"),
    path("logout", user_logout, name="user_logout")
]