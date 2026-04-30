import cv2
import pickle
import numpy as np

class MLDefectDetector:
    def __init__(self, model_path, config):
        self.model = pickle.load(open(model_path, "rb"))
        self.config = config

    def extract_features(self, cnt):
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)

        aspect_ratio = w / h if h != 0 else 0
        rect_area = w * h if w * h != 0 else 1
        extent = area / rect_area
        solidity = area / cv2.contourArea(cv2.convexHull(cnt)) if cv2.contourArea(cv2.convexHull(cnt)) != 0 else 0

        return np.array([area, perimeter, aspect_ratio, extent, solidity]).reshape(1, -1)

    def detect(self, preprocessed_img, original_img):
        contours, _ = cv2.findContours(preprocessed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        defects = []
        annotated = original_img.copy()

        for cnt in contours:
            features = self.extract_features(cnt)
            prediction = self.model.predict(features)[0]
            confidence = max(self.model.predict_proba(features)[0])

            if confidence > self.config["defect_detection"]["confidence_threshold"]:
                x, y, w, h = cv2.boundingRect(cnt)

                cv2.drawContours(annotated, [cnt], -1, (0, 0, 255), 2)

                defects.append({
                    "event_type": "defect",
                    "defect_type": prediction,
                    "confidence": float(confidence),
                    "bbox": (x, y, w, h)
                })

        return defects, annotated