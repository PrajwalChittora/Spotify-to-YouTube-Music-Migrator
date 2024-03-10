import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']

def get_youtube_auth():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0) 
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('youtube', 'v3', credentials=creds)

def search_track(youtube, track_name, artist_name):
    """Searches for a track on YouTube based on the track name and artist name."""

    search_response = youtube.search().list(
        part='snippet',
        q=track_name + ' ' + artist_name,
        type='video',
        maxResults=1  # Adjust if you want more results
    ).execute()

    if search_response['items']: 
        return search_response['items'][0]  # Return the first result
    else:
        return None  # Or handle the case where no tracks are found

def create_playlist(youtube, title):
    """Creates a new playlist on YouTube with the given title."""

    playlist_response = youtube.playlists().insert(
        part='snippet,status',
        body={
            'snippet': {
                'title': title,
                'description': 'Playlist migrated from Spotify'  
            },
            'status': {
                'privacyStatus': 'public'  # Options: 'public', 'private', 'unlisted'
            }
        }
    ).execute()

    return playlist_response['id']  # Return the ID of the newly created playlist

def add_track_to_playlist(youtube, playlist_id, video_id):
    """Adds a track (specified by its video ID) to a YouTube playlist."""

    add_video_response = youtube.playlistItems().insert(
        part='snippet',
        body={
            'snippet': {
                'playlistId': playlist_id, 
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
    ).execute()

    return add_video_response
