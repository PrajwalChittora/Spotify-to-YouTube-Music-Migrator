from googleapiclient.discovery import build
from credentials import yt_api
import json
from spotify_extract import query_builder
import time



def makePublicService(api_key):
    return build(serviceName='youtube',version='v3',developerKey=api_key)


def getVideoIds(queries, api):
    service = makePublicService(api)
    ids = []
    for query in queries:
        request = service.search().list(part="snippet", maxResults=2, q=query)
        response = request.execute()

        print(json.dumps(response, indent=2))  # Keep this for debugging

        if 'items' in response and len(response['items']) > 0: 
            for item in response['items']:
                if item['id']['kind'] == 'youtube#video':  # Check if it's a video
                    videoid = item['id']['videoId']
                    ids.append(videoid)
                else:
                    print(f"Skipping item (not a video): {item['id']}")   

        time.sleep(3) 
    return ids
# print(getVideoIds(queries))


