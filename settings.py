# settings.py
from dotenv import load_dotenv
import os
load_dotenv()

weather_key = os.getenv("WEATHER_API_KEY")
email = os.getenv("EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("RECEIVER")

#Test to see if variables were obtained
if __name__ == "__main__":
    print(weather_key)