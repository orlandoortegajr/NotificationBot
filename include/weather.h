#include<string>
#pragma once
#ifndef WEATHER_H_
#define WEATHER_H_

class Weather {
    public:
        Weather(std::string userLocation);
        std::string getWeatherData();

    private:
        std::string location;
};

#endif 