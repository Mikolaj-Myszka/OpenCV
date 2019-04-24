import cv2


img = cv2.imread('lena.jpg', 0)
#img = cv2.imread('lena.jpg', 1)
#img = cv2.imread('lena.jpg', -1)
print(img)
print(type(img))

cv2.imshow('image', img)
#cv2.waitKey(5000)


k = cv2.waitKey(0) & 0xFF # 0xFF for 64bit machines according to off docs
if k == 27: # Esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy_lena.png', img)
    cv2.destroyAllWindows()

