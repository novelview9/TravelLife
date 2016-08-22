import json
import os
import requests

from django.shortcuts import render
from django.views.generic import View


class AddressToPointView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "address.html",
            {},
        )

    def post(self, request, *args, **kwargs):

        address = request.POST.get("address_1")

        url = "https://openapi.naver.com/v1/map/geocode?encoding=utf-8&coord=latlng&output=json&query={addr}".format(
            addr=address,
        )

        headers = {
            "X-Naver-Client-Id": os.environ.get("NAVER_CLIENT_ID"),
            "X-Naver-Client-Secret": os.environ.get("NAVER_CLIENT_SECRET"),
            }

        response = requests.get(url, headers=headers)

        data = json.loads(response.text)

        latitude = data.get("result").get("items")[0].get("point").get("y")
        longitude = data.get("result").get("items")[0].get("point").get("x")
        point = {
            "latitude": latitude,
            "longitude": longitude,
        }

        return render(
            request,
            "address.html",
            {
                "point": point,
             },
        )
