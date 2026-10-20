# Roadmap / Tasks

## Phase 0 — Inspect & plan
- [x] Confirm MVP scope
- [x] Provide project tree + PowerShell scaffolding command
- [x] `git init`

## Phase 1 — Documentation & scaffolding
- [ ] Write six `docs/*.md`
- [ ] Write `.gitignore`, `requirements.txt`, `.streamlit/config.toml`
- [ ] Commit: `docs: add project documentation and scaffolding`

## Phase 2 — Model loading & image inference
- [ ] `src/config.py`
- [ ] `src/detection/detector.py` (load + detect)
- [ ] `src/detection/annotator.py`
- [ ] `src/utils/image_io.py`
- [ ] Tests: `tests/test_detector.py`, `tests/test_annotator.py`
- [ ] Verify: run a small image through detector in a REPL/script
- [ ] Commit: `feat: add YOLO model loading and image inference`

## Phase 3 — Webcam detection & resource management
- [ ] `src/camera/capture.py`
- [ ] `src/utils/metrics.py`
- [ ] Verify camera open/read/release and Stop behavior
- [ ] Commit: `feat: add webcam capture with safe resource cleanup`

## Phase 4 — UI
- [ ] `app.py` (layout, Start/Stop, metric cards, uploader, states)
- [ ] `.streamlit/config.toml` theme applied
- [ ] Verify: full UI matches `design.md`, no fabricated numbers
- [ ] Commit: `feat: build dashboard UI`

## Phase 5 — Metrics, validation, robust errors
- [ ] Confidence slider wired through
- [ ] Error banners for camera / image / model failures
- [ ] Unit tests for metrics + image_io
- [ ] Commit: `feat: add metrics and robust error handling`

## Phase 6 — End-to-end test & CPU tuning
- [ ] Manual E2E: webcam, Stop, upload, threshold change, permission denied
- [ ] Confirm FPS ≥ 5 on target laptop
- [ ] Fix real bugs only
- [ ] Commit: `test: end-to-end verification and CPU tuning`

## Phase 7 — README & release prep
- [ ] `README.md` (overview, features, screenshots, setup, troubleshooting, limitations)
- [ ] Screenshots in `assets/screenshots/` (no private footage)
- [ ] Verify `.gitignore` excludes weights
- [ ] Commit: `docs: add README and release notes`