import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
from pytube import YouTube
import pytube
import youtube_dl
import re


def del_symbols(song):
    new_song = re.sub(r'[^0-9A-Za-zа-я- А-Я]', '', song)
    return new_song


def search(music, performers):
    videos_search = VideosSearch(f'{performers} - {music}')
    video_result = videos_search.result()["result"][0]["link"]
    return video_result


# Download music from Youtube
def download(video, song_name, artists):
    try:
        video = YouTube(video)
        video.title = del_symbols(video.title)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path="music/", filename=f"{', '.join(artists)} - {song_name}.mp3")
    except:
        print("Error download")


SPOTIPY_CLIENT_ID = "889ef760014a45519839b310c46e19b3"
SPOTIPY_CLIENT_SECRET = "d2a26a78a1c142d6afdd0ac54a05ea3a"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
playlist = spotify.playlist(playlist_id="04Ky7zkWTFpay2XVHPkfKc")


for i, row in enumerate(playlist['tracks']['items']):
    song_name = row['track']['name']
    artists = row['track']['artists']
    art = [res['name'] for res in artists]
    lazy_url = row['track']['preview_url']

    print(f"{', '.join(art)} - {song_name}")
    download(search(song_name, art), song_name, art)

