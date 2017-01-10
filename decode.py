from PIL import Image
import numpy as np
import os

def decode(fname):
    i = Image.open(fname)
    iar = np.array(i)
    iarl = iar.tolist()

    image_width = len(iar)
    image_height = len(iar[0])

    character_width = 30
    start = 0
    for c in xrange(image_height):
        empty = True
        count = 0;
        for x in xrange(image_width):
            if iarl[x][c] != 0:
                count = count+ 1
                if count > 5:
                    print x,c
                    empty = False
                    break
        if not empty:
            start = c
            break

    characters = 5
    for c in xrange(characters):
        newList  = []
        for x in xrange(image_width):
            newList.append(iarl[x][start:start+character_width])

        for x in xrange(len(newList)):
            for y in xrange(len(newList[0])):
                print str(newList[x][y]) + "\t",
            print "\n" ,

        print "\n"
        newArray = np.array(newList)
        img = Image.fromarray(newArray,"1")
        name = fname.split(".")[0]+"_decoded_"+str(c)+".png"
        img.save(name)
        start = start + character_width

decode("0_1_2.png")
# dir = "."
# for file in os.listdir(dir):
#     if file.endswith("_1_2.png"):
#         decode(file)
