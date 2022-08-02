
# Python code to read image
import cv2 as cv
from matplotlib import image
import numpy as np
from matplotlib import pyplot as plt
 
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv.imread("12.jpg", 0)
# img = cv.medianBlur(img,5)
print(img.shape)


ret,th1 = cv.threshold(img,150,250,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
# plt.show()

# th1 = cv.medianBlur(th1,9)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (2,3))
close = cv.morphologyEx(th1, cv.MORPH_CLOSE, kernel, iterations=2)
result = 255 - close

# cv.imshow('thresh', th1)

# cv.imshow('close', close)
# cv.imshow('result', result)
# cv.imwrite('result.png', result)
# cv.waitKey()
filename = 'savedImage.jpg'
cv.imwrite(filename, th1)



# gaussian_blur = cv.GaussianBlur(src=th1, ksize=(3,3), sigmaX=1, sigmaY=0)
median = cv.medianBlur(src=th1, ksize=5)

# kernel2 = np.ones((5, 5), np.float32) / 19

img = cv.filter2D(src=th1, ddepth=-1, kernel=kernel)

blur = cv.GaussianBlur( th1, (5,5), 0)
# smooth = cv.addWeighted( blur, 1.5, img, -0.5, 0)

cv.imshow('Original', th1)

cv.imshow('Kernel Blur', blur)

cv.waitKey()




# import matplotlib.pyplot as plt
# # import keras_ocr

# pipeline = keras_ocr.pipeline.Pipeline()
# #read image from the an image path (a jpg/png file or an image url)
# img = keras_ocr.tools.read(th1)

# # Prediction_groups is a list of (word, box) tuples
# prediction_groups = pipeline.recognize([img])
# #print image with annotation and boxes
# keras_ocr.tools.drawAnnotations(image=img, predictions=prediction_groups[0])

# import math
# import numpy as np
# def midpoint(x1, y1, x2, y2):
#     x_mid = int((x1 + x2)/2)
#     y_mid = int((y1 + y2)/2)
#     return (x_mid, y_mid)
# #example of a line mask for the word "Tuesday"
# box = prediction_groups[0][10]
# x0, y0 = box[1][0]
# x1, y1 = box[1][1] 
# x2, y2 = box[1][2]
# x3, y3 = box[1][3] 
        
# x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
# x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
# thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))

# mask = np.zeros(img.shape[:2], dtype="uint8")
# cv.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)

# masked = cv.bitwise_and(img, img, mask=mask)
# plt.imshow(masked)

# img_inpainted = cv.inpaint(img, mask, 7, cv.INPAINT_NS)
# plt.imshow(img_inpainted)






# import matplotlib.pyplot as plt
# import keras_ocr
# import cv2
# import math
# import numpy as np
# def midpoint(x1, y1, x2, y2):
#     x_mid = int((x1 + x2)/2)
#     y_mid = int((y1 + y2)/2)
#     return (x_mid, y_mid)
# pipeline = keras_ocr.pipeline.Pipeline()
# def inpaint_text(img_path, pipeline):
#     # read image
#     img = keras_ocr.tools.read(img_path)
#     # generate (word, box) tuples 
#     prediction_groups = pipeline.recognize([img])
#     mask = np.zeros(img.shape[:2], dtype="uint8")
#     for box in prediction_groups[0]:
#         x0, y0 = box[1][0]
#         x1, y1 = box[1][1] 
#         x2, y2 = box[1][2]
#         x3, y3 = box[1][3] 
        
#         x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
#         x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
        
#         thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
        
#         cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255,    
#         thickness)
#         img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
                 
#     return(img)
