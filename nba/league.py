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
            team_name: full name of the team being looked at.
        
        Returns:
            data obtained from given team which includes nickname, tricode and id.
        """

        return self.teams[team_name]
    
    def get_team_schedule(self, team_name):
        """
        Retrieves the entire game schedule for the given team.

        Args:
            team_name: full name of the team being looked at.
        
        Returns:
            the entire schedule for the given team in a list in a readable format where the 
            elements are similar to the following format: "New Orleans Pelicans vs. Toronto Raptors on 10/22/2019 
            at 20:00" 
        """

        #obtains the given team's details from the team list
        team = self.teams[team_name]

        schedule = get_team_games(self.teams, team.get_id())
        final_schedule = []

        #formatting schedule to obtain a more human readable result
        for game in schedule:
            final_schedule.append("{0} vs. {1} on {2} at {3}".format(game[0], game[1], game[2], game[3]))

        return final_schedule



    def get_next_game(self, team_name):
        """
        Retrieves the next game for the given team.

        Args:
            team_name: full name of the team being looked at.
        
        Returns:
            the next game on schedule for the given team in a string format of the following style:
            "New Orleans Pelicans vs. Toronto Raptors on 10/22/2019 at 20:00"
        """
        
        team = self.teams[team_name]
        schedule = get_team_games(self.teams, team.get_id())

        current_date = datetime.now()

        for game in schedule:
            #convert string to date for proper dates comparison
            game_date = datetime.strptime(game[2],'%m/%d/%Y')
            if(game_date > current_date):
                return "{0} vs. {1} on {2} at {3}".format(game[0], game[1], game[2], game[3])