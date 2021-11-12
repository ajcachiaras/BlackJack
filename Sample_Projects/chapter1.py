import cv2
print("Package Imported")

# use an image
# 
img = cv2.imread("F:\BlackJack\Sample_Projects\pfp.jpeg")
print("Success")
cv2.imshow("Output",img)
cv2.waitKey(0)

# use a video
#
# cap = cv2.VideoCapture("TestVideo.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


# use a webcam (i dont care to make it work)
#
# cap = cv2.VideoCapture(1)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break