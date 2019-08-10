from .w_data import find_country_code, get_weather_data
"""
Representation of weather object, allowing for weather data to be used in other modules.
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

        #TODO: Check if city exists
        self.city = city.lower()
        self.country_code = find_country_code(country) 
        #dictionary containing all weather data
        self.weather_dict = get_weather_data(self.city, self.country_code)   
    
    def get_temperature(self):
        #TODO: Convert to celcius
        #TODO: Give user opportunity to choose between celcius or fahrenheit
        pass
    
    def get_city(self):
        return self.city

    def get_code(self):
        return self.country_code

    #TODO: Allow user to change their location


    


    
    
