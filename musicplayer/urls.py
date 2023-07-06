from django.urls import path
from musicplayer.views import music_view

urlpatterns = [
    path("", music_view, name="musicplayer"),
]