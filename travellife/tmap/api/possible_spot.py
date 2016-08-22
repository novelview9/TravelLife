from rest_framework.views import APIView
from rest_framework.response import Response

from tmap.utils import sort_tourist_spot_datas
from tmap.utils import cal_travel_time
from tmap.utils import halve_array
from tour.models import TouristSpotData


class PossibleSpotAPIView(APIView):

    def post(self, request, *args, **kwargs):
        startX = request.POST.get("startX")
        startY = request.POST.get("startY")
        preferred_time = request.POST.get("preferred_time")
        sorted_spot_data_tuple_array = sort_tourist_spot_datas(startX, startY)
        minified_array = halve_array(startX, startY, sorted_spot_data_tuple_array, preferred_time)
        travel_minute_array = []
        for tuple_data in minified_array:
            spot_id = tuple_data[0]
            spot_data = TouristSpotData.objects.get(id=spot_id)
            travel_minute = cal_travel_time(
                startX,
                startY,
                spot_data.longitude,
                spot_data.latitude,
            )
            if travel_minute:
                tuple_travel_minute = (
                    spot_id,
                    travel_minute,
                )
                travel_minute_array.append(tuple_travel_minute)
        sorted_travel_minute_array = sorted(travel_minute_array, key=lambda x: abs(x[1]-int(preferred_time)))

        data = {
            "spot_datas": sorted_travel_minute_array,
        }
        return Response(
            data=data,
        )
