# Engineering Rules — Constitution

## Scope
- Build only approved features. No speculative abstractions.
- Follow the phases in `tasks.md`; do not skip ahead.

## Code
- PEP 8, meaningful names, small focused functions.
- One responsibility per module: UI, inference, camera, utils separated.
- No duplicated logic; reuse existing helpers.
- No hardcoded secrets or machine-specific absolute paths.
- No undefined imports or dead functions.

## Resources
- Always release the webcam (Stop, exception, and app exit paths).
- Never open multiple camera sessions.
- Cache the model; never reload per frame.
- Do not block the UI during inference; keep per-rerun work minimal.

## Errors
- Handle: missing camera, permission denied, undecodable image, missing weights, inference exceptions.
- Show user-friendly messages; log technical detail.
- Never crash silently.

## Dependencies
- Justify each new dependency; prefer stdlib/existing.
- Pin versions in `requirements.txt` (constraints or `==`).
- Verify license compatibility before any commercial claim.

## Repo hygiene
- Keep `.gitignore` current (venv, `__pycache__`, `.pt` weights, `.streamlit` secrets if any).
- Never commit venv, caches, private footage, or large weights.
- Do not commit `.env`; `.env.example` only if genuinely needed.

## Testing
- Test real behavior, not assumptions.
- Unit tests for pure logic: detector post-processing, annotator, FPS counter, image I/O.
- Manual verification for webcam behavior and UI states.

## Documentation
- Update `architecture.md`, `tasks.md`, `memory.md` whenever behavior or structure changes.
- `memory.md` reflects actual commands run and real outcomes only.