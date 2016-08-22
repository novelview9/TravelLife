from django.shortcuts import render
from math import pi, asin, sqrt, pow, sin, cos
import os

from geopy.distance import vincenty


def tmap(request):
    pA_x = 126.98217734415019
    pA_y = 37.56468648536046
    pB_x = 129.07579349764512
    pB_y = 37.17883196265564
    point1 = (pA_x, pA_y)
    point2 = (pB_x, pB_y)
    distance = vincenty(point1, point2).meters
    api_key = os.environ.get("TMAP_API_KEY")
    return render(
        request,
        "tmap.html",
        context={
            "distance": distance,
            "api_key": api_key,
        }
    )
