""" Maps module which calculates distance between locations in a pessimistic way """

from datetime import time, datetime
import googlemaps
from googlemaps.distance_matrix import distance_matrix

from app.config import API_KEY
from app.events import get_events

gmaps = googlemaps.Client(key=API_KEY)


def parse_direction(data):
    destination = data.get('destination_addresses', [None])[0]
    origin = data.get('origin_addresses', [None])[0]
    duration_in_traffic = data.get('rows', [{}])[0].get('elements', [{}])[0].get('duration_in_traffic', {}).get('value',
                                                                                                                None)
    distance = data.get('rows', [{}])[0].get('elements', [{}])[0].get('distance', {}).get('text', None)

    print(f"Отправление из: {origin}")
    print(f"Прибытие в: {destination}")
    print(f"Время в пути: {duration_in_traffic} секунд")
    print(f"Расстояние: {distance}")


def count_distance():
    locs = get_events

    location1 = locs[0]
    location2 = locs[1]

    time_string = "2024, 8, 29 21:00"
    parsed_time = datetime.strptime(time_string, "%Y, %m, %d %H:%M")
    direction = distance_matrix(gmaps, location1, location2, departure_time=parsed_time, mode='driving',
                                traffic_model="pessimistic")
    parse_direction(direction)
