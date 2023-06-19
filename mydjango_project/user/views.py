from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.utils import timezone


def index(request):
    resp = render(request, "user/profile.html")
    resp.set_cookie("cookie_text", "test_value")
    return resp


def user_profile(request):
    return HttpResponse(
        """
      <h1>나의 프로필</h1>
      <ul>
        <li>이름: 신윤수</li>
        <li>별명: ys</li>
      </ul>
      """
    )


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(
                username=username, password=password
            )  # DB의 USER정보와 비교 및 조회 -> 접속 허가 OR NONE반환
            login(request, user)
            return redirect(reverse("user:index"))
    return render(request, "user/register.html", {"form": form})
