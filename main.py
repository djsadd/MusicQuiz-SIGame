import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
from pytube import YouTube
import re


class Music:
    def __init__(self, music):
        pass


class SpotifyAccount:
    SPOTIPY_CLIENT_ID = "889ef760014a45519839b310c46e19b3"
    SPOTIPY_CLIENT_SECRET = "d2a26a78a1c142d6afdd0ac54a05ea3a"

    def __init__(self, playlist):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=self.SPOTIPY_CLIENT_ID,
            client_secret=self.SPOTIPY_CLIENT_SECRET)
        )

        self.playlist = self.spotify.playlist(playlist_id=self.get_id_playlist(playlist))
        self.songs = []
        self.songs_di = {}

    def get_id_playlist(self, playlist):
        # IF URL UPDATE THESE STRING
        return playlist

    def del_symbols(self, song):
        return re.sub(r'[^0-9A-Za-zа-я- А-Я]', '', song)

    def download(self, video, song_name, artists):
        try:
            print(f"Download {video, song_name, artists}")
            video = YouTube(video)
            video.title = self.del_symbols(video.title)
            stream = video.streams.filter(only_audio=True).first()
            filename = f"{', '.join(artists)} - {song_name}.mp3"
            path = "static/music/"
            stream.download(output_path=path, filename=filename)
            return filename
        except:
            # Нужно возвращать ошибку скачивания определенного трека
            print(f"{artists} - {song_name}: Download Error")

    def search(self, music, performers):
        print(f"Search: {', '.join(performers)} - {music}")
        videos_search = VideosSearch(f'{', '.join(performers)} - {music}')
        video_result = videos_search.result()["result"][0]["link"]
        return video_result

    def songs_download(self):
        for i, row in enumerate(self.playlist['tracks']['items']):
            song_name = row['track']['name']
            artists_dict = row['track']['artists']
            artists = [res['name'] for res in artists_dict]
            lazy_url = row['track']['preview_url']
            print(f"{', '.join(artists)} - {song_name}")
            file = self.download(self.search(song_name, artists), song_name, artists)
            print(f"{', '.join(artists)} - {song_name} - {file}")

            self.songs.append({'name': file, "path": f'{file}', "number": i})
        else:
            return "Songs downloaded"

    def get_list_song(self):
        return self.songs
