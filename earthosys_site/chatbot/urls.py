from django.conf.urls import url
from . import views

app_name = 'bot'

urlpatterns = [
    url(r'^', views.BotResponse.as_view(), name='bot')
]
