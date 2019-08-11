from .w_data import find_country_code, get_weather_data
from .helpers import kelvin_to_celcius, kelvin_to_fahrenheit
"""
Representation of weather object, allowing for weather data to be used in other modules.

All data accessed is current weather data
"""

class Weather:
    """
    Object representing weather data, also handles all operations including
    obtaining data and making api calls.
    """

    def __init__(self, city, country):
        """
        Initializes weather object containing all data required to send a weather notification
        """
        location = []
        location = self._format_location(city, country)
        self.city = location[0]
        self.country_code = location[1] 
        #weather data structure
        self.weather_dict = get_weather_data(self.city, self.country_code)   
    
    def get_city(self):
        """
        Returns current city
        """

        return self.city

    def get_code(self):
        """
        Returns country 2-letter code
        """

        return self.country_code

    def get_status(self):
        """
        Returns weather status
        """

        return self.weather_dict["status"]

    def get_description(self):
        """
        Returns the current weather's description
        """

        return self.weather_dict["description"]

    def get_temperature(self, c_temp, t_temp = 0):
        """
        Return the temperature corresponding to the given letter:\n
        c -> celcius \n
        f -> fahrenheit \n
        k -> kelvin \n 

        To access max and minimum temperatures use 1, -1 respectively as the third argument, no need for use when asking for current temperature
        """
        #default temperature type to regular
        temp = self.weather_dict["temperature"]

        if(t_temp > 1 or t_temp < - 1):
            #TODO: handle error for when user enters incorrect third argument
            print("invalid value")
        elif(t_temp == 1):
            temp = self.weather_dict["max_temperature"]
        elif(t_temp == -1):
            temp = self.weather_dict["min_temperature"]

        if(c_temp == "c"):
            return kelvin_to_celcius(temp)
        elif(c_temp == "f"):
            return kelvin_to_fahrenheit(temp)
        elif(c_temp == "k"):
            return temp
        else:
            #TODO: handle error when wrong type of temperature is asked for
            return -99999

    def get_humidity(self):
        """
        Returns weather humidity in %
        """

        return self.weather_dict["humidity"]

    def get_wind_speed(self):
        """
        Returns wind speed in meters/seconds
        """

        return self.weather_dict["wind_speed"]

    def _format_location(self, city, country):
        """
        Returns location data in the correct format 
        """

        return [city.lower(), find_country_code(country)]

    def set_new_location(self, city, country):
        """
        Sets the variables representing location in the object
        """

        #TODO: Check if city exists
        #obtain the correct format first before setting the values
        location = self._format_location(city, country)
        self.city = location[0]
        self.country_code = location[1]
        self.weather_dict = get_weather_data(self.city, self.country_code)   



    


    
    
