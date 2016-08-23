import os
import json

import requests

from tour.models import TouristSpotData


def update_tour_model():

    TouristSpotData.objects.all().delete()

    tour_api_key = os.environ.get("TOUR_API_KEY")
    app_name = "travelife"
    keys = ["12", "14"]
    items = []

    for key in keys:
        url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey="\
            + "{service_key}&numOfRows=10000&contentTypeId={key}&MobileOS=ETC&MobileApp={app}&_type=json".format(
                service_key=tour_api_key,
                key=key,
                app=app_name,
            )

        response = requests.get(url)
        items += json.loads(response.text).get("response").get("body").get("items").get("item")

    for item in items:
        if item.get("mapx") and item.get("mapy") \
            and float(item.get("mapx")) > 124 and float(item.get("mapx")) < 131 \
            and float(item.get("mapy")) > 33 and float(item.get("mapy")) < 39 \
                and item.get("cat2") and item.get("addr1"):
                title = item.get("title")
                address = item.get("addr1")
                group = item.get("cat2")
                latitude = item.get("mapy")
                longitude = item.get("mapx")
                area_code = item.get("areacode")
                image_url = item.get("firstimage")
                thumbnailimage_url = item.get("firstimage2")

                spot_data = TouristSpotData.objects.create(
                    title=title,
                    group=group,
                    address=address,
                    latitude=float(latitude),
                    longitude=float(longitude),
                    area_code=area_code,
                    image_url=image_url,
                    thumbnailimage_url=thumbnailimage_url,
                )
