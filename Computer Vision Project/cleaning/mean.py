import cv2
import numpy as np

def highlight_gold(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define the range for gold color in HSV
    lower_gold = np.array([10, 80, 20])  # Lower bound of gold
    upper_gold = np.array([80, 255, 255])  # Upper bound of gold
    
    # Create a mask for gold color
    mask = cv2.inRange(hsv_image, lower_gold, upper_gold)
    
    # Apply the mask to isolate the gold areas
    gold_highlighted = cv2.bitwise_and(image, image, mask=mask)
    
    # Apply mean shift filtering
    filtered_image = cv2.pyrMeanShiftFiltering(image, sp=20, sr=40)
    
    # Combine the filtered image with the gold mask
    combined_result = cv2.bitwise_and(filtered_image, filtered_image, mask=mask)
    
    # Save the result as "meanshift.jpg"
    cv2.imwrite("meanshift.jpg", combined_result)
    
    return gold_highlighted, combined_result

# Example usage
gold_highlighted, result = highlight_gold("photos/dupa1.jpg")

# Optionally display results
cv2.imshow("Gold Highlighted", gold_highlighted)
cv2.imshow("Filtered with Highlight", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
