from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    """ show the home page with the form prompts"""
    return render(request, 'messageHandler/home.html')


def voice_message(request):
    pass


def email_message(request):
    pass
