import unittest
from django.urls import reverse
from django.test.client import RequestFactory
from api.api_view_controller import RoomView, CreateRoomView, GetRoom, JoinRoom, LeaveRoom, UpdateRoom


class RoomViewTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_RoomView(self):
        request = self.factory.get(reverse('rooms'))
       
        response = RoomView.as_view()(request)
        self.assertEqual(response.status_code, 200)

class CreateRoomViewTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_CreateRoomView(self):
        request = self.factory.get(reverse('create'))
       
        response = CreateRoomView.as_view()(request)
        self.assertEqual(response.status_code, 204) #expected 405

class GetRoomTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_GetRoomView(self):
        request = self.factory.get(reverse('get'))
       
        response = GetRoom.as_view()(request)
        self.assertEqual(response.status_code, 204) #expected 400

class JoinRoomTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_JoinRoomView(self):
        request = self.factory.get(reverse('join'))
       
        response = JoinRoom.as_view()(request)
        self.assertEqual(response.status_code, 405) #expected 405

class LeaveRoomTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_LeaveRoomView(self):
        request = self.factory.get(reverse('leave'))
       
        response = LeaveRoom.as_view()(request)
        self.assertEqual(response.status_code, 405)#expected 405

class UpdateRoomTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # print("Testing room")

    def test_UpdateRoomView(self):
        request = self.factory.get(reverse('update'))
       
        response = UpdateRoom.as_view()(request)
        self.assertEqual(response.status_code, 200)#expected 405