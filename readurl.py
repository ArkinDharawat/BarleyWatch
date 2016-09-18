import urllib2,requests

from PIL import Image
import urllib, cStringIO


URL = "http://172.16.167.156/sample.jpg
file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = Image.open(file)
