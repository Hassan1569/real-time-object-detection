"""
Draws bounding boxes and labels on images.
"""

import cv2
import numpy as np
from src.config import BOX_COLOR, TEXT_COLOR, BOX_THICKNESS, FONT_SCALE

def draw_detections(frame: np.ndarray, results) -> np.ndarray:
    """
    Draws bounding boxes and labels on a copy of the frame.
    `results` is the output from detector.detect_objects().
    """
    annotated_frame = frame.copy()
    
    # results.boxes contains the bounding boxes and metadata
    if results.boxes is None:
        return annotated_frame

    for box in results.boxes:
        # Get coordinates (x1, y1, x2, y2)
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        
        # Get confidence and class name
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        label = f"{results.names[cls_id]} {conf:.2f}"
        
        # Draw bounding box
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), BOX_COLOR, BOX_THICKNESS)
        
        # Draw label background
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, 1)
        cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + w, y1), BOX_COLOR, -1)
        
        # Draw label text
        cv2.putText(
            annotated_frame, 
            label, 
            (x1, y1 - 5), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            FONT_SCALE, 
            TEXT_COLOR, 
            1
        )

    return annotated_frame