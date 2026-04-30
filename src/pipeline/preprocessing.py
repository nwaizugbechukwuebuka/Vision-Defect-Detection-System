import cv2
import numpy as np

def preprocess_image(img, config):
    blur_k = config['preprocessing']['blur_kernel_size']
    canny1 = config['preprocessing']['canny_threshold1']
    canny2 = config['preprocessing']['canny_threshold2']
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (blur_k, blur_k), 0)
    edges = cv2.Canny(blurred, canny1, canny2)
    return edges
