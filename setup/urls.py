# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("api.urls", namespace="api")),
    path("admin/", admin.site.urls),
]
