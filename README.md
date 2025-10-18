# 🚀 YOLOv8 Real-Time Object Detection

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7.0-brightgreen)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project is a **real-time object detection system** built using **YOLOv8** and **Tkinter GUI**.  
It can detect objects from:

- 🎥 **Webcam feeds**  
- 📸 **Images**  
- 🎬 **Video files**  
- 📷 **External cameras**  

Detected objects are **logged in a scrollable GUI text box**, making it easy for users to view detections in real-time.  

> ⚡ Lightweight YOLOv8n model ensures **fast and accurate detection**.

---

## ✨ Features

- Real-time object detection from multiple sources.  
- Logs detected objects in a **scrollable text box**.  
- ✅ Lightweight YOLOv8n model for fast detection.  
- 🖥️ Intuitive **Tkinter GUI** with buttons for:
  - Start Webcam  
  - Start External Camera  
  - Browse Image  
  - Browse Video  
  - Stop Detection  
- 🧵 Threaded video processing ensures **smooth GUI performance**.  

---


## 📂 Folder Structure
```bash
YOLOv8-Object-Detection/
│
├── README.md                   # This file
├── requirements.txt            # Project dependencies
├── main.py                     # Full Python code
├── images/                     # Test images
│   └── sample.jpg
├── videos/                     # Test videos
    └── sample.mp4
 
```
## ⚙️ Installation

**1.Clone the repository:**
```bash
git clone https://github.com/<username>/YOLOv8-Object-Detection.git
cd YOLOv8-Object-Detection
```

**2.Install dependencies:**
```bash
pip install -r requirements.txt
```

**3.Run the project:**
```bash
python main.py
```

YOLOv8 will automatically download the model if not present locally.

## 🎮 Usage
## 🛠️ GUI Buttons
Button	      Description
🎥 Start  Webcam	Real-time detection from your default webcam.
📷 Start  External Cam	Detection from an external camera.
🖼️ Browse Image	Select an image file for detection.
🎬 Browse System Video	Select a video file for detection.
⏹️ Stop   Detection	Stop any running detection safely.

- Detected objects appear in the GUI text box with counts.
- Detection runs until stopped or OpenCV window is closed.

## 🧩 How It Works

**1.YOLOv8 Model**
- Loads yolov8n.pt automatically to detect objects.
- Detects multiple object types from the COCO dataset.
**2.Video/Image Processing**
  - OpenCV resizes and processes frames
  - Annotated frames are displayed in real-time.

**3.GUI Logging**
- Tkinter GUI shows a scrollable text box listing detected objects.
- Only new objects are logged to avoid duplicates.

**4.Threading**
- Video/image detection runs in a separate thread for smooth GUI Performance.

## 🔮 Future Enhancements

- Integrate DeepSORT for object tracking with unique IDs.

- Save detection logs to CSV or database.

- Mobile-friendly or web-based GUI.

- Customizable detection thresholds and models.
---
## 📦 Requirements

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- Imutils
- Tkinter
- NumPy

**Install all dependencies:**
```bash
pip install -r requirements.txt
```


## 🙏 Acknowledgements

- Ultralytics YOLOv8
- OpenCV
- Imutils
- Tkinter

