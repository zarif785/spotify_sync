import unittest
from django.urls import reverse
from django.test.client import RequestFactory
from spotify.spotify_view_controller import *


class AuthUrlViewTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_AuthUrl(self):
        request = self.factory.get(reverse('auth'))
       
        response = AuthURL.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PauseTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_Pause(self):
        request = self.factory.get(reverse('pause'))
       
        response = PauseSong.as_view()(request)
        self.assertEqual(response.status_code, 405)


class PlayTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_Play(self):
        request = self.factory.get(reverse('play'))
       
        response = PlaySong.as_view()(request)
        self.assertEqual(response.status_code, 402)

class SkipTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_Play(self):
        request = self.factory.get(reverse('skip'))
       
        response = SkipSong.as_view()(request)
        self.assertEqual(response.status_code, 405)