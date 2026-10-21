
import numpy as np
from src.detection.annotator import draw_detections

class MockBox:
    def __init__(self):
        self.xyxy = [[10, 10, 100, 100]]
        self.conf = [0.85]
        self.cls = [0]

class MockResults:
    def __init__(self):
        self.boxes = [MockBox()]
        self.names = {0: "person"}

def test_draw_detections():
    """Verifies that the annotator properly draws boxes on a frame."""
    frame = np.zeros((500, 500, 3), dtype=np.uint8)
    results = MockResults()
    
    annotated = draw_detections(frame, results)
    
    assert annotated.shape == (500, 500, 3)
    # Verify that pixels were actually drawn (the array is no longer all zeros)
    assert np.any(annotated != 0)