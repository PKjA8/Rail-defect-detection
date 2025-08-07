from ultralytics import YOLO
import numpy as np
import cv2

def load_model(model_path):
    return YOLO(model_path)

def run_detection(model, image):
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    results = model(image_bgr)
    annotated_image = results[0].plot()

    detections = []
    for detection in results[0].boxes:
        label = int(detection.cls)
        confidence = float(detection.conf)
        detections.append((label, confidence))

    return annotated_image, detections
