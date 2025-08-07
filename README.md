# 🚆 Rail Defect Detection using YOLOv8

This project focuses on automating railway track defect detection using deep learning. Leveraging the YOLOv8-nano model and a user-friendly Streamlit interface, the system enables fast, real-time identification of defects in railway track images. It enhances railway safety and supports proactive maintenance.

---

## 📌 Overview

- **Objective**: Real-time defect detection in railway tracks from images.
- **Core Tech**: YOLOv8-nano (object detection), Streamlit (web interface).
- **Dataset**: Public datasets from [Kaggle](https://www.kaggle.com/datasets/salmaneunus/railway-track-fault-detection) and [Roboflow](https://universe.roboflow.com/).
- **Outcome**: An accurate, scalable, and user-accessible tool for infrastructure monitoring.

---

## 🧠 Key Features

- **🔍 Real-Time Object Detection**  
  Detects railway defects with bounding boxes and confidence scores.

- **🖼️ Batch Image Upload & Processing**  
  Upload folders of images to process multiple images in one go.

- **📊 Accuracy Calculator**  
  Allows manual validation and model accuracy estimation.

- **🧾 Detection Summary Table**  
  View detected defect classes and confidence scores in a clear table format.

- **🧠 Caching for Reuse**  
  Avoids reprocessing already-checked images during the same session.

---

## 🛠 Tech Stack

| Category             | Technology                     |
|----------------------|--------------------------------|
| Model                | YOLOv8-nano (Ultralytics)      |
| Framework            | PyTorch 2.6, CUDA 12.4         |
| Interface            | Streamlit                      |
| Dataset Source       | Kaggle, Roboflow               |
| Training Environment | Tesla T4 GPU                   |
| Language             | Python                         |

---

## 📦 Project Structure

