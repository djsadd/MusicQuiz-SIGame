import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
SPOTIPY_CLIENT_ID = "889ef760014a45519839b310c46e19b3"
SPOTIPY_CLIENT_SECRET = "d2a26a78a1c142d6afdd0ac54a05ea3a"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
results = spotify.artist_top_tracks(lz_uri)


result = spotify.playlist(playlist_id="37i9dQZF1DZ06evO0yp56w")
for i, row in enumerate(result['tracks']['items']):
    song_name = row['track']['name']
    artists = row['track']['artists']
    lazy_url = row['track']['preview_url']
    print(song_name, lazy_url)
