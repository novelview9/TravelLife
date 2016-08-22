import os

import requests
import json


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
    travel_time = json_data.get("features")[0].get("properties").get("totalTime")
    return travel_time
