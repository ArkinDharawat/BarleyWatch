import weather
import numpy
import matplotlib.pyplot as plt
import numpy as np
import math


def weather_plot(cityName):
    maxtemps = weather.retMaxTemp(cityName)
    mintemps = weather.retMinTemp(cityName)
    x = 1
    #plt.subplot(211)
    lines = plt.plot(range(0,len(maxtemps)),maxtemps)
    plt.setp(lines, color='r', linewidth=2.0)
    plt.xlabel("Day")
    plt.ylabel("Farenheit")

    #plt.subplot(212)
    lines_1 = plt.plot(range(0,len(mintemps)),mintemps)
    plt.setp(lines_1, color='b', linewidth=2.0)
    plt.xlabel("Day")
    plt.ylabel("Farenheit")

    plt.show()
