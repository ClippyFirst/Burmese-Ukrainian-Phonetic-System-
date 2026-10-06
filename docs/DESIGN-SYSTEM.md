# Burmese → Ukrainian — Design System

## Design direction

The interface is a **linguistic reference instrument**: restrained, typographic, information-dense but calm. The Chinese project is the structural reference; the Burmese project has its own visual identity.

## National identity

The Myanmar national flag uses horizontal yellow, green and red fields with a white star. The interface derives a restrained accent palette from these colors rather than reproducing the flag as decoration.

| Role | Value | Use |
|---|---|---|
| Paper | #F5F3EC | page background |
| Surface | #FFFFFF | work surfaces |
| Soft surface | #FAF9F4 | input/secondary surfaces |
| Ink | #151719 | primary text |
| Muted | #686B6F | secondary text |
| Line | #D8D6CF | separators |
| Strong line | #B9B7AF | borders |
| Myanmar yellow | #F2D12E | identity / small markers |
| Myanmar green | #3F7D3A | secondary identity / success |
| Myanmar red | #D62828 | primary action / warning accent |
| Red soft | #FBECEC | warning surface |
| Green soft | #EEF6EE | established status |
| Yellow soft | #FFF9DD | analysis-dependent status |

Color is never the only carrier of meaning.

## Typography

- UI: system sans stack with Cyrillic and Myanmar fallbacks.
- Burmese: Myanmar-compatible sans fallback.
- Main title: restrained serif/system serif.
- IPA: readable sans with broad Unicode coverage.
- Codepoints/rule IDs: monospace.

Avoid decorative display fonts and excessive uppercase.

## Layout

The service follows the Chinese project's information hierarchy:
1. bilingual brand line;
2. restrained hero;
3. input workspace;
4. compact controls;
5. results;
6. feedback/provenance;
7. footer.

The scientific page uses the same header/footer but changes the main content to a long-form methodological layout.

## Main service

Burmese input is immediately visible. Ukrainian output is the primary result. IPA and structural analysis are supporting evidence.

## Components

### Status

Compact textual labels:
ESTABLISHED · WELL_SUPPORTED · ANALYSIS_DEPENDENT · CONTEXT_DEPENDENT · UNCERTAIN · NOT_ESTABLISHED · UNSUPPORTED

### Result panel

Each result contains:
- index;
- title;
- short methodological description;
- copy action;
- output;
- status/provenance.

### Rule explanation

A compact disclosure may show:
- IPA input;
- Ukrainian candidate;
- rule ID;
- reason;
- evidence IDs.

## Responsive behavior

Desktop: max width ~1120–1160px.

Tablet: controls wrap.

Mobile:
- 11–16px side margins;
- one-column results;
- no horizontal scrolling;
- large touch targets;
- scientific tables become stacked/scrollable only when unavoidable.

## Accessibility

Semantic landmarks, native buttons, visible focus, aria-live conversion status, no color-only state, reduced-motion support, readable zoom and an appropriate Myanmar fallback stack are required.

## Design QA

1. Burmese input is discoverable immediately.
2. The Ukrainian result is visually primary.
3. IPA is clearly identified as phonetic evidence, not translation.
4. Uncertainty is visible without looking like an application failure.
5. National colors identify the project without becoming decorative noise.
6. Scientific page reads like a reference document.
