import cv2
import numpy as np
from rectangle import process_image

image = cv2.imread("photos/face1.jpg")
original_image = image.copy()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_gold = np.array([10, 100, 40])
upper_gold = np.array([65, 255, 255])

gold_mask = cv2.inRange(hsv, lower_gold, upper_gold)

kernel = np.ones((5, 5), np.uint8)
gold_mask = cv2.morphologyEx(gold_mask, cv2.MORPH_CLOSE, kernel)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rectangles = []

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4 and cv2.isContourConvex(approx):
        area = cv2.contourArea(approx)
        if area > 500:
            x, y, w, h = cv2.boundingRect(approx)
            rectangles.append((x, y, x + w, y + h))

mask = np.zeros(image.shape[:2], dtype=np.uint8)

for rect in rectangles:
    cv2.rectangle(mask, (rect[0], rect[1]), (rect[2], rect[3]), 255, -1)

result = np.zeros_like(image)
result[mask == 255] = image[mask == 255]

result[gold_mask > 0] = [255, 0, 255]

cv2.imwrite("res.jpg", result)

process_image("res.jpg", "res2.jpg")
