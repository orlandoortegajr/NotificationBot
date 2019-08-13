"""
Contains the following helper methods:
    Kelvin -> Celcius
    Kelvin -> Fahrenheit
"""

def kelvin_to_celcius(temperature):
    """
    Converts temperature from kelvin to celcius.

    Args:
        temperature: temperature to be converted.
    
    Returns:
        temperature converted from kelvin to celcius.
    """
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature):
    """
    Converts temperature from kelvin to fahrenheit.

    Args:
        temperature: temperature to be converted.
    
    Returns:
        temperature converted from kelvin to fahrenheit.
    """
    return (temperature - 273.15) * (9/5) + 32