# Burmese → Ukrainian Converter — Product & Technical Design Specification

**Date:** 2026-10-06  
**Status:** Implementation baseline  
**Reference:** ClippyFirst/chinese-for-ukrainians

## Problem

A Ukrainian reader needs a practical way to read Burmese text in Ukrainian Cyrillic, but no authoritative pre-existing Ukrainian Burmese system was established in the repository research. Therefore the service must expose the author's evidence-gated system rather than disguise it as an official standard.

## Product

Two-page static web application:
1. service;
2. explanation of the author's system.

## Core principle

The public result is not a direct character substitution and not a translation.

Burmese orthography → structural analysis → phonological/phonetic interpretation → IPA → Ukrainian target-language policy → practical Ukrainian output

## Visual principle

Use the Chinese project's functional reference-tool language: typography, grid, whitespace and rules.

Replace its Chinese identity with a restrained Myanmar national palette: yellow / green / red / white.

No gradients, AI imagery, decorative flags, chat bubbles or generic SaaS cards.

## Product honesty

The interface must say when a result is established, supported, analysis-dependent, uncertain or not established.

The service may return a partial result rather than fabricate confidence.

## Handoff

The implementation should preserve the repository's research engine as the conceptual source of truth and add only the browser adapter, generated data and public presentation layer.
