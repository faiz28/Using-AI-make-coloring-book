import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
# import cv2
# import numpy as np

# load the image
image = skimage.io.imread("iamge4.jpg")


# fig, ax = plt.subplots()
# plt.imshow(image)
# plt.show()


print(len(image.shape))
gray_image = image
for x in range(0, len(image.shape)):
    for y in range(0, (image.shape[0])):
        gray_image[x][y] = image[x][y]/255
        print(gray_image[x][y])
        
fig, ax = plt.subplots()
plt.imshow(gray_image)
plt.show()


# if len(image.shape) == 2:    
#     for x in range(0, len(image.shape)):
#         for y in range(0, (image.shape[0])):
#             print(image[x][y])
#     gray_image = skimage.color.gray2rgb(image)
# # convert the image to grayscale
# gray_image = skimage.color.rgb2gray(image)

# gray_image = image
# zero  = 0
# one=0
# other =0
# for x in range(len(gray_image)):
#     for y in range(len(gray_image[0])):
#         # if gray_image[x][y] == 0:
#         #     zero+=1
#         # elif gray_image[x][y] == 1:
#         #     one+=1
#         # else:
#         #     other+=1
#         if gray_image[x][y] >=0.5:
        
#             gray_image[x][y] = 1
#         else:
#             gray_image[x][y] = 0
            


# print(gray_image.shape)

# gray_image = skimage.color.gray2rgb(gray_image)
# fig, ax = plt.subplots()
# plt.imshow(gray_image)
# plt.show()

# print(zero)
# print(one)
# print(other)