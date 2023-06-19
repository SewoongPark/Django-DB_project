from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),  # as_view = class를 함수 형태로 바꿔준다
    path(
        "login",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),  # as_view = class를 함수 형태로 바꿔준다
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    path("register", views.register, name="register"),
    # path('sample', views.SampleView.as_view())
]
