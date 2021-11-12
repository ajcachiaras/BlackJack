import cv2
import numpy

filename = "Resources\Cards.jpg"

numcards = 5

img = cv2.imread(filename)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (1,1), 2000)
flag, thresh = cv2.threshold(imgBlur, 175, 255, cv2.THRESH_BINARY)
# imgCanny = cv2.Canny(imgBlur, 250, 250)

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:numcards]

# contours, heirarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 5000:
        cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 2)
    # peri = cv2.arcLength(cnt, True)
    # approx = cv2.approxPolyDP(cnt, 0.01*peri, True)
    # pts = numpy.float32(approx)

    # x, y, w, h = cv2.boundingRect(cnt)

    # average = numpy.sum(pts, axis=0)/len(pts)
    # cent_x = int(average[0][0])
    # cent_y = int(average[0][1])

    # cardFlat = 



cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image thresh", thresh)
# cv2.imshow("Image Canny", imgCanny)
cv2.imshow("image contour", imgContour)
cv2.waitKey(0)