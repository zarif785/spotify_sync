  
from django.urls import path
from .api_view_controller import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom

urlpatterns = [
    path('room', RoomView.as_view(),name='rooms'),
    path('create-room', CreateRoomView.as_view(),name="create"),
    path('get-room', GetRoom.as_view(),name="get"),
    path('join-room', JoinRoom.as_view(),name="join"),
    path('user-in-room', UserInRoom.as_view(),name="user"),
    path('leave-room', LeaveRoom.as_view(),name="leave"),
    path('update-room', UpdateRoom.as_view(),name="update")
]