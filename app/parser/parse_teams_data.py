def convert_datatime_to_timestamp(datatime):
    formatted_datatime = datatime.strftime('%H:%M')
    return formatted_datatime


def parse_result(teams):
    for i, team in enumerate(teams):
        print(f"\nTeam {i + 1}:")
        for j in team:
            print(j['name'], j['location'],
                  convert_datatime_to_timestamp(j['start_time']), convert_datatime_to_timestamp(j['end_time']))
