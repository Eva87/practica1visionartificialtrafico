import cv2
import numpy as np

np.set_printoptions(suppress=True)
img = cv2.imread("./test/00575.jpg")
img = cv2.imread("./test/00411.jpg")
img = cv2.imread("./test/00420.jpg")
img = cv2.imread("./test/00403.jpg")
img = cv2.imread("./test/00482.jpg")
print('img:', type(img), img.shape, img.dtype)
cv2.imshow('img', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

'''
blue_lower = np.array([0,0,50], np.uint8)
blue_upper = np.array([10,255,255], np.uint8)
blue_lower2 = np.array([150,0,50], np.uint8)
blue_upper2 = np.array([200,255,255], np.uint8)
'''
rojo_bajo = np.array([0, 0, 50])
blue_upper = np.array([10, 255, 255])
rojo_bajo2 = np.array([150, 0, 50])
blue_upper2 = np.array([200, 255, 255])


blue_lower=np.array([100,50,50])
blue_upper=np.array([124,255,255])

blue_lower=np.array([19,62,164])
blue_upper=np.array([42,255,245])

mask = cv2.inRange(hsv, blue_lower, blue_upper)
'''
mask1 = cv2.inRange(hsv, blue_lower, blue_upper)
mask2 = cv2.inRange(hsv, blue_lower2, blue_upper2)
mask = cv2.add( mask1,mask2)

'''


print('mask', type(mask), mask.shape)
cv2.imshow('mask', mask)
blurred = cv2.blur(mask, (9, 9))
cv2.imshow('blurred', blurred)
ret, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('blurred binary', binary)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed', closed)
erode = cv2.erode(closed, None, iterations=4)
cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=4)
cv2.imshow('dilate', dilate)
contours, hierarchy = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('number', len(contours))
i = 0
res = img.copy()
for con in contours:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))

    cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
    print([box])
h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
print('h1', h1)
print('h2', h2)
print('l1', l1)
print('l2', l2)
if h1 - h2 > 0 and l1 - l2 > 0:
    temp = img[h2:h1, l2:l1]
    i = i + 1
    cv2.imshow('sign' + str(i), temp)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()