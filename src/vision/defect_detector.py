import cv2
from src.vision.contour_analysis import analyze_contours
from src.vision.feature_extractor import extract_features

class DefectDetector:
    def __init__(self, config):
        self.config = config

    def detect(self, preprocessed_img, original_img):
        contours, _ = cv2.findContours(preprocessed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        defects = []
        annotated = original_img.copy()
        confidence_threshold = self.config['defect_detection']['confidence_threshold']

        for cnt in contours:
            features = extract_features(cnt)
            x, y, w, h = cv2.boundingRect(cnt)

            if w > 0 and h > 0:
                aspect_ratio = max(w, h) / min(w, h)
                area = cv2.contourArea(cnt)

                if aspect_ratio > 8 and area < 800:
                    defect_type = "scratch"
                    confidence = 0.9
                else:
                    defect_type, confidence = analyze_contours(features, self.config)
            else:
                defect_type, confidence = analyze_contours(features, self.config)

            if confidence > confidence_threshold:
                cv2.drawContours(annotated, [cnt], -1, (0, 0, 255), 2)
                defects.append({
                    "event_type": "defect",
                    "defect_type": defect_type,
                    "confidence": float(confidence),
                    "status": "detected",
                    "bbox": (x, y, w, h)
                })

        return defects, annotated
