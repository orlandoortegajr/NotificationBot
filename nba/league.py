from .nbadata import get_nba_teams, get_team_schedule


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
            the entire schedule for the given team in a list of tuples format where the first index is the matchup and the second the date
        """
        schedule = get_team_schedule()

    def get_next_game(self, team_name):
        """
        Retrieves the next game for the given team.

        Args:
            team_name: full name of the team being looked at.
        
        Returns:
            the next game on schedule for the given team in a tuple format where the first index is the matchup and the second the date
        """
        pass
