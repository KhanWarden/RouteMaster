""" Events module, which loads events from .txt, sorts them by time (in ascending order) and returns in get_events()"""

from datetime import datetime
from pathlib import Path

project_folder = Path(__file__).parent.parent
events_file_path = project_folder / 'app' / 'events.txt'

""" The date that you need """
fixed_date = datetime(2024, 10, 5)


def time_of_event_start(hour, minute):
    return fixed_date.replace(hour=hour, minute=minute)


def time_of_event_end(hour, minute):
    return fixed_date.replace(hour=hour, minute=minute)


def load_events_from_txt(filename):
    _events = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, location, start_time, end_time = line.strip().split(';')
                lat, lng = map(float, location.split(','))
                start_hours, start_minutes = map(int, start_time.split(':'))
                end_hours, end_minutes = map(int, end_time.split(':'))

                _event = {
                    'name': name.strip(),
                    'location': (lat, lng),
                    'start_time': time_of_event_start(start_hours, start_minutes),
                    'end_time': time_of_event_end(end_hours, end_minutes)
                }
                _events.append(_event)
    except FileNotFoundError:
        print('File not found')
    return _events


def sort_events_by_time(_events):
    _sorted_events = sorted(_events, key=lambda event: event['start_time'])
    return _sorted_events


def get_events():
    events = load_events_from_txt(events_file_path)
    return sort_events_by_time(events)
