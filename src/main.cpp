#include <iostream>
#include <string>
#include "../include/weather.h"

int main()
{
    Weather weather = Weather("Toronto");
    auto data = weather.getWeatherData();
    std::cout << data << std::endl;
}