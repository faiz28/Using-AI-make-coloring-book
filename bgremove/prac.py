import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters

# load the image
image = skimage.io.imread("image.jpg")

fig, ax = plt.subplots()
plt.imshow(image)
plt.show()

# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)

# blur the image to denoise
blurred_image = skimage.filters.gaussian(gray_image, sigma=0.5)

fig, ax = plt.subplots()
plt.imshow(blurred_image, cmap="gray")
plt.show()

# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()

t = 0.8
binary_mask = blurred_image < t

fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
plt.show()


# # use the binary_mask to select the "interesting" part of the image
# selection = image.copy()
# selection[~binary_mask] = 0

# fig, ax = plt.subplots()
# plt.imshow(selection)
# plt.show()

# from PIL import Image, ImageDraw
# import numpy as np
# import skimage.morphology

# # Open the shirt and make a clean copy before we dink with it too much
# im = Image.open('image.jpg')
# orig = im.copy()

# # Make all background pixels (not including Nike logo) into magenta (255,0,255)
# ImageDraw.floodfill(im,xy=(0,0),value=(255,0,255),thresh=50)

# # DEBUG
# im.show()

# # Make into Numpy array
# n = np.array(im)

# # Mask of magenta background pixels
# bgMask =(n[:, :, 0:3] == [255,0,255]).all(2)

# # DEBUG
# Image.fromarray((bgMask*255).astype(np.uint8)).show()

# # Make a disk-shaped structuring element
# strel = skimage.morphology.disk(13)

# # Perform a morphological closing with structuring element to remove blobs
# newalpha = skimage.morphology.binary_closing(bgMask,selem=strel)

# # Perform a morphological dilation to expand mask right to edges of shirt
# newalpha = skimage.morphology.binary_dilation(newalpha, selem=strel)

# # Make a PIL representation of newalpha, converting from True/False to 0/255
# newalphaPIL = (newalpha*255).astype(np.uint8)
# newalphaPIL = Image.fromarray(255-newalphaPIL, mode='L')

# # DEBUG
# newalphaPIL.show()

# # Put new, cleaned up image into alpha layer of original image
# orig.putalpha(newalphaPIL)
# orig.save('result.png')


    # DataFlair background removal
# import necessary packages
# import os
# import cv2
# import numpy as np
# import mediapipe as mp
# # store background images in a list
# image_path = '.'
# images = os.listdir(image_path)
# image_index= 0
# bg_image = cv2.imread(image_path+'/'+images[image_index])

# # initialize mediapipe
# mp_selfie_segmentation = mp.solutions.selfie_segmentation
# selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# # create videocapture object to access the webcam
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#   _, frame = cap.read()
#   # flip the frame to horizontal direction
#   frame = cv2.flip(frame, 1)
#   height , width, channel = frame.shape
  
#   RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#   # get the result
#   results = selfie_segmentation.process(RGB)
#   # extract segmented mask
#   mask = results.segmentation_mask
#   # show outputs
#   cv2.imshow("mask", mask)
#   cv2.imshow("Frame", frame)
#   key = cv2.waitKey(1)
#   if key == ord('q'):
#         break