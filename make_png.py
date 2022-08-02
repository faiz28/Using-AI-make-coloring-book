
# Python code to read image
import cv2 as cv
from matplotlib import image
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
# To read image from disk, we use
# cv2.imread function, in below method,
import os

# path = "F:\Faiz important project\practice\input\\"
dir_path = 'F:\\Faiz important project\\practice\\input\\'
save_dir = 'F:\\Faiz important project\\practice\\output\\'
png = 'F:\\Faiz important project\\practice\\png\\'

cnt=0
for path in os.listdir(save_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(save_dir, path)):
        img = os.path.join(save_dir, path)
        img = Image.open(img)
        img = img.convert("RGBA")
        datas = img.getdata()
        print(cnt)
        cnt+=1
        newData = []
        for item in datas:
            if item[0] >= 200 and item[1] >= 200 and item[2] >=200 :
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        filename = png+path
        img.save(filename, "PNG")
