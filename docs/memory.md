# Project Memory

## Current phase
Phase 7 — Release prep and GitHub publication.

## Key decisions
- Successfully implemented YOLOv8n with Streamlit.
- Webcam and image upload working with dynamic confidence thresholds.
- FPS metrics calculated via rolling time diff.

## Files created / changed
- `app.py` (Streamlit UI and loop)
- `src/detection/detector.py` (Model)
- `src/camera/capture.py` (Webcam)
- `src/utils/image_io.py` and `metrics.py`
- `README.md` and `requirements.txt`

## Known bugs / issues
- None. Core functionality verified on Windows 11 with Python 3.12.

## Exact next step
Final Git commit and push to GitHub.