import cv2
import numpy as np

def process_image(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = []

    for contour in contours:
        epsilon = 0.025 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4 and cv2.isContourConvex(approx):
            area = cv2.contourArea(approx)
            if area > 500:
                x, y, w, h = cv2.boundingRect(approx)
                rectangles.append((x, y, x + w, y + h))

    if rectangles:
        mask = np.zeros(image.shape[:2], dtype=np.uint8)

        for rect in rectangles:
            cv2.rectangle(mask, (rect[0], rect[1]), (rect[2], rect[3]), 255, -1)

        result = np.zeros_like(image)
        result[mask == 255] = image[mask == 255]

        for rect in rectangles:
            cv2.rectangle(result, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
            
        cv2.imwrite(output_image_path, result)

process_image("samples/res.jpg", "samples/res2.jpg")