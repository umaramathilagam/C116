import cv2

img = cv2.imread("butterfly.jpg")
print(img)
cv2.imshow("Display Colored Image",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Display GRAY Image",gray_img)

print(gray_img)


cv2.waitKey(0)