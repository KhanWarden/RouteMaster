import json
import googlemaps
from googlemaps.distance_matrix import distance_matrix


def get_data(api_key, origin, destination, departure_time):
    """ Get JSON data from Google Maps API """
    data = distance_matrix(api_key, origin, destination, departure_time, mode="driving", traffic_model='pessimistic')
    return data


def get_departure_time_from_data(api_key, origin, destination, departure_time):
    data = distance_matrix(api_key, origin, destination, departure_time=departure_time, traffic_model='pessimistic', mode='driving')

    duration_in_traffic = data['rows'][0]['elements'][0]['duration_in_traffic']
    seconds = duration_in_traffic['value']  # Get seconds

    return seconds
