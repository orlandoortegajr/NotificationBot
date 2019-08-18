from .nbadata import get_nba_teams, get_team_games
from .team import Team
from datetime import datetime

class League:
    """
    Object containing all of the teams in the league and allowing for their schedules to be found.
    """
    def __init__(self):
        self.teams = get_nba_teams()

    def get_team_data(self, team_name):
        """
        Retrieves the data obtained from the given team which includes:
        nickname, tricode and id.

        Args:
            team_name: Full name of the team being looked at.
        
        Returns:
            data obtained from api call from given team.
        """
        return self.teams[team_name]
    
    def get_team_schedule(self, team_name):
        """
        Retrieves the entire game schedule for the given team.

        Args:
            team_name: full name of the team being looked at.
        
        Returns:
            the entire schedule for the given team in a list of tuples format where the first 
            index is the matchup and the second the date.
        """
        team = self.teams[team_name]
        schedule = get_team_games(self.teams, team.get_id())
        final_schedule = []

        for game in schedule:
            final_schedule.append("{0} vs. {1} on {2} at {3}".format(game[0], game[1], game[2], game[3]))

        return final_schedule



    def get_next_game(self, team_name):
        """
        Retrieves the next game for the given team.

        Args:
            team_name: full name of the team being looked at.
        
        Returns:
            the next game on schedule for the given team in a tuple format where the first index is 
            the matchup and the second the date.
        """
        
        current_date = datetime.now()
        schedule = self.get_team_schedule("Toronto Raptors")

        for game in schedule:
            if(game[2] > current_date):
                return "{0} vs. {1} on {2} at {3}".format(game[0], game[1], game[2], game[3])