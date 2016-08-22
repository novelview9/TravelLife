import os
import requests
import json

from rest_framework.views import APIView
from rest_framework.response import Response


class AddressToPointAPIView(APIView):

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

        return Response(
            data=point,
        )
