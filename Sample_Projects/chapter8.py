import cv2
import numpy


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 300:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor == 5:
                objectType = "Pent"
            elif objCor == 6:
                objectType = "Hex"
            elif objCor == 8:
                objectType = "Oct"
            else:
                objectType = "Circle"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(imgContour, objectType, (x + (w//2), y + (h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

img = cv2.imread("Resources\Shapes.jpg")
print(img.shape)


imgCropped = img[150:700, 35:1230]
imgContour = imgCropped.copy()
imgGray = cv2.cvtColor(imgCropped, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 3)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Contour", imgContour)
cv2.waitKey(0)