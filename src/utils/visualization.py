import cv2
import os

def save_annotated_image(img, img_name, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f'annotated_{img_name}')
    cv2.imwrite(out_path, img)
