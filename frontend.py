import streamlit as st 
import os
from PIL import Image
import numpy as np
import pandas as pd
import cv2
import base64

from main import load_model, run_detection

# Load YOLO model
model = load_model(r"D:\2ndY\Sem_2\ML\Rail_Defect_Detection\Final_Project\best.pt")

# Streamlit UI Configuration
st.set_page_config(
    page_title="Railway Track Defect Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Load and display logo and heading ===
logo_path = r"D:\2ndY\Sem_2\ML\Rail_Defect_Detection\Final_Project\gsv_logo_img.png"

# Load logo and encode as base64
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# Centered logo, heading, title, and description
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{encoded_logo}' width='150'/>
        <h1 style='margin-bottom: 0;'>GATI SHAKTI VISHWAVIDYALAYA , VADODARA</h1>
        <h1 style='margin-top: 10px;'>🚂 Railway Track Defect Detection</h1>
        <p style='font-size: 18px;'>
            Analyze railway track images for potential defects using the YOLOv8 model.<br>
            This app organizes results in an easy-to-read format.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Settings")
folder_path = st.sidebar.text_input("📂 Enter Folder Path:")

# Session state initialization
if "summary_data" not in st.session_state:
    st.session_state.summary_data = []
if "image_files" not in st.session_state:
    st.session_state.image_files = []

# Image Processing
if folder_path:
    if os.path.isdir(folder_path):
        st.success(f"📁 Found folder: {folder_path}")
        image_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(("jpg", "jpeg", "png"))
        ]

        if image_files:
            if not st.session_state.image_files or st.session_state.image_files != image_files:
                st.info(f"🔍 Processing {len(image_files)} image(s)...")
                st.session_state.summary_data = []
                st.session_state.image_files = image_files

                tabs = st.tabs(image_files)

                for idx, image_file in enumerate(image_files):
                    image_path = os.path.join(folder_path, image_file)
                    image = Image.open(image_path)

                    annotated_image, detections = run_detection(model, image)

                    detection_status = "Defects Detected" if detections else "No Defects"

                    st.session_state.summary_data.append({
                        "Image Name": image_file,
                        "Status": detection_status,
                        "Detections": ", ".join(
                            [f"Label: {d[0]}, Confidence: {d[1]:.2f}" for d in detections]
                        )
                    })

                    with tabs[idx]:
                        st.subheader(f"Image: {image_file}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(image, caption="Original Image", use_container_width=True)
                        with col2:
                            st.image(annotated_image, caption="Detected Image", use_container_width=True)
                        if detections:
                            st.markdown("### Detection Details")
                            for label, confidence in detections:
                                st.write(f"- *Label: {label}, **Confidence*: {confidence:.2f}")
            else:
                st.success("✅ Already processed images. Showing results from cache.")

            st.markdown("## 📝 Detection Summary")
            summary_df = pd.DataFrame(st.session_state.summary_data)
            st.dataframe(summary_df, use_container_width=True)

            st.markdown("## 🎯 Accuracy Calculator")
            total_images = st.number_input("Enter total number of images:", min_value=1, value=len(st.session_state.image_files))
            correct_predictions = st.number_input("Enter number of correct predictions:", min_value=0, value=0)

            if st.button("Calculate Accuracy"):
                accuracy = (correct_predictions / total_images) * 100
                st.success(f"📊 Accuracy: *{accuracy:.2f}%*")

        else:
            st.warning("⚠ No valid images found in the folder.")
    else:
        st.error("🚫 The specified folder does not exist.")
else:
    st.info("📝 Please enter a folder path to get started.")
