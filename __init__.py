import test_windwo,sys
import display_information_window,imagescraper
import time

button_hit = False
city = ""
date = ""

button_hit,city, date = test_windwo.main()

#print button_hit,city,date

while (button_hit and (city=="" or date=="")):
        button_hit,city, date = test_windwo.main()
        test_windwo.BUTTON_HIT = False #Important

if not button_hit: #if button_hit = false then exit normally
    sys.exit(0)

#display_information_window.weather_plot(city)
imagescraper.downloadImage("http://172.16.167.156/sample.jpg")
display_information_window.main()
