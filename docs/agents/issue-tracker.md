# Issue tracker configuration

- **Canonical tracker:** GitHub Issues in ClippyFirst/Burmese-Ukrainian-Phonetic-System-.
- **Current integration:** use the connected GitHub repository integration when available. Do not assume a local gh CLI is installed or authenticated.
- **Pull requests as intake:** disabled. PRs are delivery/review objects; issues are the canonical request, blocker and research-decision records.
- **Status vocabulary:** DONE_VERIFIED, PARTIAL, TODO, BLOCKED, DEFERRED, as defined by AGENTS.md and the master handoff.
- **Triage labels:** do not invent a parallel label vocabulary. Inspect current repository labels before any label mutation; if no matching label exists, leave labels unchanged and record status in the issue body.
- **Issue discipline:** search for an existing issue before creating one; link the originating issue from implementation PRs; distinguish source-backed facts, project decisions, hypotheses and blockers.
- **Authorship:** preserve human-authored issue/PR template sections and do not imply that agent-generated text was written by the repository owner.
- **Research issues:** include source URL, exact source locator/version, profile, data provenance, license status and acceptance criteria. MLCTS data, IPA dictionaries, audio transcripts and independently adjudicated IPA are different evidence types.
