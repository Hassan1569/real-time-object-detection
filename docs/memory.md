# Project Memory

## Current phase
Phase 1 — Documentation & scaffolding (in progress; awaiting user confirmation after paste).

## Key decisions
- Stack: Python 3.11, Streamlit, Ultralytics YOLOv8n, OpenCV, NumPy, Pillow, pytest.
- Model: `yolov8n.pt` (CPU-friendly). License: AGPL-3.0 (Ultralytics) — do not claim commercial use without review.
- Weights stored in `assets/models/` and gitignored; auto-download on first run if network allows.
- Single-process architecture; no HTTP, DB, or cloud.
- Docs live in `docs/` (the six source-of-truth files).

## Files created / changed
- Phase 0: full project tree scaffolded locally via PowerShell (user action).
- Phase 1: writing six `docs/*.md`, `.gitignore`, `requirements.txt`, `.streamlit/config.toml`.

## Commands actually run
- Phase 0: `git init` (user, local). No other commands executed by me — no workspace access.
- Phase 1: none executed; files are pasted by user.

## Known bugs / issues
- None open.

## Current limitations
- No workspace access from assistant; all file operations are user-side.
- Streamlit webcam latency not yet validated (Phase 3 gate).
- Commercial license of Ultralytics not verified for any commercial claim.

## Exact next step
After user confirms Phase 1 paste + commit, begin Phase 2 with `src/config.py`, then `src/detection/detector.py`, `src/detection/annotator.py`, `src/utils/image_io.py`, and their tests.