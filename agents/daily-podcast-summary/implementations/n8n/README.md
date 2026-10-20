# Daily Podcast Summary

This folder contains the **Daily Podcast Summary** workflow. Its executable nodes use `code`, `gmail`, `html`, `httpRequest`, `if`, `openAi`, `scheduleTrigger`, `set`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`daily-podcast-summary.json`](daily-podcast-summary.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail | `gmail` | Inspect parameters |
| TaddyTopDaily | `httpRequest` | POST |
| Genre | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Whisper Transcribe Audio | `httpRequest` | POST |
| Final Data | `set` | Inspect parameters |
| Merge Results | `code` | Inspect parameters |
| HTML | `html` | Inspect parameters |
| Summarize Podcast | `openAi` | chat |
| Schedule | `scheduleTrigger` | Inspect parameters |
| Request Audio Crop | `httpRequest` | POST |
| Get Download Link | `httpRequest` | Inspect parameters |
| Download Cut MP3 | `httpRequest` | Inspect parameters |
| Download Podcast | `httpRequest` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| If Downloads Ready | `if` | Inspect parameters |

## Connection map

- HTML → Gmail (`main`, output 0, input 0)
- Wait → Get Download Link (`main`, output 0, input 0)
- Genre → TaddyTopDaily (`main`, output 0, input 0)
- Schedule → Genre (`main`, output 0, input 0)
- Split Out → Download Podcast (`main`, output 0, input 0)
- Final Data → Merge Results (`main`, output 0, input 0)
- Merge Results → HTML (`main`, output 0, input 0)
- TaddyTopDaily → Split Out (`main`, output 0, input 0)
- Download Cut MP3 → Whisper Transcribe Audio (`main`, output 0, input 0)
- Download Podcast → Request Audio Crop (`main`, output 0, input 0)
- Get Download Link → If Downloads Ready (`main`, output 0, input 0)
- Summarize Podcast → Final Data (`main`, output 0, input 0)
- If Downloads Ready → Download Cut MP3 (`main`, output 0, input 0)
- If Downloads Ready → Wait (`main`, output 1, input 0)
- Request Audio Crop → Get Download Link (`main`, output 0, input 0)
- Whisper Transcribe Audio → Summarize Podcast (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0583_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0583_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
