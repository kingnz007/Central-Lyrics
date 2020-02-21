from django.test import TestCase, Client
from django.urls import reverse
import lyricsgenius

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.search = reverse('search')
        self.lyrics = reverse('lyrics', kwargs={
            'artist': 'artistname',
            'song': 'songname',
        })
        self.genius = lyricsgenius.Genius("4FMfq4F26i2Xz8JSEAsTInmjHBvGRK9Vz9NBT58L0ztn3bC7mPi8vg7MODxax_Pj")
        self.genius.skip_non_songs = True
        

    def test_homepage_GET(self):
        response = self.client.get(self.index)
        self.assertTrue(self.genius.skip_non_songs)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/index.html')

    def test_search_GET(self):
        response = self.client.get(self.search)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/search.html')


    def test_lyrics_GET(self):
        response = self.client.get(self.lyrics)

        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'central/lyrics.html')        
