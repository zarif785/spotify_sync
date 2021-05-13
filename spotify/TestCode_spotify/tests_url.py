from django.test import SimpleTestCase
from django.urls import resolve,reverse
from spotify.spotify_view_controller import *

class TestUrls(SimpleTestCase):

    def testAuthURL_Url(self):
        url =reverse("auth")
        self.assertEqual(resolve(url).func.view_class,AuthURL)  

    def test_spotify_callback_Url(self):
        url =reverse("redirect")
        self.assertEqual(resolve(url).func,spotify_callback) 

    def testIsAuthenticated_Url(self):
        url =reverse("isauth")
        self.assertEqual(resolve(url).func.view_class,IsAuthenticated)  
    
    
    def testCurrentSong_Url(self):
        url =reverse("current")
        self.assertEqual(resolve(url).func.view_class,CurrentSong)  

    def testCurrentSong_Url(self):
        url =reverse("current")
        self.assertEqual(resolve(url).func.view_class,CurrentSong) 

    def testPauseSong_Url(self):
        url =reverse("pause")
        self.assertEqual(resolve(url).func.view_class,PauseSong) 

    def testPlaySong_Url(self):
        url =reverse("play")
        self.assertEqual(resolve(url).func.view_class,PlaySong) 

    def testSkipSong_Url(self):
        url =reverse("skip")
        self.assertEqual(resolve(url).func.view_class,SkipSong) 
