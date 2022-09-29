# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


from api import views


router = routers.DefaultRouter()
router.register("api/users", views.UserViewSet)
router.register("api/groups", views.GroupViewSet)


app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("api/user/authenticate", views.Login.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
