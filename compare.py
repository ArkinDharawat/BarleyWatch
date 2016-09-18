import skimage
import os
from skimage import io
from skimage import novice
import math


def closeness(image,w,h):
    Black = (0,0)
    Red = (225,0)
    Green = (0,225)
    Yellow = (225,225)

    Greens = 0
    Yellows = 0

    i=0
    while i<(w):
        j =0
        while j<(h):
            R = image[i,j][0]
            G = image[i,j][1]
            if G >= 112.5 and R < 112.5:
                Greens+=1
            if G >=112.5 and R>=112.5:
                Yellows+=1
            j+=1
        i+=1
#    print Greens,Yellows
    return Greens,Yellows

def values():
    compareFile = os.path.join(skimage.data_dir, "/Users/arkin/BarleyWatch/cropimages/Testcases/Compare.jpg")
    pic = novice.open("/Users/arkin/BarleyWatch/cropimages/Testcases/Compare.jpg")
    stopWaterImage = io.imread(compareFile)[(pic.size[1]/2)-250:(pic.size[1]/2)+250,(pic.size[0]/2)-250:(pic.size[0]/2)+250]

    #print "Stop the Water",
    gC,yC = closeness(stopWaterImage,stopWaterImage.shape[1],stopWaterImage.shape[0])


    #print readGreen(stopWaterImage,stopWaterImage.shape[1],stopWaterImage.shape[0])

    #The file thats perfect
    ripeFile = os.path.join(skimage.data_dir, "/Users/arkin/BarleyWatch/cropimages/Testcases/Ripe.jpg")
    pic = novice.open("/Users/arkin/BarleyWatch/cropimages/Testcases/Ripe.jpg")
    ripeImage = io.imread(ripeFile)[(pic.size[1]/2)-250:(pic.size[1]/2)+250,(pic.size[0]/2)-250:(pic.size[0]/2)+250]

    #print "Ripe Vareity",
    gR,yR = closeness(ripeImage,ripeImage.shape[1],ripeImage.shape[0])


    #print readGreen(ripeImage,ripeImage.shape[1],ripeImage.shape[0])

    #The file that is unripe
    earlyFile = os.path.join(skimage.data_dir, "/Users/arkin/BarleyWatch/cropimages/Testcases/Early.jpg")
    pic = novice.open("/Users/arkin/BarleyWatch/cropimages/Testcases/Early.jpg")
    earlyImage = io.imread(earlyFile)[(pic.size[1]/2)-250:(pic.size[1]/2)+250,(pic.size[0]/2)-250:(pic.size[0]/2)+250]

    #print "Unripe Variey",
    gU,yU = closeness(earlyImage,earlyImage.shape[1],earlyImage.shape[0])

    return gC,yC,gR,yR,gU,yU

def outcome(grVal,yeVal,gC,yC,gR,yR,gU,yU):
    R = float(grVal)/(grVal+yeVal)

    cRatio = float(gC)/(gC+yC)
    rRatio = float (gR)/(gR+yR)
    uRatio = float (gU)/(gU+yU)
    if R == rRatio or (rRatio-R) <= 0.05:
        return "Ripe"
    elif R == cRatio or (cRatio-r)<=0.05:
        return "Stop Irrigation"
    else:
        return "Unripe"

def compare(imgFileName):
    #the file that we want to compare
    gC,yC,gR,yR,gU,yU = values()
    imageFile = os.path.join(skimage.data_dir, "/Users/arkin/BarleyWatch/cropimages/"+imgFileName)
    pic = novice.open("/Users/arkin/BarleyWatch/cropimages/"+imgFileName)
    #print imgFileName
    x = pic.size[1]
    y = pic.size[0]
    fileAsArray = io.imread(imageFile)[(x/2)-250:(x/2)+250,(y/2)-250:(y/2)+250]
    g,ye = closeness(fileAsArray,fileAsArray.shape[1],fileAsArray.shape[0])
    return outcome(g,ye,gC,yC,gR,yR,gU,yU)
