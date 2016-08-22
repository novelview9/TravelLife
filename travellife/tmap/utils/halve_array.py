from tmap.utils import cal_travel_time
from tour.models import TouristSpotData


def halve_array(startX, startY, tupple_array, preferred_time):
    if len(tupple_array) < 50:
        return tupple_array
    mid = int(len(tupple_array)/2)
    mid_spot_id = tupple_array[mid][0]
    mid_spot_data = TouristSpotData.objects.get(id=mid_spot_id)

    mid_travel_time = cal_travel_time(
        startX,
        startY,
        mid_spot_data.longitude,
        mid_spot_data.latitude,
    )

    if mid_travel_time < int(preferred_time):
        return halve_array(
            startX,
            startY,
            tupple_array[mid+1:],
            preferred_time,
        )
    return halve_array(
        startX,
        startY,
        tupple_array[:mid],
        preferred_time,
    )
