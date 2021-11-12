import cv2
import numpy as np

cards = cv2.imread("Resources\Cards.jpg")

green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)
black = (0, 0, 0)
card_dict = {}

# 8 of diamonds
# cv2.circle(cards, (104, 334), 2, green, 1)
# cv2.circle(cards, (191, 332), 2, blue, 1)
# cv2.circle(cards, (69, 433), 2, red, 1)
# cv2.circle(cards, (169, 431), 2, black, 1)
d8_mat = np.float32([[104, 334], [191, 332], [69, 433], [169, 431]])
card_dict["d8"] = d8_mat

# 10 of spades
# cv2.circle(cards, (216, 333), 2, green, 1)
# cv2.circle(cards, (304, 331), 2, blue, 1)
# cv2.circle(cards, (200, 432), 2, red, 1)
# cv2.circle(cards, (299, 431), 2, black, 1)
s10_mat = np.float32([[216, 333], [304, 331], [200, 432], [299, 431]])
card_dict["s10"] = s10_mat

# 9 of hearts
# cv2.circle(cards, (331, 332), 2, green, 1)
# cv2.circle(cards, (419, 329), 2, blue, 1)
# cv2.circle(cards, (332, 432), 2, red, 1)
# cv2.circle(cards, (431, 427), 2, black, 1)
h9_mat = np.float32([[331, 332], [419, 329], [332, 432], [431, 427]])
card_dict["h9"] = h9_mat

# Ace of hearts
# cv2.circle(cards, (441, 331), 2, green, 1)
# cv2.circle(cards, (527, 327), 2, blue, 1)
# cv2.circle(cards, (457, 429), 2, red, 1)
# cv2.circle(cards, (554, 424), 2, black, 1)
ha_mat = np.float32([[441, 331], [527, 327], [457, 429], [554, 424]])
card_dict["ha"] = ha_mat

# Ace of clubs
# cv2.circle(cards, (548, 326), 2, green, 1)
# cv2.circle(cards, (631, 322), 2, blue, 1)
# cv2.circle(cards, (579, 424), 2, red, 1)
# cv2.circle(cards, (675, 417), 2, black, 1)
ca_mat = np.float32([[548, 326], [631, 322], [579, 424], [675, 417]])
card_dict["ca"] = ca_mat

cardWidth, cardHeight = 250, 350
transform_mat = np.float32([[0, 0], [cardWidth, 0], [0, cardHeight], [cardWidth, cardHeight]])

for card in card_dict:
    matrix = cv2.getPerspectiveTransform(card_dict[card], transform_mat)
    outputCard = cv2.warpPerspective(cards, matrix, (cardWidth, cardHeight))
    # cv2.imwrite("Resources\ImagesQuery\\" + card + ".png", outputCard)
    cv2.imshow(card, outputCard)

cv2.imshow("Unwarped", cards)
cv2.waitKey(0)