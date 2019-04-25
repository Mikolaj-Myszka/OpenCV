import cv2


img = cv2.imread('lena.jpg', 1)
cv2.line(img, (0,0), (256,256), (255,0,0), 10)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0,130), font, 1, (255,0,0), 2)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows