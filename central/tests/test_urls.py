from django.test import SimpleTestCase
from django.urls import resolve, reverse
from central.views import index, search, lyrics

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_lyrics_url_resolves(self):
        url = reverse('lyrics', kwargs={
            'artist': 'artistname',
            'song': 'songname',
        })
        
        self.assertEquals(resolve(url).func, lyrics)

