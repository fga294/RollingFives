from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Team

# Create your views here.


def brasileirao(request):
    teams = Team.objects.all()
    return render(request, 'brasileirao/index.html', {'teams': teams})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'brasileirao/team_detail.html', {'team': team})
