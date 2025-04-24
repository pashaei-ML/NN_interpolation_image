from PIL import Image
import numpy as np

def resizing_nn(path, factor):
    image = Image.open(path).convert("L")
    image.show()
    w, h = image.size
    print("Original Height, Width:", h, w)
    matrix = np.array(image)
    
    n_w = int(factor * w)
    n_h = int(factor * h)
    new_image = np.zeros((n_h, n_w), dtype=np.uint8)

    for j in range(n_h):
        for i in range(n_w):
            x = int(i / factor)
            y = int(j / factor)
            if 0 <= x < w and 0 <= y < h:
                new_image[j, i] = matrix[y, x]
            else:
                new_image[j, i] = 0

    img = Image.fromarray(new_image)
    img.show()

path = input("Enter the path to the image: ")
factor = float(input("Enter the scaling factor (e.g., 2 for 2x): "))
resizing_nn(path, factor)
