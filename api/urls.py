from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
	path('', views.Login.as_view(), name='login')
]
