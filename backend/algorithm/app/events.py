""" Events module, which loads events from .txt, sorts them by time (in ascending order) and returns in get_events()"""

from datetime import datetime
from pathlib import Path

algorithm_folder = Path(__file__).parent.parent
events_file_path = algorithm_folder / 'app' / 'events.txt'


def load_events_from_txt(filename):
    _events = []
    try:
        with open(filename, 'r') as file:
            year, month, day = map(int, file.readline().strip().split(','))
            fixed_date = datetime(year, month, day)

            for line in file:
                name, location, start_time, end_time = line.strip().split(';')
                lat, lng = map(float, location.split(','))
                start_hours, start_minutes = map(int, start_time.split(':'))
                end_hours, end_minutes = map(int, end_time.split(':'))

                _event = {
                    'name': name.strip(),
                    'location': (lat, lng),
                    'start_time': fixed_date.replace(hour=start_hours, minute=start_minutes),
                    'end_time': fixed_date.replace(hour=end_hours, minute=end_minutes)
                }
                _events.append(_event)
    except FileNotFoundError:
        print('File not found')
    return _events


def get_events():
    events = load_events_from_txt(events_file_path)
    return sorted(events, key=lambda event: event['start_time'])
