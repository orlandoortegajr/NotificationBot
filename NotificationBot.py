from weather.weather import Weather
from setup import create_message, subject
from mail.gmail import send_email
import schedule
import time


if __name__ == "__main__":
    def task():

        #get the desired location's weather data
        w_data = Weather("Toronto", "Canada")
        nba_team_name = "Toronto Raptors"

        #create the message text
        msg_text = create_message(w_data, nba_team_name)

        #send the msg
        send_email(subject(),msg_text)

    schedule.every().day.at("09:00").do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)
    


