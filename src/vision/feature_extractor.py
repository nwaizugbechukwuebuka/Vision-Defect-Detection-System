import cv2
import numpy as np

def extract_features(contour):
    area = cv2.contourArea(contour)
    arc_length = cv2.arcLength(contour, True)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w) / h if h != 0 else 0
    return {
        'area': area,
        'arc_length': arc_length,
        'aspect_ratio': aspect_ratio,
        'bounding_box': (x, y, w, h)
    }
