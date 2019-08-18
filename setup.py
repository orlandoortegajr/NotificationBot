from weather.setup import format_weather_msg
from nba.setup import format_nba_msg
"""
Contains all functions to setup the messages to be sent to the user
"""

def subject():
    return "Notifications from NotificationBot"

def footer():
    return "\nFrom your favourite bot: NotificationBot"

def create_message(w_data, team_name):
    final_message = format_weather_msg(w_data) + format_nba_msg(team_name) + footer()
    return final_message