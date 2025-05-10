from sample_proj.helpers.vault.vault_access import VaultAccess
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self):
        self.spotify_credentials = None  # will be set in _get_spotify_key
        self.sp = None # will be set in _get_spotify_connection
        self.scope = "playlist-modify-private,user-library-read"
        self.vault = VaultAccess()

        self._get_spotify_key()
        self._get_spotify_connection()

        self.user_id = self.sp.current_user()['id']

    def _get_spotify_connection(self):
        try:
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                scope=self.scope,
                redirect_uri='https://example.com',
                client_id=self.spotify_credentials.get('client_id'),
                client_secret=self.spotify_credentials.get('client_secret'),
            ))
        except spotipy.SpotifyException as e:
            print(f"Error initializing Spotify client: {e}")
            raise

    def _get_spotify_key(self):
        path = {
            'path': 'spotify',
            'mount': 'udemy_course'
        }
        self.spotify_credentials = self.vault.pull_data(**path)

    def _search_titles_songs(self, play_list):
        uri_list = []
        for title, artist in play_list.items():
            spotify_song = self.sp.search(q=f'track:{title} artist:{artist}', type='track', limit=1)
            try:
                uri_list.append(spotify_song['tracks']['items'][0]['uri'])
            except IndexError:
                print(f"ERROR !! --> Song not found: {title} BY {artist}")
        return uri_list

    def create_playlist(self, playlist_name, date=None):
        playlist_id = self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=False,description=f'Created by Python - playlist for date {date}')['id']

        return playlist_id


    def add_songs_to_playlist(self, playlist_id, songs_play_list):
        songs_uri = self._search_titles_songs(songs_play_list)

        self.sp.playlist_add_items(playlist_id=playlist_id, items=songs_uri)



