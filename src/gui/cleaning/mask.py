import os
import cv2
import numpy as np
from .rectangle import process_image
from .sort import process_coordinates
import re

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.original_image = self.image.copy()
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.mask = None
        self.rectangles = []
        self.save_dir = os.path.join(os.path.dirname(__file__), "samples")

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
        if self.mask is None:
            print("Mask has not been created.")

        if not self.rectangles:
            print("No rectangles detected.")
            return False

        mask = np.zeros(self.image.shape[:2], dtype=np.uint8)

        for rect in self.rectangles:
            cv2.rectangle(mask, (rect[0], rect[1]), (rect[2], rect[3]), 255, -1)

        result = np.zeros_like(self.image)
        result[mask == 255] = self.image[mask == 255]
        result[self.mask > 0] = [255, 0, 255]

        if cv2.imwrite(output_path, result):
            print(f"Image saved successfully at {output_path}")
        else:
            print(f"Failed to save image at {output_path}")
        return True

    def gather_info(self,image_path):
        img = cv2.imread(image_path)
        save_dir = os.path.join(os.path.dirname(__file__), "samples")
        res2 = cv2.imread(os.path.join(save_dir, "res2.jpg"))

        gray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        def get_rectangle_info(contour):
            x, y, w, h = cv2.boundingRect(contour)
            return (y, x, x, y, w, h)

        sorted_contours = sorted(contours, key=get_rectangle_info)

        with open(os.path.join(save_dir, "wall.txt"), 'w') as file:
            for contour in sorted_contours[:9]:
                x, y, w, h = cv2.boundingRect(contour)

                file.write(f"Rectangle: x={x}, y={y}, width={w}, height={h}\n")

    def process_additional_steps(self, intermediate_path, final_path, wall_text, sorted_wall_text):
        image = cv2.imread(intermediate_path)
        if image is None:
            raise FileNotFoundError(f"Image at path {intermediate_path} could not be loaded.")

        process_image(intermediate_path, final_path)
        self.gather_info(final_path)
        process_coordinates(wall_text, final_path, os.path.join(self.save_dir, "res3.jpg"), sorted_wall_text)
        
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

    def process(self):

        lower_gold = np.array([10, 100, 40])
        upper_gold = np.array([65, 255, 255])

        self.create_gold_mask(lower_gold, upper_gold)
        self.detect_rectangles()

        if not self.apply_masks_and_save(os.path.join(self.save_dir, "res.jpg")): #Something failed. Exit.
            return False, None
        
        result = self.process_additional_steps(os.path.join(self.save_dir, "res.jpg"),
                                               os.path.join(self.save_dir, "res2.jpg"),
                                               os.path.join(self.save_dir, "wall.txt"),
                                               os.path.join(self.save_dir, "wall_sorted.txt"))
        return result


    def gather_info(self,image_path):
        img = cv2.imread(image_path)
        save_dir = os.path.join(os.path.dirname(__file__), "samples")
        res2 = cv2.imread(os.path.join(save_dir, "res2.jpg"))

        gray = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        def get_rectangle_info(contour):
            x, y, w, h = cv2.boundingRect(contour)
            return (y, x, x, y, w, h)

        sorted_contours = sorted(contours, key=get_rectangle_info)

        with open(os.path.join(save_dir, "wall.txt"), 'w') as file:
            for contour in sorted_contours[:9]:
                x, y, w, h = cv2.boundingRect(contour)

                file.write(f"Rectangle: x={x}, y={y}, width={w}, height={h}\n")
