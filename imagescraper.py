import urllib
import os

def downloadImage(url):
    myPath = "./cropimages/"
    name = "sample.jpg"
    fullfilename = os.path.join(myPath, name)
    
    urllib.urlretrieve(url,fullfilename)

downloadImage("http://172.16.167.156/sample.jpg")   