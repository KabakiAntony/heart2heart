from django.urls import path

from . import views

app_name = "messageHandler"

urlpatterns = [
    path('', views.home, name="home"),
    path('email-message/', views.email_message, name="email_message"),
    path('voice-message/', views.voice_message, name="voice_message"),

]
