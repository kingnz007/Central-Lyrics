'''
Views.py. Handles the views for home page, search page and lyrics.
Add your genius api key in ACCESS_TOKEN
'''
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import lyricsgenius
from pprint import pprint

# Enter your CLIENT ACCESS TOKEN
ACCESS_TOKEN = "YOUR CLIENT ACCESS TOKEN HERE"

genius = lyricsgenius.Genius(ACCESS_TOKEN)
genius.skip_non_songs = True

def index(request):
    '''
    render home page
    '''
    return render(request, 'central/index.html')

def search(request):
    '''
    search page
    use search_genius() fo retrieve search query and render title, artists and images
    '''
    global genius
    musics = []
    if request.method == 'GET':
        if 'q' in request.GET:
            query = request.GET['q']
            
            titles, artists, images = ([] for _ in range(3))
            try:
                songs = genius.search_genius(query)
            except:
                print("There's something wrong with your api key. Please try again.")
            
            if songs is not None: 
                for song in songs['hits']:
                    #append the data to the list
                    titles.append(song['result']['title'])
                    artists.append(song['result']['primary_artist']['name'])
                    images.append(song['result']['primary_artist']['image_url'])

            #zip the dict inside list
            musics = [{'image': t[0], 'title': t[1], 'artist':t[2]} for t in zip(images, titles, artists)]       
            
    context = {
        'musics': musics,
        'values': request.GET
    }
    return render(request, 'central/search.html', context)

#Cache page
@cache_page(60*3)    
def lyrics(request, song='', artist=''):   
    '''
    Retrieve and  display song lyrics
    '''
    global genius

    try:
        lyrics = genius.search_song(song, artist=artist, get_full_info=False)
    except:
        print("Unable to retrieve lyrics at the moment. Please try again.")

    context = {
        'lyrics': lyrics
    }
    return render(request, 'central/lyrics.html', context)
