from __future__ import division
from PIL import Image
import numpy as np
import cv2
import os
import math
#  l
########
#      # w
########
def d2(list1,list2):
    list1 = list1.tolist()
    list2 = list2.tolist()
    l, w = min(len(list1),len(list2)) ,min(len(list1[0]),len(list2[0]))
    sum = 0
    sum1 = 0
    sum2 = 0
    for i in xrange(l):
        for j in xrange(w):
            sum += (list1[i][j] * list2[i][j])
            sum1 += list1[i][j] * list1[i][j]
            sum2 += list2[i][j] * list2[i][j]

    sum1 = math.sqrt(sum1)
    sum2 = math.sqrt(sum2)
    if sum1 == 0 or sum2 == 0:
        return 0
    return sum / (sum1 * sum2)
    # return sum

def distance(list1,list2):
    list1 = list1.tolist()
    list2 = list2.tolist()
    l, w = min(len(list1),len(list2)) ,min(len(list1[0]),len(list2[0]))
    sum = 0
    for i in xrange(l):
        for j in xrange(w):
            sum += ((list1[i][j] - list2[i][j]) * (list1[i][j] - list2[i][j]))

    return sum

def removeWhite(iarl,threshold):
    limits = []
    # upper white rows
    l,w = len(iarl),len(iarl[0])
    for i in xrange(l):
        count = 0
        for j in xrange(w):
            if iarl[i][j] == 255:
                count += 1
        if count > threshold:
            limits.append(i)
            break

    #bottom white row
    for i in range(l-1,-1,-1):
        count = 0
        for j in xrange(w):
            if iarl[i][j] == 255:
                count += 1
        if count > threshold:
            limits.append(i)
            break

    # print limits[0], limits[1]
    if len(limits) == 2:
        newList = iarl[limits[0]:limits[1]][:]
        return newList
    elif len(limits) == 1:
        newList = iarl[limits[0]:]
        return newList
    return iarl

def firstNonZero(iarl,threshold,offset):
    w,l = len(iarl),len(iarl[0])

    start = 0
    for c in xrange(offset,l):
        count = 0
        for x in xrange(w):
            if iarl[x][c] != 0:
                count = count+ 1

        if count > threshold:
            start = c
            break

    return start

def Read(fname):
    src = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
    iar = np.array(src)

    threshold = 5
    offset = 0
    start = firstNonZero(iar,threshold,offset)

    dir = "./templates/"

    for i in xrange(5):
        dists = []
        for name in os.listdir(dir):
            label = {"name":name}
            tempDir = dir + name
            # print tempDir
            d = 0
            count = 0
            L = 0
            for file in os.listdir(tempDir):
                if file.endswith("_final.png"):
                    name = tempDir + "/" + file
                    templateImg = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
                    templist = np.array(templateImg)
                    tempW,tempL = len(templist),len(templist[0])

                    t = iar[:,start:start+tempL]
                    L += tempL
                    # print len(t),len(t[0])
                    captchaPart = removeWhite(t,3)
                    if len(captchaPart) == 0:
                        # print "0 here"
                        continue
                    d = d + d2(templist,captchaPart)
                    count += 1

            if count != 0:
                label["l"] = L / count
                dists.append(((d/count),label))

        dists.sort()
        if len(dists) > 0:
            print dists[0][1]["name"],
            offset = start + int(dists[-1][1]["l"])
            start = firstNonZero(iar,threshold,offset)

# file = "./_1_2/183_1_2.png"
# Read(file)
dir = "./_1_2"
for file in sorted(os.listdir(dir)):
    print file,
    Read(dir+"/"+file)
    print "\n",
