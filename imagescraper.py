import urllib
import os

def downloadImage(url):
    myPath = "./cropimages/"
    name = "sample.jpg"
    fullfilename = os.path.join(myPath, name)

    urllib.urlretrieve(url,fullfilename)

   
