#!/bin/env python3

from PIL import Image, ImageDraw
import numpy as np
import skimage.morphology

# Open the shirt and make a clean copy before we dink with it too much
im = Image.open('shirt.jpg')
orig = im.copy()

# Make all background pixels (not including Nike logo) into magenta (255,0,255)
ImageDraw.floodfill(im,xy=(0,0),value=(255,0,255),thresh=50)

# DEBUG
im.show()

# Make into Numpy array
n = np.array(im)

# Mask of magenta background pixels
bgMask =(n[:, :, 0:3] == [255,0,255]).all(2)

# DEBUG
Image.fromarray((bgMask*255).astype(np.uint8)).show()

# Make a disk-shaped structuring element
strel = skimage.morphology.disk(13)

# Perform a morphological closing with structuring element to remove blobs
newalpha = skimage.morphology.binary_closing(bgMask,selem=strel)

# Perform a morphological dilation to expand mask right to edges of shirt
newalpha = skimage.morphology.binary_dilation(newalpha, selem=strel)

# Make a PIL representation of newalpha, converting from True/False to 0/255
newalphaPIL = (newalpha*255).astype(np.uint8)
newalphaPIL = Image.fromarray(255-newalphaPIL, mode='L')

# DEBUG
newalphaPIL.show()

# Put new, cleaned up image into alpha layer of original image
orig.putalpha(newalphaPIL)
orig.save('result.png')










# from PIL import Image, ImageDraw
# import numpy as np
# import skimage.morphology

# # Open the shirt
# im = Image.open('savedImage.jpg')
# im = Image.new("RGBA", im.size)
# # Make all background pixels (not including Nike logo) into magenta (255,0,255)
# ImageDraw.floodfill(im,xy=(0,0),value=(255,0,255),thresh=10)

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

# # Perform a morphological closing with structuring element
# closed = skimage.morphology.binary_closing(bgMask,selem=strel)

# # DEBUG
# Image.fromarray((closed*255).astype(np.uint8)).show()

# #!/bin/env python3

# from PIL import Image, ImageDraw
# import numpy as np
# import skimage.morphology

# # Open the shirt and make a clean copy before we dink with it too much
# im = Image.open('savedImage.jpg')
# im = Image.new("RGBA", im.size)
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
# # newalphaPIL.save('newalpha.pgm')