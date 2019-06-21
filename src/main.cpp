#include <iostream>
#include "../include/weather.h"
#include "../include/export.h"

using namespace std;
int main()
{

    std::string city = "Oakville";
    Weather weather = Weather(city);
    Export file = Export("output");
    std::string fileFormat[] = {
        "Weather in " + weather.getLocation(),
        "Conditions: " + weather.getDescription(),
        "Temperature: " + std::to_string(weather.getTemperature()) + "C",
        "Humidity: " + std::to_string(weather.getHumidity()) + "%",
        "Wind Speed: " + std::to_string(weather.getWindSpeed()) + "miles/h"
    };

    size_t length = 5;

    file.writeToFile(fileFormat, length);
    
}