from django.shortcuts import render
from.models import *

def home(sorov):
    return render(sorov,'index.html')


def about(sorov):
    return render(sorov,'about.html')

def hamma_clublar(sorov):
    content = {
        "clubs": Club.objects.all()
    }
    return render(sorov,'clubs.html',content)


# Vazifa

# 1-topshiriq   Biron clubga kirilganida shu clubga tegishli futbolchilarni ko'rsating. (country-clubs.html)

def oyinchilar(sorov):
    content = {
        "players": Player.objects.all()
    }
    return render(sorov,'country-clubs.html',content)

def club_oyinchi(sorov,son):
    content = {
        "players": Player.objects.filter(club__id = son)
    }
    return render(sorov,'country-clubs.html',content)
