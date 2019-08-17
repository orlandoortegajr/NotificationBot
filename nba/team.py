"""
Contains the Team object used represent NBA teams
"""

class Team:
    """
    Object representing NBA teams containing the team name, it's three letter code,
    unique team id, nickname and their respective conference.
    """
    def __init__(self, name, tricode, teamID, nickname, conference):
        self.name = name
        self.tricode = tricode
        self.id = teamID
        self.nickname = nickname
        self.conference = conference

    def get_name(self):
        return self.name
    
    def get_tricode(self):
        return self.tricode
    
    def __get_id(self):
        return self.id

    def get_nickname(self):
        return self.nickname
    
    def get_conference(self):
        return self.conference
    
    def __str__(self):
        return self.name + ", " + self.tricode
    
