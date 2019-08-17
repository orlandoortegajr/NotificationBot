import requests
from .team import Team

def get_nba_teams():
    """
    Formats the nba teams from response into a usable format.

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

