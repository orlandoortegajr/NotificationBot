#include <cpr/cpr.h>
#include "../include/weather.h"

//TODO: create a user object and pass that as the paramater
Weather::Weather(std::string userLocation)
{
    this->city = userLocation;

    auto data = getWeatherData();

    //setup local variables for weather data
    this->description = data["weather"][0]["description"];
    this->humidity = data["main"]["humidity"];
    this->windSpeed = data["wind"]["speed"];
    this->country = data["sys"]["country"]; 
    this->temperature = kelvinToCelcius(data["main"]["temp"]);

}

std::string Weather::getLocation()
{
    //example: Toronto, CA
    return this->city+", "+this->country;
}

std::string Weather::getDescription()
{
    return this->description;
}

double Weather::getTemperature()
{
    return this->temperature;
}

int Weather::getHumidity()
{
    return this->humidity;
}

double Weather::getWindSpeed()
{
    return this->windSpeed;
}


/*
*   ===========================
*       Private Functions
*   ===========================
 */


nlohmann::json Weather::getWeatherData()
{
    //concatenate api call with the location given by the user to access weather details.
    auto parameters = cpr::Parameters{{"q", this->city}, {"appid", "c4f6f914d1d83a9e8a05f9e6fff5cad4"}};
    auto r = cpr::Get(cpr::Url{"api.openweathermap.org/data/2.5/weather"}, parameters);

    //convert cpr response into json format for access
    nlohmann::json j = nlohmann::json::parse(r.text);

    return j;
}

double Weather::kelvinToCelcius(double temp)
{
    return temp - 273.15;
}







