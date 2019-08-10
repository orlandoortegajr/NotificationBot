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

        location = _format_location(city, country)
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

    def get_temperature_celcius(self, c_temp):
        """
        Return the temperature corresponding to the given letter:\n
        c -> celcius \n
        f -> fahrenheit \n
        k -> kelvin 
        """

        if(c_temp == "c"):
            return kelvin_to_celcius(self.weather_dict["temperature"])
        elif(c_temp == "f"):
            return kelvin_to_fahrenheit(self.weather_dict["temperature"])
        elif(c_temp == "k"):
            return self.weather_dict["temperature"]
        else:
            #TODO: handle error when wrong type of temperature is asked for
            return -99999

    def get_max_temperature(self, c_temp):
        """
        Return the maximum temperature corresponding to the given letter:\n
        c -> celcius \n
        f -> fahrenheit \n
        k -> kelvin 
        """

        if(c_temp == "c"):
            return kelvin_to_celcius(self.weather_dict["max_temperature"])
        elif(c_temp == "f"):
            return kelvin_to_fahrenheit(self.weather_dict["max_temperature"])
        elif(c_temp == "k"):
            return self.weather_dict["max_temperature"]
        else:
            #TODO: handle error when wrong type of temperature is asked for
            return -99999

    def get_min_temperature(self, c_temp):
        """
        Return the minimum temperature corresponding to the given letter:\n
        c -> celcius \n
        f -> fahrenheit \n
        k -> kelvin 
        """

        if(c_temp == "c"):
            return kelvin_to_celcius(self.weather_dict["min_temperature"])
        elif(c_temp == "f"):
            return kelvin_to_fahrenheit(self.weather_dict["min_temperature"])
        elif(c_temp == "k"):
            return self.weather_dict["min_temperature"]
        else:
            #TODO: handle error when wrong type of temperature is asked for
            return -99999

    def get_humidity(self):
        """
        Returns weather humidity
        """

        return self.weather_dict["humidity"]

    def get_wind_speed(self):
        """
        Returns wind speed
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
        location = _format_location(city, country)
        self.city = location[0]
        self.country_code = location[1]



    


    
    
