from django.views.generic import View
from django.shortcuts import render
import os

from geopy.distance import vincenty
import requests
import json

from tmap.models import ChargingStation
from tour.models import TouristSpotData


class TmapView(View):

    def get(self, request, *args, **kwargs):
        api_key = os.environ.get("TMAP_API_KEY")
        return render(
            request,
            "tmap.html",
            context={
                "api_key": api_key,
            }
        )
