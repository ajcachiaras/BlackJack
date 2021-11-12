import cv2
import numpy

img = cv2.imread("Sample_Projects\pfp.jpeg")

# imgHor = numpy.hstack((img, img))
# imgVert = numpy.vstack((img, img))

# cv2.imshow("Image Horizontal", imgHor)
# cv2.imshow("Image Vertical", imgVert)


cv2.waitKey(0)