from django.shortcuts import render
import lyricsgenius
from pprint import pprint




def index(request):
    return render(request, 'central/index.html')

def search(request):
    genius = lyricsgenius.Genius("4FMfq4F26i2Xz8JSEAsTInmjHBvGRK9Vz9NBT58L0ztn3bC7mPi8vg7MODxax_Pj")
    genius.skip_non_songs = True

    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            song = genius.search_genius(query)
            pprint(song['hits'][1])

    context = {
        'query': query
    }

    return render(request, 'central/search.html', context)

def lyrics(request):
    return render(request, 'central/lyrics.html')

