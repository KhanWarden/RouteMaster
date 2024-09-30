from app import maps, events
from app.events import get_events
from app.maps import make_teams


def main():
    teams = make_teams()
    print(teams)


if __name__ == '__main__':
    main()
