"""
Contains the Team object used represent NBA teams
"""

class Team:
    """
    Object representing NBA teams containing: 
        team name -
        three letter code -
        unique team id - 
        nickname.
    """
    def __init__(self, name, tricode, teamID, nickname):
        self.name = name
        self.tricode = tricode
        self.id = teamID
        self.nickname = nickname

    def get_name(self):
        return self.name
    
    def get_tricode(self):
        return self.tricode
    
    def __get_id(self):
        return self.id

    def get_nickname(self):
        return self.nickname
    
    def __str__(self):
        return self.name + ", " + self.tricode
    
