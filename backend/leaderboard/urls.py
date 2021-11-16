﻿from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'leaderboard'

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
