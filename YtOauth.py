import json
import os
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow

from youtube_api import makePublicService


def makeService():
    credentials = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", scopes=["https://www.googleapis.com/auth/youtube"]
            )
            flow.run_local_server(port=8080, prompt="consent")

            credentials = flow.credentials
            print(credentials.to_json())
            return build("youtube", "v3", credentials=credentials)


def makePlaylist(serv, name):
    request = serv.playlists().insert(
        part="snippet", body={"snippet": {"title": str(name)}}
    )

    response = request.execute()
    return response["id"]


def addItemToPlaylist(service, pl_id, items):
    res = []
    for i in items:
        request = service.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": str(pl_id),
                    "resourceId": {"kind": "youtube#video", "videoId": i},
                }
            },
        )
        response = request.execute()
        print("Added")
        res.append(response)

    return res


#  addItemToPlaylist(test_pl_id,video_ids)
