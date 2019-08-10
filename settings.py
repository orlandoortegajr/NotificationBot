# settings.py
from dotenv import load_dotenv
import os
load_dotenv()

weather_key = os.getenv("WEATHER_API_KEY")

#Test to see if variables were obtained
if __name__ == "__main__":
    print(weather_key)