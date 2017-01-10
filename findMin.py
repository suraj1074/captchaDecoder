import os
from PIL import Image

dir = "./templates/"
length = []
width = []

for name in os.listdir(dir):
    tempDir = dir + name
    print tempDir
    for file in os.listdir(tempDir):
        if file.endswith("_final.png"):
            fname = tempDir + "/" + file
            i = Image.open(fname)
            l,w = i.size[0], i.size[1]
            print l,w
    print "\n"

# length.sort()
# width.sort()
# print length[0], width[0]
# print length[-20:],width[-1:]
