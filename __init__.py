import starter_window,weather,sys

button_hit = False
city = ""
date = ""

button_hit,city, date = starter_window.main()

while (button_hit and (city=="" or date=="")):
        button_hit,city, date = starter_window.main()
        starter_window.BUTTON_HIT = False #Important

if not button_hit: #if button_hit = false then exit normally
    sys.exit(0)


print weather.retMaxTemp(city)
print weather.retMinTemp(city)
print weather.retWeather(city)
