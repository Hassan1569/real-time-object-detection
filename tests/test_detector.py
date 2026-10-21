
import numpy as np
import pytest
from src.detection.detector import load_model, detect_objects

def test_model_loads():
    """Verifies the model loads without crashing."""
    model = load_model()
    assert model is not None

def test_detect_on_blank_image():
    """Runs detection on a blank dummy image to verify the inference pipeline."""
    model = load_model()
    # Create a 640x640 black image
    dummy_image = np.zeros((640, 640, 3), dtype=np.uint8)
    results = detect_objects(model, dummy_image)
    assert results is not None
    assert hasattr(results, 'boxes')
    assert len(results.boxes) == 0  # Blank image should have no detections