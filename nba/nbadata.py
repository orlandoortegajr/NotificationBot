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
                team_dict[team["fullName"]] = Team(team["fullName"], team["tricode"], 
                                                   team["teamId"], team["nickname"])
    
    return team_dict

def get_team_games(teams, team_id):
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
        for game in schedules["league"][region]:
            team_schedule.append(game["gameUrlCode"]+game["homeStartTime"])

    return format_games(teams, team_schedule)

def format_games(teams, schedule_list):
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
        home = __find_team(teams, game[9:12])
        away = __find_team(teams,game[12:15])
        hour = game[15:17]
        minutes = game[17:19]
        final_schedule.append([home,away, month+"/"+day+"/"+year, hour+":"+minutes])
    
    return final_schedule

def __find_team(teams, team_tricode):
    """
    Auxilary function to find the team that matches the tricode.

    Args:
        team_tricode: the tricode of the given team.

    Returns:
        corresponding team for the given tricode
    """

    #team = key(full team names) in the dictionary of teams
    for team in teams:
        if(teams[team].get_tricode() == team_tricode):
            return team


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

