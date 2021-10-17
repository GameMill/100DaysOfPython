from requests import api
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json
import os


class MySpotipy:
    ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

    def __init__(self):
        self.load_config()
        self.setup_connection()

    def load_config(self):
        with open(f"{self.ROOT}spotify.key") as api_key:
            self.API_KEY = json.load(fp=api_key)

    def setup_connection(self):
        self.sp = Spotify(auth_manager=SpotifyOAuth(
            self.API_KEY["ClientID"],
            self.API_KEY["Secret"],
            self.API_KEY["RedirectURL"],
            scope="playlist-modify-private,playlist-read-private",
            cache_path=f"{self.ROOT}token.txt"
            ))

    def find_song(self,song):
        song = self.sp.search(song,1)
        if(len(song["tracks"]["items"]) == 0):
            return
        return song["tracks"]["items"][0]

    def create_playlist(self,playlist_name):
        user_id = self.sp.current_user()["id"]
        playlist = self.sp.user_playlist_create(user_id,playlist_name,False,False,"Hello world")
        print("Playlist Created")
        return playlist["id"]
    
    def add_song_to_playlist(self,playlist_id,songs):
        self.sp.playlist_add_items(playlist_id,songs)
        print("ADDED")
        
        