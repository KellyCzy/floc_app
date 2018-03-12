# In this snippet we attempt to replicate the methods in:
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4752185/
# We want to try and perform noise reduction on the floc images to separate the
# foreground from the back ground, we also need to see how to properly deal
# with different flocs that are in and out of focus.
#
# Current Implementation:
# *We first start to test how the gaussian filter affects the floc images
# *We are applying inverse thresholding to the images and are currently testing
#     what values produce the best result


import cv2
import numpy as np
from matplotlib import pyplot as plt

# The image processing of image 32891:

# Import of image
img_32891_orig = cv2.imread('../images/flocs/Image 32891.jpg')

plt.figure()
plt.subplot(221), plt.imshow(img_32891_orig), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Application of the Gaussian Filter
img_32891_blur = cv2.GaussianBlur(img_32891_orig, (5, 5), 0)

plt.subplot(222), plt.imshow(img_32891_blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

# Binary Inverse Thresholding after filter
retval, img_32891_threshold = cv2.threshold(img_32891_blur, 130, 255, cv2.THRESH_BINARY_INV)
plt.subplot(223), plt.imshow(img_32891_threshold), plt.title('Threshold')
plt.xticks([]), plt.yticks([])


# Morphological Transformations
# closing: closing small holes inside the object
kernel = np.ones((5,5),np.uint8)
img_32891_closing = cv2.morphologyEx(img_32891_threshold, cv2.MORPH_CLOSE, kernel)

plt.subplot(224), plt.imshow(img_32891_closing), plt.title('closing')
plt.xticks([]), plt.yticks([])
#plt.show()

#if using denosing instead of Gaussian filter in the first step:
img_32891_den = cv2.fastNlMeansDenoisingColored(img_32891_orig,None,10,10,7,21)

plt.figure()
plt.subplot(131), plt.imshow(img_32891_orig), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_32891_blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_32891_den), plt.title('Denoised')
plt.xticks([]), plt.yticks([])
#plt.show()

# We cannot see too too much difference between Gaussian filter and normal denoising.
# So we continue to use Gaussian filter mentioned in the article.


# sobel filter: remove out of focus particles
# horizontal and vertical sobel filter
img_32891_sobelx = cv2.Sobel(img_32891_blur, cv2.CV_64F,1,0,ksize=5)
img_32891_sobely = cv2.Sobel(img_32891_blur, cv2.CV_64F,0,1,ksize=5)

'''plt.figure()
plt.subplot(131), plt.imshow(img_32891_sobelx,cmap = 'gray'), plt.title('sobelx')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_32891_sobely,cmap = 'gray'), plt.title('sobely')
plt.xticks([]), plt.yticks([])
plt.show()'''

# The next step should be the removal of particles that touched the border
print(img_32891_closing.shape)

print(img_32891_closing[0,1279])
print(img_32891_closing[0,0])

# Set the color array
white = np.array([255,255,255])
black = np.array([0,0,0])

# get the shape of the picture
rows,cols,channels=img_32891_closing.shape

# Get all the pixels in the picture
px=img_32891_closing[0:rows,0:cols]










'''cv2.imshow('closing',img_32891_closing)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''cv2.imshow('closing',img_32891_sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('closing',img_32891_sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()'''