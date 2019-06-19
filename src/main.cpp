#include <iostream>
#include "../include/weather.h"

using namespace std;
int main()
{

    Weather userWeather = Weather("Toronto");
    cout << userWeather.getLocation() << endl;
    cout << userWeather.getDescription() << endl;
    cout << userWeather.getHumidity() << endl;
    cout << userWeather.getTemperature() << endl;
    cout << userWeather.getWindSpeed() << endl;
    
}