from PIL import Image
import numpy as np
import cv2
import os

def medianFiltering(fname):
    i = Image.open(fname)
    iar = np.array(i)
    iarl = iar.tolist()

    image_width = len(iar)
    image_height = len(iar[0])

    newList = []

    window_width = 5
    window_height = 5

    edgex = window_width / 2
    edgey = window_height / 2

    for x in xrange(edgex,image_width-edgex):
        temp_x = []
        for y in xrange(edgey,image_height-edgey):
            temp_y = []
            for i in xrange(3):
                window = []
                for fx in xrange(window_width):
                    for fy in xrange(window_height):
                        window.append(iar[x+fx-edgex][y+fy-edgey][i])
                window.sort()
                temp_y.append(window[(window_height * window_width) / 2])

            temp_x.append(temp_y)
        newList.append(temp_x)

    newArray = np.array(newList)
    img = Image.fromarray(newArray, 'RGB')
    name = fname.split(".")[0]+"_1.png"
    img.save(name)
    return name

def thresholdFilter(fname):
    maxValue = 255
    thresh = 235
    src = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)
    name = fname.split(".")[0]+"_2.png"
    cv2.imwrite(name,dst)

z = medianFiltering("2.png")
thresholdFilter(z)
# dir = "."
#
# for file in os.listdir(dir):
#     if file.endswith(".png"):
#         z = medianFiltering(file)
#         thresholdFilter(z)
