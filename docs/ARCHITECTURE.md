# Burmese → Ukrainian — Service Architecture

## Runtime model

The public service is a static Vite application. No server, database, account or analytics layer is required for ordinary conversion.

## Pipeline

Burmese Unicode → normalization → grapheme/syllable segmentation → Burmese structural analysis → phonological / IPA derivation → Ukrainian target mapping → practical Ukrainian output → explanation + provenance → UI

The application must never use Russian transcription as a runtime intermediate.

## Source-of-truth rule

Research CSV/JSON files remain authoritative. Build scripts generate JavaScript data modules from those sources. Generated files are not hand-edited.

## Application contract

The UI consumes a stable ConversionResult shape:

input, normalized, output, ipa, syllables[], status, issues[], explanations[], provenance[]

A future Python/API consumer can use the same conceptual contract.

## Two-page routing

- / — service;
- /system.html — explanation of the author's system.

## Security boundary

User-controlled text is rendered with textContent; no innerHTML; no runtime network calls; no analytics; no user-text upload. Production CSP restricts scripts/styles to same-origin assets.

## Dependency policy

Keep the browser dependency footprint small. Linguistic data belongs in repository data files and generated modules, not opaque third-party services.
