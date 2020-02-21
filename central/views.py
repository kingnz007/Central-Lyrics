from django.shortcuts import render
import lyricsgenius
from pprint import pprint

genius = lyricsgenius.Genius("4FMfq4F26i2Xz8JSEAsTInmjHBvGRK9Vz9NBT58L0ztn3bC7mPi8vg7MODxax_Pj")
genius.skip_non_songs = True



def index(request):
    return render(request, 'central/index.html')

def search(request):
    global genius
    if 'q' in request.GET:
        query = request.GET['q']

        
        titles, artists, images = ([] for _ in range(3))
        songs = genius.search_genius(query)


        
        for song in songs['hits']:
            titles.append(song['result']['title'])
            artists.append(song['result']['primary_artist']['name'])
            images.append(song['result']['primary_artist']['image_url'])

        musics = [{'image': t[0], 'title': t[1], 'artist':t[2]} for t in zip(images, titles, artists)]
        
        
        
            
    context = {
        'musics': musics,
        'values': request.GET
    }

    return render(request, 'central/search.html', context)

def lyrics(request, song='', artist=''):   
    global genius
    lyrics = genius.search_song(song, artist=artist)

    context = {
        'lyrics': lyrics
    }

    return render(request, 'central/lyrics.html', context)

