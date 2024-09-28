from typing import List, Dict, Tuple
from datetime import datetime, timedelta
from app.events import events
from googlemaps.distance_matrix import distance_matrix

teams = {
    "Team 1":   None,
    "Team 2":   None,
    "Team 3":   None,
    "Team 4":   None,
    "Team 5":   None,
    "Team 6":   None,
    "Team 7":   None,
    "Team 8":   None,
    "Team 9":   None,
    "Team 10":  None
}



def assign_events_to_teams(events: List[events], teams: List[str]) -> Dict[str, List[events]]:
    events.sort(key=lambda event: event[1])

    team_assignments = {team: [] for team in teams}

    for event in events:
        best_team = None
        best_time_gap = timedelta.max

        for team in teams:
            if not team_assignments[team]:
                time_gap = timedelta(0)
            else:
                last_event = team_assignments[team][-1]
                travel_time = timedelta(0)
                time_gap = (event[1] - last_event[2]) - travel_time

            if time_gap >= timedelta(0) and time_gap < best_time_gap:
                best_time_gap = time_gap
                best_team = team

        if best_team is not None:
            team_assignments[best_team].append(event)

    return team_assignments

