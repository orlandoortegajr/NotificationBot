"""
Contains the following helper methods:
Kelvin -> Celcius
Kelvin -> Fahrenheit
"""

def kelvin_to_celcius(temperature):
    """
    Converts kelvin to celcius
    """
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature):
    """
    Converts kelvin to fahrenheit
    """
    return (temperature - 273.15) * (9/5) + 32