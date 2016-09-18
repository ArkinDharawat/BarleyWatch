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

import Tkinter as tk
from PIL import ImageTk, Image
import compare

#This creates the main window of an application
def main():
    window = tk.Tk()
    path = "sample.jpg"
    print compare.compare(path)


    path_file = "/Users/arkin/BarleyWatch/cropimages/sample.jpg"

    window.title(compare.compare(path))
    window.geometry("300x300")
    window.configure(background='grey')

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path_file))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(window, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #Start the GUI
    window.mainloop()
