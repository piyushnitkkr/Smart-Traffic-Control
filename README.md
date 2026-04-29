# 🚦 Smart Traffic Control System Using YOLOv5

A Machine Learning-based Smart Traffic Control System that dynamically adjusts traffic signal timing based on vehicle density in each lane. The system uses YOLOv5 for vehicle detection and provides a simulation using Python and Streamlit.

---

## 📸 Project Overview

Traditional traffic systems use fixed timers, which often cause unnecessary congestion. This project improves traffic efficiency by:

* Detecting vehicles from images or video
* Counting cars, buses, and trucks
* Dynamically assigning signal durations
* Simulating traffic signals via a dashboard

---

## 🧠 Features

* 🔍 YOLOv5-based vehicle detection
* 🚗 Counts cars and heavy vehicles (bus, truck)
* ⏱️ Dynamic signal timing algorithm
* 📊 CSV output for lane-wise traffic data
* 🎥 Supports image and video input (Demo included)
* 🌐 Streamlit dashboard for visualization

---

## 📁 Project Structure

```
Smart-Traffic-Control/
│
├── data/                  # Input images (lanes)
├── Demo.mp4               # Demo video
├── LICENSE
├── README.md
│
├── app.py                 # Streamlit dashboard
├── main.py                # Main execution script
├── detect.py              # YOLOv5 detection logic
├── traffic_logic.py       # Signal timing algorithm
├── utils.py               # Helper functions
├── train.py               # Model training script
│
├── requirement.txt        # Dependencies
├── signal_output.csv      # Output results
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/piyushnitkkr/Smart-Traffic-Control.git
cd Smart-Traffic-Control
```

### 2. Install Dependencies

```bash
pip install -r requirement.txt
```

### 3. Clone YOLOv5

```bash
git clone https://github.com/ultralytics/yolov5
```

---

## 📥 Dataset

Download the dataset from the official sources:

* Indian Driving Dataset (IDD): [https://idd.insaan.iiit.ac.in/](https://idd.insaan.iiit.ac.in/)
* IDD Detection Dataset: [https://cvit.iiit.ac.in/research/projects/cvit-projects/idd-detection](https://cvit.iiit.ac.in/research/projects/cvit-projects/idd-detection)

After downloading, convert or arrange the dataset in YOLO format if needed.

---

## 🚀 Usage

### ▶️ Run Detection + Signal Logic

```bash
python main.py
```

This will:

* Process lane images from `/data`
* Detect vehicles
* Calculate signal timing
* Save output in `signal_output.csv`

---

### 🌐 Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 🧠 Signal Timing Logic

The system assigns time using:

```
duration = base_time + (cars × weight1) + (trucks/buses × weight2)
```

* Cars → lower weight
* Trucks/Buses → higher weight
* Max cap applied to avoid starvation

---

## 🏋️ Model Training (Optional)

```bash
python train.py
```

* Uses YOLOv5 pretrained weights
* Can be fine-tuned on custom datasets (IDD / IDK20K)

---

## 📊 Output Example

| Lane | Cars | Big Vehicles | Duration (sec) |
| ---- | ---- | ------------ | -------------- |
| 1    | 10   | 2            | 38             |
| 2    | 5    | 1            | 24             |

Saved as:

```
signal_output.csv
```

---

## 🎥 Demo

A demo video is included in the repository:

```
Demo.mp4
```

---

## 🔮 Future Improvements

* 🚦 Real-time CCTV feed integration
* 🧠 Reinforcement Learning-based signal optimization
* 📍 Multi-intersection coordination
* ☁️ Deployment on cloud with GPU

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
