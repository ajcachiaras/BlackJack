import cv2
import numpy

img = cv2.imread("Resources\Cards.jpg")
# print(img.shape)
# its 512 x 768

cv2.circle(img, (105, 332), 3, (0, 255, 0), 2)
cv2.circle(img, (191, 331), 3, (0, 255, 0), 2)
cv2.circle(img, (68, 433), 3, (0, 255, 0), 2)
# cv2.circle(img, (168, 433), 3, (0, 255, 0), 2)

width, height = 250, 350
pts1 = numpy.float32([[105, 334], [191, 331], [68, 433], [168, 433]])
pts2 = numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# width, height = 250, 350
# pts1 = numpy.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image Warped", imgOutput)
cv2.waitKey(0)