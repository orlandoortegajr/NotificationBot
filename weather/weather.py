from .weatherdata import find_country_code, get_weather_data
from .helpers import kelvin_to_celcius, kelvin_to_fahrenheit
"""
Representation of weather object, allowing for weather data to be used in other modules.

All data accessed is current weather data.
"""

class Weather:
    """
    Object representing weather data, allowing for access and also editing of the current location and it's corresponding weather data.
    """

    def __init__(self, city, country):
        """
        Initializes weather object containing all data required to send a weather notification.

        Args:
            city: the city in which the weather will be looked at.
            country: the country where the city belongs.
        """
        location = []
        location = self.__format_location(city, country)
        self.city = location[0]
        self.country_code = location[1] 
        #weather data structure
        self.weather_dict = get_weather_data(self.city, self.country_code)   
    
    def get_city(self):
        """
        Get the selected city.

        Returns:
            Current city.
        """

        return self.city

    def get_code(self):
        """
        Get the selected country's 2-letter code.

        Returns:
            Country 2-letter code.
        """

        return self.country_code

    def get_status(self):
        """
        Get the main status of the weather(rainy, sunny, etc...).

        Returns:
            Weather status.
        """

        return self.weather_dict["status"]

    def get_description(self):
        """
        Get the current weather's description(i.e. light drizzle, light clouds).

        Returns:
            Current weather's description.
        """

        return self.weather_dict["description"]

    def get_temperature(self, c_temp, t_temp = 0):
        """
        Gets the temperature based on the given conditions passed as function arguments.

        Args:
            c_temp: character for temperature unit:
                c -> celcius,
                f -> fahrenheit,
                k -> kelvin.
            t_temp: number for the type of temperature:
                -1 -> minimum,
                 0 -> current,
                 1 -> maximum.
        
        Returns:
            Temperature based on the passed conditions
            
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
        Get the humidity of the current weather.

        Returns:
            %humidity.
        """

        return self.weather_dict["humidity"]

    def get_wind_speed(self):
        """
        Get the current wind speed in meters/second.

        Returns:
            Wind speed in meters/seconds.
        """

        return self.weather_dict["wind_speed"]

    def __format_location(self, city, country):
        """
        Formats the location variables given to conform API call requirements.

        Returns:
            Location data in the correct format, city name in lowercase and country converted to 2-letter country code.
        """

        return [city.lower(), find_country_code(country)]

    def set_new_location(self, city, country):
        """
        Sets the variables representing location in the object.

        Args:
            city: the selected city used for weather data.
            country: the country in which the city is located.
        """

        #TODO: Check if city exists
        #obtain the correct format first before setting the values
        location = self.__format_location(city, country)
        self.city = location[0]
        self.country_code = location[1]
        self.weather_dict = get_weather_data(self.city, self.country_code)   



    


    
    
