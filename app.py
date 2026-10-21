"""
Real-Time Object Detection Dashboard - Main Application.
"""

import streamlit as st
import cv2
import time

from src.config import DEFAULT_CONFIDENCE
from src.detection.detector import load_model, detect_objects
from src.detection.annotator import draw_detections
from src.utils.image_io import bytes_to_ndarray
from src.utils.metrics import FPSCounter
from src.camera.capture import CameraStream

# --- Page Config & Setup ---
st.set_page_config(page_title="Object Detection AI", layout="wide", initial_sidebar_state="collapsed")

# --- Session State Initialization ---
if "running" not in st.session_state:
    st.session_state.running = False
if "camera" not in st.session_state:
    st.session_state.camera = CameraStream()
if "fps_counter" not in st.session_state:
    st.session_state.fps_counter = FPSCounter()

# --- Load Model ---
with st.spinner("Loading YOLO Model..."):
    model = load_model()

# --- Layout ---
st.title("Real-Time Object Detection")
st.markdown("---")

# Sidebar Controls
with st.sidebar:
    st.header("Controls")
    conf_threshold = st.slider("Confidence Threshold", min_value=0.10, max_value=0.90, value=DEFAULT_CONFIDENCE, step=0.05)
    
    if st.button("Start Camera", use_container_width=True, type="primary" if not st.session_state.running else "secondary"):
        st.session_state.running = True
        st.rerun()
        
    if st.button("Stop Camera", use_container_width=True, type="primary" if st.session_state.running else "secondary"):
        st.session_state.running = False
        st.session_state.camera.release()
        st.rerun()

    st.markdown("---")
    st.header("Image Upload")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Main Layout (2/3 Video, 1/3 Metrics)
col_video, col_metrics = st.columns([2, 1])

with col_metrics:
    st.subheader("Live Metrics")
    fps_placeholder = st.empty()
    obj_count_placeholder = st.empty()
    status_placeholder = st.empty()
    
    if st.session_state.running:
        status_placeholder.success("Status: Camera Active")
    else:
        status_placeholder.info("Status: Idle")

with col_video:
    st.subheader("Live Feed")
    video_placeholder = st.empty()

# --- Image Upload Handling ---
if uploaded_file is not None:
    try:
        img_bytes = uploaded_file.getvalue()
        frame = bytes_to_ndarray(img_bytes)
        
        results = detect_objects(model, frame, conf=conf_threshold)
        annotated = draw_detections(frame, results)
        
        # Convert BGR (OpenCV) to RGB (Streamlit)
        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        
        with col_video:
            video_placeholder.image(annotated_rgb, caption="Uploaded Image Detection", use_column_width=True)
            
        with col_metrics:
            obj_count_placeholder.metric("Detected Objects", len(results.boxes))
            
    except Exception as e:
        st.error(f"Failed to process image: {e}")

# --- Webcam Loop Handling ---
elif st.session_state.running:
    camera = st.session_state.camera
    
    if not camera.open():
        st.error("Could not open webcam. Please check your camera permissions.")
        st.session_state.running = False
    else:
        while st.session_state.running:
            frame = camera.read()
            if frame is None:
                st.error("Lost connection to webcam.")
                camera.release()
                st.session_state.running = False
                break
                
            # Inference
            results = detect_objects(model, frame, conf=conf_threshold)
            annotated = draw_detections(frame, results)
            
            # Convert and display
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            video_placeholder.image(annotated_rgb, use_column_width=True)
            
            # Metrics
            fps = st.session_state.fps_counter.update()
            obj_count = len(results.boxes)
            
            fps_placeholder.metric("FPS", f"{fps:.1f}")
            obj_count_placeholder.metric("Objects Detected", obj_count)
            
else:
    # Idle State
    with col_video:
        video_placeholder.info("Camera is stopped. Click 'Start Camera' in the sidebar to begin.")