#include<string>
#include <nlohmann/json.hpp>
#pragma once
#ifndef WEATHER_H_
#define WEATHER_H_

class Weather {
    public:
        
        //TODO: change this to a user object parameter
        Weather(std::string userLocation);
        std::string getLocation();
        std::string getDescription();
        double getTemperature();
        int getHumidity();
        double getWindSpeed();

    private:
        std::string city;
        std::string country;
        std::string description;
        double temperature;
        int humidity;
        double windSpeed;

        nlohmann::json getWeatherData();
        double kelvinToCelcius(double temp);
        
};

#endif 