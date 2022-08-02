
# Import the library OpenCV
from turtle import shape
import cv2
  
# Import the image
file_name = "savedImage.jpg"
  
# Read the image
src = cv2.imread(file_name,1)
  
# Convert image to image gray
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  
# Applying thresholding technique
_, alpha = cv2.threshold(tmp, 0,255, cv2.THRESH_BINARY)
  
# Using cv2.split() to split channels 
# of coloured image
b, g, r = cv2.split(src)
  
# Making list of Red, Green, Blue
# Channels and alpha
rgba = [b]
print(rgba[0].shape)
# for xx in range(len(rgba)):
    
#     for yy in range(rgba[xx].shape[0]-1):
#         for zz in range(rgba[xx].shape[1]-1):
#             # print(yy,zz)
#             rgba[xx][yy][zz] = 400 - rgba[xx][yy][zz]
#     # yy = 1 - rgba[xx].any()
#     # rgba[xx] =yy
#     print(rgba[xx].shape[0])
# Using cv2.merge() to merge rgba
# into a coloured/multi-channeled image
dst = cv2.merge(rgba, 2)
  
# Writing and saving to a new image
cv2.imwrite("gfg_white.png", dst)