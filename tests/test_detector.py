import pytest
import numpy as np
import cv2
from src.vision.defect_detector import DefectDetector
from src.utils.config_loader import load_config

def test_scratch_detection():
    config = load_config('config/config.yaml')
    detector = DefectDetector(config)
    # Simulate a scratch (long thin line)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.line(img, (10, 50), (90, 50), (255,255,255), 2)
    preprocessed = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 50, 150)
    defects, _ = detector.detect(preprocessed, img)
    assert any(d['defect_type'] == 'scratch' for d in defects)
