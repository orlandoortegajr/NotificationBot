from nba.league import League
"""
Contains all functions to setup the messages to be sent to the user about NBA games.
"""

def format_nba_msg(team_name):
    nba_team = League()
    final_str = "\nNext NBA game for {0}: \n        {1}\n".format(team_name, nba_team.get_next_game(team_name))
    return final_str