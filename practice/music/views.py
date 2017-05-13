from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song
from django.http import Http404
# Create your views here.

def index(request):
	all_albums = Album.objects.all()
	return render(request,'music/index.html',{'all_albums':all_albums})

def detail(request,album_id):
	try:
		album=Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
	try:
		selected_song=Album.song_set.get(pk=request.POST['song'])
	except (KeyError,Song.DoesNotExist):
		return render(request,'music/detail.html',{
			'album':album,
			'error_message':"song not found"
			})
	else:
		selected_song.is_favorite= True
		selected_song.save()
		return render(request,'music/detail.html',{'album':album})