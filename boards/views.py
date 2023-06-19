from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import (
    User,
    Champions,
    Review,
    champion_skill_img_text,
    champion_tip,
    Champion_counter,
    Champion_rate,
    champion_skill_name,
    Champion_story,
)
from django.contrib.auth.models import User
from .forms import ReviewForm, CommentForm

from django.core.paginator import Paginator
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict


def index(request):
    board_list = champion_tip.objects.all()
    return render(request, "boards/index.html", {"board_list": board_list})


def board_detail(request, champion_id):
    ChampionBoard = (
        Champions.objects.filter()
        .prefetch_related("review_set")
        .get(champion=champion_id)
    )
    ChampionTipBoard = champion_tip.objects.filter().get(champion=champion_id)
    ChampionSkillImgBoard = champion_skill_img_text.objects.filter().get(
        champion=champion_id
    )
    ChampionCounterBoard = Champion_counter.objects.filter(
        champion_id=champion_id
    ).all()

    counter_data = ChampionCounterBoard.values()
    # print(counter_data)
    counter_tips = champion_tip.objects.filter(
        champion_id__in=[counter.get("counter_name") for counter in counter_data]
    ).all()
    counter_tips = counter_tips.values()
    counter_tips = {ct["champion_id"]: ct["image_url"] for ct in counter_tips}
    print(counter_tips)
    for counter in counter_data:
        cid = counter["counter_name"]
        try:
            counter["image_url"] = counter_tips[cid]
        except KeyError as e:
            counter[
                "image_url"
            ] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGF64l_02CqKyoe9AbHArznivy5B7xLpYzArNj6cQ&s"

    ChampionRateBoard = Champion_rate.objects.filter().get(champion=champion_id)
    ChampionSkillNameBoard = champion_skill_name.objects.filter().get(
        champion=champion_id
    )
    ChampionStoryBoard = Champion_story.objects.filter().get(champion=champion_id)

    form = CommentForm()
    comments = ChampionBoard.review_set.all()
    paginator = Paginator(comments, 10)
    page = request.GET.get("page")

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review(content=data["review"], ChampionBoard=ChampionBoard)
            review.save()
            return redirect(
                reverse("ChampionBoard:detail", kwargs={"champion_id": champion_id})
            )
    ChampionCounterBoard = counter_data
    return render(
        request,
        "boards/detail.html",
        {
            "ChampionBoard": ChampionBoard,
            "ChampionTipBoard": ChampionTipBoard,
            "ChampionSkillImgBoard": ChampionSkillImgBoard,
            "ChampionCounterBoard": ChampionCounterBoard,
            "ChampionRateBoard": ChampionRateBoard,
            "ChampionSkillNameBoard": ChampionSkillNameBoard,
            "ChampionStoryBoard": ChampionStoryBoard,
            "form": form,
            "comments": comments,
            "page": page,  # 추가된 부분: 현재 페이지 번호를 템플릿에 전달
        },
    )


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        if len(searched) == 0:
            return redirect("http://127.0.0.1:8000/boards/")
        else:
            return redirect("/boards/{}".format(searched))
