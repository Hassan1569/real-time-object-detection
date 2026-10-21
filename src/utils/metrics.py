"""
Utilities for calculating real-time metrics.
"""

import time

class FPSCounter:
    def __init__(self, window_size: int = 30):
        self.window_size = window_size
        self.timestamps = []

    def update(self) -> float:
        """Records a new frame timestamp and returns the calculated FPS."""
        now = time.perf_counter()
        self.timestamps.append(now)
        
        if len(self.timestamps) > self.window_size:
            self.timestamps.pop(0)
            
        if len(self.timestamps) < 2:
            return 0.0
            
        time_diff = self.timestamps[-1] - self.timestamps[0]
        if time_diff == 0:
            return 0.0
            
        return (len(self.timestamps) - 1) / time_diff