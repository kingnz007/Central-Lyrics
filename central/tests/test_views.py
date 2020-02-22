'''
Test website views
'''
from django.test import TestCase, Client
from django.urls import reverse
import lyricsgenius

class TestViews(TestCase):
    '''
    Inherits from TestCase and tests all the views of central lyrics
    '''
    def setUp(self):
        '''
        Runs in every tests.
        instantiates Client.
        '''
        self.client = Client()
        self.index = reverse('index')
        self.search = reverse('search')
        self.lyrics = reverse('lyrics', kwargs={
            'artist': 'artistname',
            'song': 'songname',
        })

    def test_homepage_GET(self):
        '''
        test for home page response code and template
        '''
        response = self.client.get(self.index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/index.html')

    def test_search_GET(self):
        '''
        test for search page response code and template
        '''
        response = self.client.get(self.search)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/search.html')

    def test_lyrics_GET(self):
        '''
        test for lyrics page response code and template
        '''
        response = self.client.get(self.lyrics)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/lyrics.html')
