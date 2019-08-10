import json
import requests
from settings import weather_key
"""
This file handles all data processing from looking at json files to making 
API calls.
"""

def find_country_code(country):
    """
    Gets the correct 2-letter country code in order to make api calls
    """

    #open the json file
    with open('countrycodes.json','r') as c:
        country_dict = json.load(c)
    #compare each item to find the matching country
    for item in country_dict:
        #make comparisons with both items lowercase
        if(country.lower() == item["name"].lower()):
            #return the lowercase form of the country code
            return item["code"].lower()
    
    #TODO: make exception for when the country could not be found
    print("Country was not found")

def get_weather_data(city, country_code):
    """
    Obtains the weather data from the city in the given country by the user.
    This data includes weather status, description, temp, humidity, max_temp, min_temp, wind_speed.
    """

    #{0} = city name
    #{1} = country code
    #{2} = api key
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}'.format(city, country_code, weather_key)
    )

    #TODO: properly handle successful/unsuccessful api calls
    if(response):
        print("call successful!")
    else:
        print("An error occured")
        return {"error": "data could not be obtained"}
    
    json_data = response.json()

    #store data from api data in json format in their respective keys
    print(json_data)
    weather_dict = dict(
        status = json_data["weather"][0]["main"], 
        description = json_data["weather"][0]["description"], 
        temperature = json_data["main"]["temp"], 
        humidity = json_data["main"]["humidity"],
        max_temperature = json_data["main"]["temp_max"], 
        min_temperature = json_data["main"]["temp_min"],
        wind_speed =  json_data["wind"]["speed"]
    )

    return weather_dict