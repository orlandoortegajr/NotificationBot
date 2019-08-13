from weather.weather import Weather
"""
Contains all functions to setup the messages to be sent to the user
"""

#TODO: register user's chosen categories so only the appropriate ones are chosen
#TODO: add master function which appends all the strings which complete the entire notification message

def subject():
    return "Notifications from NotificationBot"

def format_weather_msg(w : Weather):
    msg_text ="""\
    ===Weather Data===
    Location: {0}, {1}
    Temperature C: {2}
    Status: {3}
    Description: {4}

    Additional Information:
        Humidity: {5}
        Maximum Temperature: {6}
        Minimum Temperature: {7}
        Wind Speed: {8}
    """.format(
        w.get_city().capitalize(), 
        w.get_code().upper(), 
        "{0:.2f}".format(w.get_temperature("c")),
        w.get_status(),
        w.get_description().capitalize(),
        str(w.get_humidity())+"%",
        "{0:.2f}".format(w.get_temperature("c", 1)),
        "{0:.2f}".format(w.get_temperature("c",-1)),
        str(w.get_wind_speed()) + " meters/second"
        )

    return msg_text

def footer():
    return "\n    From your favourite bot: NotificationBot"