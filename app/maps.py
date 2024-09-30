""" Maps module which calculates distance between locations in a pessimistic way """

from datetime import time, datetime, timedelta
import googlemaps
from googlemaps.distance_matrix import distance_matrix
from pathlib import Path

from app.config import API_KEY
from app.events import get_events
from app.parse_json import parse_json
from app.parse_json.parse_json import get_departure_time_from_data

gmaps = googlemaps.Client(key=API_KEY)


def make_teams():
    _events = get_events()

    teams = []
    remaining_events = _events[:]

    while remaining_events:
        current_team = []
        current_event = remaining_events.pop(0)
        current_team.append(current_event)

        end_time = current_event['end_time']
        formatted_end_time = int(end_time.timestamp())
        current_location = current_event['location']

        while True:
            next_game_index = -1
            min_travel_time = float('inf')

            for i, game in enumerate(remaining_events):
                travel_time = get_departure_time_from_data(gmaps, current_location, game['location'], formatted_end_time)
                if travel_time < min_travel_time:
                    start_time = game['start_time']
                    if (end_time + timedelta(seconds=travel_time)) <= start_time:
                        min_travel_time = travel_time
                        next_game_index = i

            if next_game_index == -1:
                break

            next_game = remaining_events[next_game_index]
            current_team.append(next_game)
            current_location = next_game['location']
            end_time = next_game['end_time']

            remaining_events.pop(next_game_index)

        teams.append(current_team)
    return teams
