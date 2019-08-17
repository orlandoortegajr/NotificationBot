from .nbadata import get_nba_teams


class League:
    """
    Object containing all of the teams in the league and allowing for their schedules to be found
    """
    def __init__(self):
        self.teams = get_nba_teams()

    def get_team_data(self, team_name):
        return self.teams[team_name]
    
    def get_team_schedule(self):
        pass
