# /usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

###### Loading image and thresholding
img = cv2.imread('../images/flocs/Image 32373.jpg')
blur = cv2.GaussianBlur(img, (5, 5), 0)
#retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)


#retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t3=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

thresh = t3
######

print(thresh.shape)

##### Closing
kernel = np.ones((5,5),np.uint8)
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

edges = cv2.Canny(closed, 130, 200)
mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)
fld_IMG = closed.copy()


cv2.floodFill(fld_IMG, mask, (960, 100), (255,255,255))
inverted_Flood = cv2.bitwise_not(fld_IMG)
img_Out = (inverted_Flood | closed)
cv2.imshow('closing', t3)
cv2.waitKey(0)
cv2.destroyAllWindows()
