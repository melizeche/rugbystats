from django.shortcuts import render
from django.http import HttpResponse
from apps.scoreboard.models import Match, Championship, Team, Round

# Create your views here.

def scoreboard():

    return HttpResponse('HOLA')
