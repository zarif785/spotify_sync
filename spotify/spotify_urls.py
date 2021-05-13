from django.urls import path
from .spotify_view_controller import *

urlpatterns = [
    path('get-auth-url', AuthURL.as_view(),name='auth'),
    path('redirect', spotify_callback,name='redirect'),
    path('is-authenticated', IsAuthenticated.as_view(),name='isauth'),
    path('current-song', CurrentSong.as_view(),name='current'),
    path('pause', PauseSong.as_view(),name='pause'),
    path('play', PlaySong.as_view(),name='play'),
    path('skip', SkipSong.as_view(),name='skip')
]