import cv2
import numpy

img = cv2.imread("F:\BlackJack\Sample_Projects\pfp.jpeg")
kernel = numpy.ones((5, 5), numpy.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgCanny = cv2.Canny(img, 100, 100)
# Dilate = make edges thicker
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode = make edges thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)