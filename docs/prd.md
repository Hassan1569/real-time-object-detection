# Product Requirements Document — Real-Time Object Detection AI

## Purpose
A local, browser-based desktop app that detects objects in real time from a laptop webcam and from uploaded images, using a pretrained YOLO model. Built as a portfolio-grade, single-developer project.

## Target users
- Recruiters / reviewers evaluating a computer-vision portfolio project.
- Students and hobbyists wanting a clean local detection tool.
- Developers seeking a reference Streamlit + OpenCV + YOLO integration.

## Core features (MVP)
- Webcam live detection with Start / Stop controls.
- Bounding boxes, class names, confidence scores on the frame.
- Metric cards: measured FPS, total detected objects, current model status.
- Single-image upload detection.
- Configurable confidence threshold (UI control).
- Clear loading, error, and camera-permission-denied states.
- Graceful camera release on Stop and on app exit.

## Non-goals (MVP)
- Video-file upload.
- Model training or fine-tuning.
- Multi-camera support.
- User accounts, authentication, cloud deploy.
- Commercial-use licensing claims.

## User stories
- **US-1** As a user, I can press Start and see my webcam feed annotated with detections.
- **US-2** As a user, I can press Stop and the camera is released immediately.
- **US-3** As a user, I can upload an image and see detections on it.
- **US-4** As a user, I can adjust the confidence threshold and see the result change.
- **US-5** As a user, I see a clear message if the camera is unavailable or permission is denied.
- **US-6** As a user, I see the real measured FPS, not a fabricated number.

## Acceptance criteria
- US-1: pressing Start opens the webcam within 2 s on a normal laptop; boxes render each frame.
- US-2: after Stop, the webcam LED turns off and the device is released (verified via `cv2.VideoCapture.isOpened()` returning False on a re-acquire attempt after short delay).
- US-3: a valid JPG/PNG upload produces an annotated image within a few seconds on CPU.
- US-4: dragging the threshold updates detections on the next frame/image without reloading the model.
- US-5: with the camera blocked/unplugged, the UI shows a non-technical error, not a traceback.
- US-6: FPS is computed from real frame timings, not hardcoded.

## Functional requirements
- FR-1: Model loaded once per session and cached.
- FR-2: Confidence threshold default `0.35`, adjustable `0.10`–`0.90`.
- FR-3: Only COCO-class names from the pretrained model are displayed.
- FR-4: Start/Stop toggles are idempotent (no double-open).
- FR-5: Image upload validated for type and decodability before inference.

## Non-functional requirements
- NFR-1: Runs on Windows 10/11 with Python 3.11, CPU only.
- NFR-2: Target ≥ 5 FPS on a typical laptop CPU at model input 640 with `yolov8n`.
- NFR-3: No paid APIs, no API keys, no cloud dependency.
- NFR-4: No secrets in repo; model weights not committed.
- NFR-5: UI must not block during inference (Streamlit rerun-safe caching).

## Supported inputs / outputs
- Input: webcam stream, single image (`.jpg`, `.jpeg`, `.png`).
- Output: annotated frame/image, metric cards (FPS, object count, status), class list.

## Error states
- Camera not found / permission denied.
- Invalid or undecodable image.
- Model weights missing and download blocked (offline).
- Inference exception (logged, shown as a friendly banner).

## Performance expectations (CPU)
- `yolov8n` @ 640 on integrated graphics laptops: ~5–12 FPS.
- Image inference: < 2 s typical.
- UI reruns kept lightweight; model cached.

## MVP vs future
- **MVP**: webcam + image + metrics + robust errors.
- **Future**: video file, class filter chips, export annotated image, session summary, packaging via PyInstaller.