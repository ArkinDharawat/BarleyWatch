import urllib2
from json import JSONDecoder, dumps

def retMaxTemp(cityName):
    maxtemp = []
    appid = '8b0535876a983c207e0513f391973931'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode=json&units=metric&cnt=16&appid={}'.format(cityName, appid)
    response = urllib2.urlopen(url)
    weather_html = response.read()
    decoder = JSONDecoder()
    weather_data = decoder.decode(weather_html)
    pretty_weather_data = dumps(weather_data, indent=2, separators=(',', ': '))
    #print pretty_weather_data

    for i in weather_data['list']:
        maxtemp.append(i['temp']['max']+32)

    return maxtemp

def retMinTemp(cityName):
    mintemp = []
    appid = '8b0535876a983c207e0513f391973931'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode=json&units=metric&cnt=16&appid={}'.format(cityName, appid)
    response = urllib2.urlopen(url)
    weather_html = response.read()
    decoder = JSONDecoder()
    weather_data = decoder.decode(weather_html)
    pretty_weather_data = dumps(weather_data, indent=2, separators = (',', ': '))
    #print pretty_weather_data

    for i in weather_data['list']:
        mintemp.append(i['temp']['min']+32)

    return mintemp


def retWeather(cityName):
    weather = []
    appid = '8b0535876a983c207e0513f391973931'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode=json&units=metric&cnt=16&appid={}'.format(cityName, appid)
    response = urllib2.urlopen(url)
    weather_html = response.read()
    decoder = JSONDecoder()
    weather_data = decoder.decode(weather_html)
    pretty_weather_data = dumps(weather_data, indent=2, separators=(',', ': '))
    #print pretty_weather_data

    for i in weather_data['list']:
        weather.append(i['weather'][0]['main'])
        print weather

    return mintemp

def retWeather(cityName):
    weather = []
    appid = '8b0535876a983c207e0513f391973931'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&mode=json&units=metric&cnt=16&appid={}'.format(cityName, appid)
    response = urllib2.urlopen(url)
    weather_html = response.read()
    decoder = JSONDecoder()
    weather_data = decoder.decode(weather_html)
    pretty_weather_data = dumps(weather_data, indent=2, separators=(',', ': '))
    #print pretty_weather_data

    for i in weather_data['list']:
        weather.append(i['weather'][0]['description'])
    return weather
