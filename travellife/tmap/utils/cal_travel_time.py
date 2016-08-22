import os
import json

import requests


def cal_travel_time(startX, startY, endX, endY):
    url = "https://apis.skplanetx.com/tmap/routes?version=1&format=json"
    headers = {
        'appKey': os.environ.get("TMAP_API_KEY")
    }
    data = {
        "startX": startX,
        "endX": endX,
        "startY": startY,
        "endY": endY,
        "reqCoordType": "WGS84GEO",
    }
    response = requests.post(
        url,
        headers=headers,
        data=data,
    )
    json_data = json.loads(response.text)
    try:
        travel_seconds = json_data.get("features")[0].get("properties").get("totalTime")
        travel_minutes = int(travel_seconds / 60)
        return travel_minutes
    except TypeError:
        return
