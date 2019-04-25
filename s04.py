import cv2


img = cv2.imread('lena.jpg', 1)

img[355,355] = [255,255,255]
img[100:200,100:200] = [255,255,255]


lena_face = img[218:363,197:375]
img[0:145,0:178] = lena_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows

