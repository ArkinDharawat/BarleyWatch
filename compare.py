import skimage
import os
from skimage import io
import math

def compare(filePath):
    #the file that we want to compare
    compareFile = os.path.join(skimage.data_dir, filePath)
    image = io.imread(compareFile)[0:500, 0:500]
    #The file thats perfect
    ripeFile = os.path.join(skimage.data_dir, "/Users/adityabhargava/Documents/BarleyWatch/ripe.jpg")
    ripeImage = io.imread(ripeFile)[0:500, 0:500]
    #The file that is unripe
    earlyFile = os.path.join(skimage.data_dir, "/Users/adityabhargava/Documents/BarleyWatch/early.jpg")
    earlyImage = io.imread(earlyFile)[0:500, 0:500]
    #The file is over ripe
    #lateFile = os.path.join(skimage.data_dir, "")
    #lateImage = io.imread(lateFile)[0:500, 0:500]
    diff = (0,0,0)
    i = 0
    while i<500:
    	j =0
    	while j<500:
    		diff += abs(image[i,j] - ripeImage[i,j])
    		j= j+1
    	i=i+1	

    r1 = diff[0]/(500*500)
    g1 = diff[1]/(500*500)
    b1 = diff[2]/(500*500)
    d1 = math.sqrt(r1*r1 + g1*g1 + b1*b1)
    print r1
    print g1
    print b1

    diff = (0,0,0)
    i = 0
    while i<500:
    	j =0
    	while j<500:
    		diff += abs(image[i,j] - earlyImage[i,j])
    		j= j+1
    	i=i+1	

    r2 = diff[0]/(500*500)
    g2 = diff[1]/(500*500)
    b2 = diff[2]/(500*500)
    d2 = math.sqrt(r2*r2 + g2*g2 + b2*b2)
    print r2
    print g2
    print b2


    if(d1<d2):
    	print "close to ripe"
    elif(d1>d2):
    	print "close to early"
    else:
    	print "the fuck they the same"

    print d1
    print d2	

compare("/Users/adityabhargava/Documents/Github/BarleyWatch/sample.jpg")