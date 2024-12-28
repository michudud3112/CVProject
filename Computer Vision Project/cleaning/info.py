import cv2
import numpy as np

def gather_info(image_path):
    img = cv2.imread(image_path)
    res2 = cv2.imread('samples/res2.jpg')
    
    gray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    def get_rectangle_info(contour):
        x, y, w, h = cv2.boundingRect(contour)
        return (y, x, x, y, w, h)
    
    sorted_contours = sorted(contours, key=get_rectangle_info)
    
    with open('samples/wall.txt', 'w') as file:
        
        for contour in sorted_contours[:9]:
            x, y, w, h = cv2.boundingRect(contour)
            
            file.write(f"Rectangle: x={x}, y={y}, width={w}, height={h}\n")