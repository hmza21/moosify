from os import remove

from moosify.settings import MEDIA_ROOT

from django.http import FileResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Track
from .functions import download, lookup, download_track

def get_history(request: WSGIRequest):
    track_objs = Track.objects.filter(user=request.user).order_by('-timestamp')
    tracks = [(track, lookup(track.spotify_url)) for track in track_objs]
    return tracks


class IndexView(LoginRequiredMixin, View):
    template_name = 'download/index.html'
    
    def get(self, request: WSGIRequest):
        
        tracks = get_history(request)
        
        for track in tracks:
            if track[0].downloaded:
                remove(str(MEDIA_ROOT / track[0].filename))
                track[0].delete()
                tracks.pop(tracks.index(track))
        
        context = {
            'tracks': tracks
        }
        
        return render(request, IndexView.template_name, context)


class DownloadView(LoginRequiredMixin, View):
    
    def get(self, request: WSGIRequest):
        
        url = request.GET.get('url')
        if url:
            track = Track.objects.filter(user=request.user, spotify_url__icontains=url).first()
            
            if not track:
                track_meta = download_track(url)
                track = Track(user=request.user, spotify_url=url, filename = str(track_meta) + '.mp3')
                track.save()
                return redirect('download:index')
            else:
                track.downloaded = True
                track.save()
                return FileResponse(open(str(MEDIA_ROOT / track.filename), 'rb'), as_attachment=True)
        
        else:
            return redirect('download:index')
