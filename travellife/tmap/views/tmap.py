from django.views.generic import View
from django.shortcuts import render
from math import pi, asin, sqrt, pow, sin, cos
import os

from geopy.distance import vincenty
import requests
import json

from tmap.models import ChargingStation
from tour.models import TouristSpotData


def return_real_time(startX, startY, endX, endY):
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
    real_time = json_data.get("features")[0].get("properties").get("totalTime")
    return real_time


class TmapView(View):

    def get(self, request, *args, **kwargs):
        pA_x = 126.98217734415019
        pA_y = 37.56468648536046
        # pB_x = 129.07579349764512
        # pB_y = 37.17883196265564
        point1 = (pA_x, pA_y)
        # point2 = (pB_x, pB_y)
        # distance = vincenty(point1, point2).meters
        # charging_stations = ChargingStation.objects.all()
        charging_stations = ""

        tourlist_spot_datas = TouristSpotData.objects.all()
        distances = []
        for spot_data in tourlist_spot_datas:
            point2 = (spot_data.latitude, spot_data.longitude)
            distance = vincenty(point1, point2).meters
            data = (spot_data.id, distance)
            distances.append(data)
        distances = sorted(distances, key=lambda x: x[1])
        middle = distances[int(len(distances)/2)]
        spot_middle_data = TouristSpotData.objects.get(id=middle[0])
        pB_x, pB_y = float(spot_middle_data.longitude), float(spot_middle_data.latitude)
        real = return_real_time(pA_x, pA_y, pB_x, pB_y)
        api_key = os.environ.get("TMAP_API_KEY")
        return render(
            request,
            "tmap.html",
            context={
                # "distance": distance,
                "middle": middle,
                "real": real,
                "distances": distances,
                "api_key": api_key,
                "charging_stations": charging_stations,
            }
        )
