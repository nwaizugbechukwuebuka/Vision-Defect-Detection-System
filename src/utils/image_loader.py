import cv2
import os

def load_images(directory):
    print("Loading from:", directory)
    print("Exists:", os.path.exists(directory))

    images = []

    for fname in os.listdir(directory):
        print("Found file:", fname)

        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            path = os.path.join(directory, fname)
            img = cv2.imread(path)

            if img is None:
                print("Failed to read:", path)
            else:
                images.append((fname, img))

    print("Total images loaded:", len(images))
    return images
