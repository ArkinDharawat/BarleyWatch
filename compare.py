import skimage
import os
from skimage import io

def compare(filePath):
    #the file that we want to compare
    compareFile = os.path.join(skimage.data_dir, filePath)
    image = io.imread(compareFile)[0:500, 0:500]
    #The file thats perfect
    ripeFile = os.path.join(skimage.data_dir, "/Users/adityabhargava/Documents/BarleyWatch/ripe.jpg")
    ripeImage = io.imread(ripeFile)[0:500, 0:500]
    #The file that is unripe
    #earlyFile = os.path.join(skimage.data_dir, "")
    #earlyImage = io.imread(earlyFile)[0:500, 0:500]
    #The file is over ripe
    #lateFile = os.path.join(skimage.data_dir, "")
    #lateImage = io.imread(lateFile)[0:500, 0:500]
    while i<500:
    	j =0
    	while j<500:
    		image[i,j] - ripeImage[i,j]
    


compare("/Users/adityabhargava/Documents/BarleyWatch/early.jpg")