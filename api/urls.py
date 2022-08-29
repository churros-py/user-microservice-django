from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
	path('login/', views.Login.as_view(), name='login'),
	path('user/', views.user, name='user'),
]
