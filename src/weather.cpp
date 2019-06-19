#include <iostream>
#include <cpr/cpr.h>
#include "../include/weather.h"
#include <string>

Weather::Weather(std::string userLocation)
{
    this->location = userLocation;
}

std::string Weather::getWeatherData()
{
    //concatenate api call with the location given by the user to access weather details.
    auto r = cpr::Get(cpr::Url{"api.openweathermap.org/data/2.5/weather?q="+this->location+"&appid=c4f6f914d1d83a9e8a05f9e6fff5cad4"});
    return r.text;
}



