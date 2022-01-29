from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import JsonResponse
from playlist.models import Playlist, Track

def main(request):
    like = 0
    like = like + 1
    context = {
        "land_type":"about",
        "name": "arsen",
    }
    return render(request, "main.html", context)
    
def about(request):
    context = {
    }
    return render(request, "playlist.html", context)

def sign_in(request):
    context = {
    }
    return render(request, "sign_in.html", context)

def upload_track_page(request):
    context = {
    }
    return render(request, "create_track.html", context)
    
def reg_user(request):
    name = request.GET.get("mail")
    Playlist.objects.create(name=name)
    data = {
    }
    return JsonResponse(data)

def upload_track(request):
    song_name = request.POST.get("song_name")
    artist = request.POST.get("artist")
    link = request.POST.get("link")
    track = Track.objects.create(
        name=song_name,
        artist=artist,
        )
    if request.FILES.get('file'):
        file = request.FILES.get('file')
        track.file = file
        track.save()
    data = {
        "ok":"VSE POLUCHILOSЬ"
    }
    return JsonResponse(data)


def getplaylist(request):
    tracks = Track.objects.all()
    data_music = []
    for i in range(0, len(tracks)):
        track = tracks[i]
        if track.file:
            file_url = track.file.url
        else:
            file_url = ""
        data_music.append([track.artist, track.name, file_url])
    data = {
        "data_music":data_music,
    }
    return JsonResponse(data)


