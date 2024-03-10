import spotify_api
import youtube_api

def migrate_playlist(spotify_auth, youtube_auth, playlist):
    yt = youtube_api.get_youtube_auth()
    yt_playlist = yt.playlists().insert(...).execute() 

    tracks = spotify_api.get_playlist_tracks(spotify_auth, playlist['id'])
    for track in tracks:
        search_result = youtube_api.search_track(yt, track['track']['name'], track['track']['artists'][0]['name'])
        # Do something with the search result (find the best match)  
        youtube_api.add_track_to_playlist(yt, yt_playlist['id'], search_result['id']['videoId'])

def main():
    sp = spotify_api.get_spotify_auth()
    yt = youtube_api.get_youtube_auth()
    playlists = spotify_api.get_user_playlists(sp)
    for playlist in playlists:
        migrate_playlist(sp, yt, playlist)

if __name__ == '__main__':
    main()
