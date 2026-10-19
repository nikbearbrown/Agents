# Opportunity Matcher v2

This folder contains the **Opportunity Matcher v2** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `if`, `scheduleTrigger`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`opportunity-matcher.json`](opportunity-matcher.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Weekly schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Weekly schedule | `scheduleTrigger` | Inspect parameters |
| Fetch Anthropic board | `httpRequest` | Inspect parameters |
| Fetch Figma board | `httpRequest` | Inspect parameters |
| Normalize records | `code` | Inspect parameters |
| Score and route (the intelligence) | `code` | Inspect parameters |
| Decision = PURSUE or NETWORK? | `if` | Inspect parameters |
| Generate briefs | `code` | Inspect parameters |
| Save digest files | `writeBinaryFile` | Inspect parameters |
| Email the digest | `emailSend` | Inspect parameters |
| Log the failure | `code` | Inspect parameters |

## Connection map

- Decision = PURSUE or NETWORK? → Generate briefs (`main`, output 0, input 0)
- Decision = PURSUE or NETWORK? → Email the digest (`main`, output 1, input 0)
- Fetch Anthropic board → Normalize records (`main`, output 0, input 0)
- Fetch Figma board → Normalize records (`main`, output 0, input 0)
- Generate briefs → Save digest files (`main`, output 0, input 0)
- Normalize records → Score and route (the intelligence) (`main`, output 0, input 0)
- Score and route (the intelligence) → Decision = PURSUE or NETWORK? (`main`, output 0, input 0)
- Weekly schedule → Fetch Anthropic board (`main`, output 0, input 0)
- Weekly schedule → Fetch Figma board (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
