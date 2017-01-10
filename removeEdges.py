import os
from PIL import Image
import numpy as np
import cv2

threshold = 3

def remove(fname):
    src = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
    iarl = np.array(src).tolist()
    l,w = len(iarl),len(iarl[0])
    print l,w

    point1 = []
    point2 = []

    # upper white rows
    for i in xrange(l):
        count = 0
        for j in xrange(w):
            if iarl[i][j] == 255:
                count += 1
        if count > threshold:
            point1.append(i)
            break

    # left white column
    for i in xrange(w):
        count = 0
        for j in xrange(l):
            if iarl[j][i] == 255:
                count += 1
        if count > threshold:
            point1.append(i)
            break

    #bottom white row
    for i in range(l-1,-1,-1):
        count = 0
        for j in xrange(w):
            if iarl[i][j] == 255:
                count += 1
        if count > threshold:
            point2.append(i)
            break

    # right white column
    for i in range(w-1,-1,-1):
        count = 0
        for j in xrange(l):
            if iarl[j][i] == 255:
                count += 1
        if count > threshold:
            point2.append(i)
            break

    newList = []
    for i in xrange(point1[0],point2[0]):
        temp = []
        for j in xrange(point1[1],point2[1]):
            temp.append(iarl[i][j])
        newList.append(temp)

    print len(newList), len(newList[0])
    newArray = np.array(newList)
    name = fname.split(".png")[0]+"_final.png"
    print name
    cv2.imwrite(name,newArray)


# remove("./templates/2/2_2.png")
# dir = "./templates/"
#
# for name in os.listdir(dir):
#     tempDir = dir + name
#     print tempDir
#     for file in os.listdir(tempDir):
#         fname = tempDir + "/" + file
#         remove(fname)
