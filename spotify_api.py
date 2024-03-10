import spotipy
import os

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'  # Or a suitable redirect URI

def get_spotify_auth():
    scope = 'playlist-read-private'  # Or adjust scopes as needed
    auth = spotipy.oauth2.SpotifyOAuth(
        SPOTIFY_CLIENT_ID, 
        SPOTIFY_CLIENT_SECRET, 
        SPOTIFY_REDIRECT_URI,
        scope=scope
    )
    return auth

def get_user_playlists(auth):
    spotify = spotipy.Spotify(auth_manager=auth)
    results = spotify.current_user_playlists()
    return results['items']

def get_playlist_tracks(auth, playlist_id):
    spotify = spotipy.Spotify(auth_manager=auth)
    results = spotify.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks 
