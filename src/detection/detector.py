"""
YOLO model loading and inference wrapper.
"""

import streamlit as st
from ultralytics import YOLO
from src.config import MODEL_PATH, DEFAULT_CONFIDENCE, IOU_THRESHOLD

@st.cache_resource(show_spinner=False)
def load_model() -> YOLO:
    """
    Loads the YOLO model once and caches it in Streamlit's resource cache.
    """
    # Ultralytics automatically downloads the weights if they don't exist at the path
    model = YOLO(str(MODEL_PATH))
    return model

def detect_objects(model: YOLO, image, conf: float = DEFAULT_CONFIDENCE):
    """
    Runs inference on a single image (ndarray or path).
    Returns the Ultralytics Results object.
    """
    results = model.predict(
        source=image,
        conf=conf,
        iou=IOU_THRESHOLD,
        verbose=False
    )
    return results[0]