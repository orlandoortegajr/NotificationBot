import json
import requests
from settings import weather_key, current_path
import os.path
"""
This file handles all data processing from looking at json files to making 
API calls.
"""

def find_country_code(country):
    """
    Gets the correct 2-letter country code in order to make api calls.

    Args:
        country: the country where the city(location for weather) is located at.
    """

    data_folder = os.path.join(current_path,"data/")
    file = os.path.join(data_folder, "countrycodes.json")

    #open the json file
    with open(file,'r') as c:
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
    Processes JSON data obtained from API calls

    Args:
        city: the location where the data comes from.
        country_code: 2-letter code of the country where the city is located.

    Returns:
        Weather data needed which includes: weather status, description, temp, humidity, max_temp, min_temp, wind_speed.
    """

    #json data obtained from response
    json_data = __response_content(city, country_code)

    #store required data from response in their respective keys
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

def __response_content(city, country_code):
    """
    Handles api calls and their respective responses.

    Args:
        city: the location where the weather data comes from.
        country_code: 2-letter code of the country where the city is located.
    
    Returns:
        Response in JSON format
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
    
    return response.json()
