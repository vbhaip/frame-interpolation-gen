import cv2

margin = 125

img = cv2.imread('testimg.png')[margin:-1*margin, margin:-1*margin]

cv2.imshow("image", img)
cv2.waitKey(0)