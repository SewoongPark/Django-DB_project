from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail", views.board_detail, name="detail"),
    path("<str:champion_id>", views.board_detail, name="detail"),
]
