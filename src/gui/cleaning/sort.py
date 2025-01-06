import cv2
import itertools

def read_rectangles(file_path):
    rectangles = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("Rectangle:"):
                parts = line.split(", ")
                x = int(parts[0].split("=")[1])
                y = int(parts[1].split("=")[1])
                width = int(parts[2].split("=")[1])
                height = int(parts[3].split("=")[1])
                rectangles.append((x, y, width, height))
    return rectangles

def group_by_nearest_y(rectangles):
    sorted_rects = sorted(rectangles, key=lambda r: r[1])
    grouped = list(itertools.zip_longest(*[iter(sorted_rects)]*3))
    grouped_sorted_by_x = [sorted(group, key=lambda r: r[0]) for group in grouped if group]
    return grouped_sorted_by_x

def annotate_image(image_path, grouped_coordinates, output_path):
    img = cv2.imread(image_path)
    numbered_coordinates = [(idx + 1, coord) for idx, coord in enumerate(itertools.chain.from_iterable(grouped_coordinates))]
    for number, (x, y, _, _) in numbered_coordinates:
        cv2.putText(img, str(number), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
    cv2.imwrite(output_path, img)

def save_sorted_rectangles(grouped_rectangles, output_file):
    with open(output_file, 'w') as file:
        idx = 1
        for group in grouped_rectangles:
            for x, y, width, height in group:
                if x is not None and y is not None:
                    file.write(f"Rectangle {idx}: x={x}, y={y}, width={width}, height={height}\n")
                    idx += 1

def process_coordinates(file_path, image_path, output_image_path, output_file_path):
    rectangles = read_rectangles(file_path)
    grouped_rectangles = group_by_nearest_y(rectangles)
    
    x_y_matrix = []
    width_height_matrix = []

    for group in grouped_rectangles:
        x_y_group = [(x, y) for x, y, _, _ in group if x is not None and y is not None]
        width_height_group = [(width, height) for _, _, width, height in group if width is not None and height is not None]
        
        x_y_matrix.append(x_y_group)
        width_height_matrix.append(width_height_group)

    print("\nX, Y Matrix:")
    for group in x_y_matrix:
        print(group)

    print("\nWidth and Height Matrix:")
    for group in width_height_matrix:
        print(group)
    
    annotate_image(image_path, grouped_rectangles, output_image_path)
    save_sorted_rectangles(grouped_rectangles, output_file_path)

    return x_y_matrix, width_height_matrix
