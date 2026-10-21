"""
Image input/output utilities.
"""

import cv2
import numpy as np

def bytes_to_ndarray(image_bytes: bytes) -> np.ndarray:
    """
    Converts raw bytes (e.g., from a Streamlit uploader) to an OpenCV BGR ndarray.
    Raises ValueError if the image cannot be decoded.
    """
    if not image_bytes:
        raise ValueError("Empty image bytes provided.")
        
    nparr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is None:
        raise ValueError("Could not decode image. File may be corrupted or unsupported.")
        
    return frame