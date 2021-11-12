import cv2
import numpy

img = numpy.zeros((512, 512, 3), numpy.uint8)
# print(img.shape)
# img[:] = 255, 0, 0
# img[200:300, 100:300] = 100, 0, 100

cv2.line(img, (0, 0), (img.shape[1], 300), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (140, 14, 100), cv2.FILLED)
cv2.circle(img, (400,50), 30, (255, 200, 0), 5)
cv2.putText(img, " OPENCV ", (200, 400), cv2.FONT_HERSHEY_PLAIN, 3, (0, 150, 0), 2)

cv2.imshow("Image", img)


cv2.waitKey(0)