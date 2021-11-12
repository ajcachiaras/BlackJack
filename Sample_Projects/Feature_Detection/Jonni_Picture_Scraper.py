import cv2
import numpy as np
import os

# cards = cv2.imread("Resources\JonniPics\PotPlayerMini64_1xsep0NjXu.jpg")

# 491, 130

# testImg = cv2.imread('F:\BlackJack\Resources\JonniPics\PotPlayerMini64_1xsep0NjXu.jpg')
# print("original = " + str(testImg.shape))

# imgCropped = testImg[130:1220, 491:2343]
# print("cropped = " + str(imgCropped.shape))
# cv2.imshow("Image", testImg)
# cv2.imshow("ImageCropped", imgCropped)
# cv2.waitKey(0)

directory = r'F:\BlackJack\\Resources\\JonniPics'

i = 0
for file in os.scandir(directory):
    img = cv2.imread(file.path)
    imgCropped = img[130:1220, 491:2343]
    cv2.imwrite("F:\BlackJack\Resources\Jonni_Pics_Cropped\Image" + str(i) + ".png", imgCropped)
    i += 1