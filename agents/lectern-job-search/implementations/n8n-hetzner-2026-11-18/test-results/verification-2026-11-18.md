# Verification: 2026-11-18

All five exact publication workflows passed synthetic fixtures in n8n 1.113.3 on Node 24.17.0. [Hash-pinned receipt](verification-2026-11-18.json) · [Full output](headless-2026-11-18.txt). The test runner was unchanged. macOS sandbox denied all network access; a disposable n8n profile and temporary HOME were used, with no inherited credentials and writes confined to the test directory.

## Changes from preserved original
- Collect: six watched boards instead of sixteen; expanded synthetic fixtures. This intentionally narrower snapshot is additive, not a silent replacement.
- Filter: embedded rules v0.6.5, country and K-12 gates, accent-aware location handling, expanded fixtures.
- Delta: updated synthetic fixtures for the newer filtering rules.
- Post and Daily: same source bytes as the original prior to publication metadata sanitization.

All workflows remain inactive. Empty metadata/pinned-data fields and the placeholder Discord credential binding were removed, then the exact sanitized artifacts were retested.

## Limits
No live API, Discord delivery, external credentials, or performance test was run. Python parity is against existing expected fixture outputs, not a fresh Python execution. Historical parity reports are preserved as historical reports, not claimed as today's tests. SmartRecruiters live collection remains unsupported. The n8n filter does not implement Python engine/consulting/speakers/federal508 rules.

This revision shares workflow IDs with the original. Import only one revision into a disposable profile; importing it into an existing profile may overwrite workflows with those IDs. The original package and migration hashes remain intact. This is one Lectern agent family with a versioned implementation, not five additional families.
