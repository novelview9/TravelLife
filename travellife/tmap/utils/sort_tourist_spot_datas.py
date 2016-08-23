from geopy.distance import vincenty

from tour.models import TouristSpotData


def sort_tourist_spot_datas(startX, startY):
    start_point = (startX, startY)
    spot_data_tuple_array = []
    tourlist_spot_datas = TouristSpotData.objects.all()
    for spot_data in tourlist_spot_datas:
        end_point = (spot_data.latitude, spot_data.longitude)
        distance = vincenty(start_point, end_point).meters
        spot_data_tuple = (spot_data.id, distance)
        spot_data_tuple_array.append(spot_data_tuple)
    sorted_spot_data_tuple_array = sorted(spot_data_tuple_array, key=lambda x: x[1])
    return sorted_spot_data_tuple_array[:100]
