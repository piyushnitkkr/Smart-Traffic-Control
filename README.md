# 🚦 Smart Traffic Control System Using YOLOv5

A Machine Learning-based Smart Traffic Control System that dynamically adjusts signal timing based on the number of vehicles (cars, trucks, buses) in each lane. The system uses a pretrained or fine-tuned YOLOv5 model for vehicle detection and offers a real-time simulation dashboard using Streamlit.

---

## 📸 Project Overview

In developing countries, manual or fixed-timer traffic lights often lead to congestion. This project aims to automate traffic signal control based on real-time analysis of traffic density from road images or video feeds.  

✅ Detects and counts vehicles using YOLOv5  
✅ Computes optimal green light duration for each lane  
✅ Displays a dynamic signal simulation dashboard  
✅ Allows customization using custom datasets like IDD or IDK20K

---

## 🧠 Features

- 🔍 YOLOv5-based vehicle detection (car, truck, bus)
- 🧠 Adaptive signal timing based on vehicle count
- 📊 Real-time traffic signal simulation via Streamlit
- 📥 Support for images or videos as input
- 💾 Export results to `.csv` or `.json` format
- ⚙️ Custom model training using Indian Driving Dataset (IDD) or IDK20K

---

## 🏗️ Folder Structure

Smart-Traffic-Control/
├── yolov5/ # YOLOv5 core repo (cloned from Ultralytics)
├── idd_dataset/ # Custom dataset in YOLO format
│ ├── train/
│ │ ├── images/
│ │ └── labels/
│ └── valid/
│ ├── images/
│ └── labels/
│ └── data.yaml # Dataset config
├── traffic_control_notebook.ipynb # Jupyter logic notebook
├── streamlit_app.py # Streamlit UI for signal simulation
├── signal_output.csv # Output file with lane-wise durations
├── test_images/ # Sample test images for prediction
└── README.md

---

## 🚀 Getting Started

### 1. Clone YOLOv5 and Install Dependencies
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt

### 2. Setup Dataset
idd_dataset/
  ├── train/images/
  ├── train/labels/
  ├── valid/images/
  └── valid/labels/


### 3. Train Model (Optional)
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 50 \
  --data ../idd_dataset/data.yaml \
  --weights yolov5x.pt \
  --name yolov5x_idd_finetune

### StreamLit Dashboard
streamlit run streamlit_app.py

### Demo Video
I have added a demo video in the repo


