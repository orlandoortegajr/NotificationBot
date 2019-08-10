from weather.weatherdata import Weather

w = Weather("Toronto", "Canada")
print(w.get_city())
print(w.get_code())