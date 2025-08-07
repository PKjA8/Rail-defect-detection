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

# 📂 Project Structure

```
rail-defect-detection/
├── data/
│   ├── train/
│   ├── val/
│   └── data.yaml
├── app/
│   └── defect_detection_app.py
├── models/
│   └── yolov8n.pt
├── notebooks/
│   └── model_training.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Running the App Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rail-defect-detection.git
   cd rail-defect-detection
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Streamlit App**
   ```bash
   streamlit run app/defect_detection_app.py
   ```

---

## 📊 Model Evaluation

- **Precision**: Accurately identifies actual defects without false positives.
- **Recall**: Captures most actual defects with minimal false negatives.
- **IoU (Intersection over Union)**: High bounding box accuracy.
- **Manual Accuracy Tool**: Users can validate and compare detection accuracy.

---

## 🎯 Future Enhancements

- ✅ **Expand the dataset**: Include more defect types like rust, wear, rail joint failures, etc.
- 📦 **Optimize for embedded systems**: Reduce model size and improve inference time for deployment on edge devices such as drones and robotic vehicles.
- 🔗 **Integrate with maintenance alert systems**: Enable auto-generation of work orders or notifications based on detected defects.
- 🎥 **Video-based detection support**: Add real-time video frame detection and annotation for continuous surveillance.

---

## 👨‍💻 Authors

- **Pradeep Kumar**  
  B.Tech in AI & Data Science, Gati Shakti Vishwavidyalaya  
- **Harphool Singh**  
  B.Tech in AI & Data Science, Gati Shakti Vishwavidyalaya  
- **Asmit Sharma**  
  B.Tech in AI & Data Science, Gati Shakti Vishwavidyalaya  
- **Vimal **  
  M.Tech in Railway Engineering, Gati Shakti Vishwavidyalaya  
- **Mentor**: Dr. Vipul Kumar Mishra  
  Associate Professor, Department of AI & DS, Gati Shakti Vishwavidyalaya

---

## 📜 License

This project is intended for academic and research purposes only. For commercial or production use, please contact the project authors for permission.

---

## 📎 References

- [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com)
- [Railway Track Fault Detection Dataset – Kaggle](https://www.kaggle.com/datasets/salmaneunus/railway-track-fault-detection)
- [Roboflow Rail Defect Dataset](https://universe.roboflow.com/defect-rexb3/rail-defect)
- [Streamlit Documentation](https://docs.streamlit.io)
