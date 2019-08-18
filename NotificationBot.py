from weather.weather import Weather
from nba.league import League
from setup import format_weather_msg, footer, subject
from settings import receiver
from mail.gmail import send_email

if __name__ == "__main__":
    #get the desired location's weather data
    w_data = Weather("Toronto", "Canada")

    #create the message text
    # msg_text = format_weather_msg(w_data) + footer()

    #send the msg
    # send_email(subject(),msg_text)

    nba_data = League()
    print(nba_data.get_next_game("Toronto Raptors"))

