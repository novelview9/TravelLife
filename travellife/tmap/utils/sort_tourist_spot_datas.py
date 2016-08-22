from geopy.distance import vincenty


def sort_tourist_spot_datas(start_point, tourlist_spot_datas):
    spot_data_tuple_array = []
    for spot_data in tourlist_spot_datas:
        end_point = (spot_data.latitude, spot_data.longitude)
        distance = vincenty(start_point, end_point).meters
        spot_data_tuple = (spot_data.id, distance)
        sorted_spot_data_tuple_array.append(spot_data_tuple)
    sorted_spot_data_tuple_array = sorted(spot_data_tuple_array, key=lambda x: x[1])
    return sorted_spot_data_tuple_array
