import unittest
from django.urls import reverse
from django.test.client import RequestFactory
from spotify.spotify_view_controller import *


class AuthUrlViewTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_get_AuthUrl(self):
        request = self.factory.get(reverse('auth'))
       
        response = AuthURL.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PauseTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_put_Pause(self):
        request = self.factory.get(reverse('pause'))
       
        response = PauseSong.as_view()(request)
        self.assertEqual(response.status_code, 405)


class PlayTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_put_Play(self):
        request = self.factory.get(reverse('play'))
       
        response = PlaySong.as_view()(request)
        self.assertEqual(response.status_code, 402)

class SkipTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_post_Skip(self):
        request = self.factory.get(reverse('skip'))
       
        response = SkipSong.as_view()(request)
        self.assertEqual(response.status_code, 405)