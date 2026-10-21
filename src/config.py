"""
Global configuration constants for the application.
"""

from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# Model settings
MODEL_PATH = ROOT_DIR / "assets" / "models" / "yolov8n.pt"
DEFAULT_CONFIDENCE = 0.35
IOU_THRESHOLD = 0.45

# UI / Drawing settings
BOX_COLOR = (49, 94, 251)  # Accent Blue from design.md (BGR format for OpenCV: #FB5E31)
TEXT_COLOR = (255, 255, 255)  # White
BOX_THICKNESS = 2
FONT_SCALE = 0.5