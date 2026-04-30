import cv2
import numpy as np
import pickle
from sklearn.svm import SVC

def extract_features(cnt):
    _, _, w, h = cv2.boundingRect(cnt)

    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    aspect_ratio = w / float(h) if h != 0 else 0
    rect_area = w * h if (w * h) != 0 else 1
    extent = area / rect_area

    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    solidity = area / hull_area if hull_area > 0 else 0

    return [area, perimeter, aspect_ratio, extent, solidity]


X = []
y = []

for _ in range(50):
    X.append([10, 100, 10, 0.2, 0.3])
    y.append("scratch")

for _ in range(50):
    X.append([500, 200, 1.2, 0.8, 0.9])
    y.append("normal")

X = np.array(X, dtype=np.float32)
y = np.array(y)

model = SVC(kernel="linear", probability=True, C=1.0, gamma="scale", random_state=42)
model.fit(X, y)

with open("defect_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")