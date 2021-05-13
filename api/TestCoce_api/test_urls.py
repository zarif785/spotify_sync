from django.test import SimpleTestCase
from django.urls import resolve,reverse
from api.api_view_controller import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom

class URLS_Test(SimpleTestCase):

    def testRoom_Urls(self):
        url =reverse("rooms")
        self.assertEqual(resolve(url).func.view_class,RoomView)  


    def testCreateRoom_Urls(self):
        url =reverse("create")
        self.assertEqual(resolve(url).func.view_class,CreateRoomView)

    def testGetRoom_Urls(self):
        url =reverse("get")
        self.assertEqual(resolve(url).func.view_class,GetRoom)
        
    def testJoinRoom_Urls(self):
        url =reverse("join")
        self.assertEqual(resolve(url).func.view_class,JoinRoom)


    def testUserInRoom_Urls(self):
        url =reverse("user")
        self.assertEqual(resolve(url).func.view_class,UserInRoom)

    def testLeaveRoom_Urls(self):
        url =reverse("leave")
        self.assertEqual(resolve(url).func.view_class,LeaveRoom)

    def testUpdateRoom_Urls(self):
        url =reverse("update")
        self.assertEqual(resolve(url).func.view_class,UpdateRoom)