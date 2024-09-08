from Music_recom import *
from spotipy import *
import webbrowser
from time import sleep
from pyautogui import click

client_id = 'b0098e95461f47c6b866c5a14a8d15f2'
client_secret = 'e97ea31d5fb142bea223ba28e1f4e9d4'
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = Spotify(auth_manager=auth_manager)


def Play_music(predicted_emotion):
    song_name = Recommend_Song(predicted_emotion)
    results = spotify.search(q=song_name)
    track_id = results['tracks']['items'][0]['id']
    spotify.start_playback(uris=['spotify:track:' + track_id])


def Play_music_browser(song_name):
    webbrowser.open(f"https://open.spotify.com/search/{song_name}")
    sleep(13)
    click(x=1055, y=617)


Play_music_browser("Happy")
