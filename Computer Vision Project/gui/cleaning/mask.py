import cv2
import numpy as np
from rectangle import process_image
from info import gather_info
from sort import process_coordinates
import re

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.original_image = self.image.copy()
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.mask = None
        self.rectangles = []

    def create_gold_mask(self, lower_gold, upper_gold):
        gold_mask = cv2.inRange(self.hsv, lower_gold, upper_gold)
        kernel = np.ones((5, 5), np.uint8)
        self.mask = cv2.morphologyEx(gold_mask, cv2.MORPH_CLOSE, kernel)

    def detect_rectangles(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) == 4 and cv2.isContourConvex(approx):
                area = cv2.contourArea(approx)
                if area > 500:
                    x, y, w, h = cv2.boundingRect(approx)
                    self.rectangles.append((x, y, x + w, y + h))

    def apply_masks_and_save(self, output_path):
        mask = np.zeros(self.image.shape[:2], dtype=np.uint8)

        for rect in self.rectangles:
            cv2.rectangle(mask, (rect[0], rect[1]), (rect[2], rect[3]), 255, -1)

        result = np.zeros_like(self.image)
        result[mask == 255] = self.image[mask == 255]
        result[self.mask > 0] = [255, 0, 255]

        cv2.imwrite(output_path, result)

    def process_additional_steps(self, intermediate_path, final_path, wall_text, sorted_wall_text):
        process_image(intermediate_path, final_path)
        gather_info(final_path)
        process_coordinates(wall_text, final_path, "samples/res3.jpg", sorted_wall_text)
        
        try:
            with open(sorted_wall_text, 'r') as file:
                lines = file.readlines()
                is_correct = len(lines) == 9
                coordinates = []
                for line in lines:
                    points = re.findall(r'x=(\d+),\s*y=(\d+)', line)
                    coords = [(int(x), int(y)) for x, y in points]
                    coordinates.append(coords)
            
        except FileNotFoundError:
            is_correct = False
            coordinates = []
        
        return is_correct, coordinates

if __name__ == "__main__":
    processor = ImageProcessor("photos/face1.jpg")
    
    lower_gold = np.array([10, 100, 40])
    upper_gold = np.array([65, 255, 255])

    processor.create_gold_mask(lower_gold, upper_gold)
    processor.detect_rectangles()
    processor.apply_masks_and_save("samples/res.jpg")
    
    result = processor.process_additional_steps("samples/res.jpg", "samples/res2.jpg", "samples/wall.txt", "wall_sorted.txt")
    
    print(f"Result Tuple: {result}")
