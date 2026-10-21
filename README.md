# real-time-object-detection

# Real-Time Object Detection AI 📸

A professional, local, browser-based application that performs real-time object detection using a webcam and uploaded images. Powered by **YOLOv8** and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36-red)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-yellow)

## Features
- **Real-Time Webcam Detection:** Detects 80 different object classes (people, laptops, phones, cups, etc.) live from your webcam.
- **Image Upload:** Run detection on static images.
- **Live Metrics:** Displays real-time FPS, detected object count, and camera status.
- **Adjustable Confidence Threshold:** Dynamically tune how "strict" the AI is using the sidebar slider.
- **Graceful Resource Management:** Safely releases the webcam when stopped.
- **Clean UI:** A modern, understated dashboard styled with a custom color palette.

## Tech Stack
- **Python 3.12**
- **Ultralytics YOLOv8** (`yolov8n.pt` - CPU optimized)
- **Streamlit** (UI & Web Server)
- **OpenCV** (Camera capture & image processing)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/real-time-object-detection.git
   cd real-time-object-detection