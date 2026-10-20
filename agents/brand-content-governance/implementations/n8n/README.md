# Madison_Content_Agent_MVP copy 1

This folder contains the **Madison_Content_Agent_MVP copy 1** workflow. Its executable nodes use `code`, `convertToFile`, `filter`, `httpRequest`, `openAi`, `respondToWebhook`, `scheduleTrigger`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`brand-content-governance.json`](brand-content-governance.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Webhook, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Convert to File | `convertToFile` | Inspect parameters |
| Prompt | `code` | Inspect parameters |
| Quality check | `code` | Inspect parameters |
| Generation | `openAi` | Inspect parameters |
| Convert to File1 | `convertToFile` | Inspect parameters |
| Respond to Webhook1 | `respondToWebhook` | Inspect parameters |
| Visual Concepts | `code` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| brand voice | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Convert to File4 | `convertToFile` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Convert to File5 | `convertToFile` | Inspect parameters |
| Compute Engagement | `code` | Inspect parameters |
| Filter Flagged | `code` | Inspect parameters |
| Filter Unflagged | `code` | Inspect parameters |
| Scoring Logic | `code` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Filter1 | `filter` | Inspect parameters |
| Discord1 | `httpRequest` | POST |
| Discord2 | `httpRequest` | POST |
| Discord3 | `httpRequest` | POST |
| Discord4 | `httpRequest` | POST |

## Connection map

- Webhook → brand voice (`main`, output 0, input 0)
- Convert to File → Discord3 (`main`, output 0, input 0)
- Prompt → Generation (`main`, output 0, input 0)
- Quality check → Scoring Logic (`main`, output 0, input 0)
- Generation → Quality check (`main`, output 0, input 0)
- Convert to File1 → Discord4 (`main`, output 0, input 0)
- Visual Concepts → Convert to File (`main`, output 0, input 0)
- brand voice → Prompt (`main`, output 0, input 0)
- Schedule Trigger → HTTP Request (`main`, output 0, input 0)
- HTTP Request → Split Out (`main`, output 0, input 0)
- Edit Fields → Compute Engagement (`main`, output 0, input 0)
- Split Out → Edit Fields (`main`, output 0, input 0)
- Convert to File4 → Discord1 (`main`, output 0, input 0)
- Compute Engagement → Filter Flagged (`main`, output 0, input 0)
- Compute Engagement → Filter Unflagged (`main`, output 0, input 0)
- Filter Flagged → Convert to File5 (`main`, output 0, input 0)
- Filter Unflagged → Convert to File4 (`main`, output 0, input 0)
- Scoring Logic → Filter (`main`, output 0, input 0)
- Scoring Logic → Filter1 (`main`, output 0, input 0)
- Filter → Visual Concepts (`main`, output 0, input 0)
- Filter1 → Convert to File1 (`main`, output 0, input 0)
- Convert to File5 → Discord2 (`main`, output 0, input 0)
- Discord3 → Respond to Webhook (`main`, output 0, input 0)
- Discord4 → Respond to Webhook1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
