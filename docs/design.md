# UI/UX Design Direction

## Palette
- Background (app): `#F7F8FA`
- Surface / card: `#FFFFFF`
- Primary text: `#20242C`
- Muted text: `#667085`
- Border: `#E4E7EC`
- Accent (primary action): `#315EFB`
- Success: `#12B76A`
- Warning: `#F79009`
- Danger: `#F04438`

## Typography
- Font stack: `"Inter", "IBM Plex Sans", -apple-system, "Segoe UI", Roboto, Arial, sans-serif`
- Sizes: H1 22px / H2 18px / body 14px / caption 12px
- Weights: 600 headings, 400 body, 500 buttons

## Spacing scale
`4 / 8 / 12 / 16 / 24 / 32 / 48` px. No arbitrary values.

## Radii & borders
- Card radius: 8px. Button radius: 6px. Input radius: 6px.
- Borders: 1px `#E4E7EC`. Shadows only on modals; cards use border, not shadow.

## Layout
- Top bar: app name (left), model status pill (right).
- Left column (≈ 2/3): live preview / uploaded image, framed with 1px border, 8px radius.
- Right column (≈ 1/3): controls + metric cards stacked.
  - Metric cards (grid 2×2): FPS, Objects, Model, Camera.
  - Controls: Start / Stop buttons (primary/neutral), confidence slider, image uploader.
- Below: detected-classes list (chips, muted style).

## Components
- **Buttons**: primary filled accent; secondary outline; disabled = `#E4E7EC` bg, muted text.
- **Metric card**: 1px border, white bg, label (caption, muted) + value (H2).
- **Status pill**: small rounded-rect, colored dot + label. States: Idle (slate), Loading (blue), Ready (green), Error (red).
- **Slider**: standard Streamlit, label above, min/max caption below.
- **File uploader**: standard Streamlit, restricted to image MIME types.
- **Empty / loading / error states**: centered, muted text, single actionable button where possible.

## Icons
Lucide icons only (via Streamlit emoji-free HTML if needed). No emoji as interface icons.

## Motion
No decorative animation. Only a subtle spinner during model load and inference.

## Accessibility
- Contrast ≥ 4.5:1 for text.
- Keyboard-reachable controls (Streamlit defaults).
- Font sizes ≥ 12px for captions, ≥ 14px for body.

## Anti-patterns (explicitly avoided)
- Gradients, neon, glassmorphism, glow.
- Oversized headings, decorative empty sections.
- Fake stats or fabricated FPS.
- Pill-shaped controls, emoji icons.