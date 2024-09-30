from app.maps import make_teams
from app.parser import parse_result


def main():
    teams = make_teams()
    print(parse_result(teams))


if __name__ == '__main__':
    main()
