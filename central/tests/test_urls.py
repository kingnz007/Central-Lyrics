'''
Test urls
'''
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from central.views import index, search, lyrics

class TestUrls(SimpleTestCase):
    '''
    Inherits from SimpleTestCase
    and test all index, search and lyrics url
    '''
    def test_index_url_resolves(self):
        '''
        test home page url
        '''
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_search_url_resolves(self):
        '''
        test search url
        '''
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_lyrics_url_resolves(self):
        '''
        test lyrics pattern and url
        '''
        url = reverse('lyrics', kwargs={
            'artist': 'artistname',
            'song': 'songname',
        })
        self.assertEquals(resolve(url).func, lyrics)      
