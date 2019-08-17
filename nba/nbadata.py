import requests
from .team import Team
"""
This file handles all data processing from API calls
"""

def get_nba_teams():
    """
    Formats the nba teams from response in the following format: a dictionary
    with key the full team name and the value being additional data: tricode, id, and nickname

    Returns:
        dictionary of teams and their details
    """

    team_data = __nba_response_teams()
    team_dict = dict()

    #break down response so only the useful data is extracted
    for region in team_data["league"]:
        for team in team_data["league"][region]:
            if(team["isNBAFranchise"] == True and team["isAllStar"] == False):
                team_dict[team["fullName"]] = Team(team["fullName"], team["tricode"], team["teamId"], team["nickname"])
    
    return team_dict

def get_team_schedule(team_id):
    """
    Processes the nba schedules for the given team for use.

    Args:
        team_id: id code for the nba team from which the schedule will be obtained.
    
    Returns:
        A list of tuples containing the matchup in the first index, and the date in the second index.
    """
    schedules = __nba_response_schedules(team_id)
    team_schedule = []

    for region in schedules["league"]:
        if(region == "lastStandardGamePlayedIndex"):
            continue
        for game in region:
            team_schedule.append(game["gameUrlCode"])

    return format_games(team_schedule)

def format_games(schedule_list):
    """
    Formats the games for cleaner use.

    Args:
        schedule_list: list of all the scheduled matchups for the team
    
    Returns:
        a list of tuples with the first index being the matchup, and the second being the date
    """
    final_schedule = []
    for game in schedule_list:
        year = game[0:4]
        month = game[4:6]
        day = game[6:8]
        teams = game[9:15]
        final_schedule.append((teams, month+"/"+day+"/"+year))
    
    return final_schedule


def __nba_response_teams():
    """
    Handles api calls for NBA team data.
    
    Returns:
        Response in JSON format containing all NBA non franchised and franchised teams.
    """

    response = requests.get("http://data.nba.net/10s/prod/v2/2019/teams.json")

    #TODO: properly handle successful/unsuccessful api calls
    if(response):
        print("nba team call successful!")
    else:
        print("An error occured")
        return {"error": "data could not be obtained"}
    
    return response.json()

def __nba_response_schedules(team_id):
    """
    Handles api calls for NBA team schedule data.

    Args:
        team_id: id code for the nba team from which the schedule will be obtained.
    
    Returns:
        Response in JSON format containing all of the respective team's season games.
    """

    response = requests.get("http://data.nba.net/10s/prod/v1/2019/teams/{0}/schedule.json".format(team_id))

    #TODO: properly handle successful/unsuccessful api calls
    if(response):
        print("nba team schedule call successful!")
    else:
        print("An error occured")
        return {"error": "data could not be obtained"}
    
    return response.json()
