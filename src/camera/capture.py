"""
Webcam capture wrapper with safe resource cleanup.
"""

import cv2
import numpy as np

class CameraStream:
    def __init__(self, src: int = 0):
        self.src = src
        self.cap = None

    def open(self) -> bool:
        """Attempts to open the webcam."""
        if self.cap is not None and self.cap.isOpened():
            return True
            
        self.cap = cv2.VideoCapture(self.src, cv2.CAP_DSHOW)  # CAP_DSHOW is for Windows
        return self.cap.isOpened()

    def read(self) -> np.ndarray | None:
        """Reads a frame. Returns None if the read fails."""
        if self.cap is None or not self.cap.isOpened():
            return None
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        """Safely releases the camera resource."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None