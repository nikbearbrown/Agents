# agent and appendorupdate google sheets and receive form events

This folder contains the **agent and appendorupdate google sheets and receive form events** workflow. Its executable nodes use `agent`, `code`, `formTrigger`, `gmail`, `googleSheets`, `lmChatGoogleGemini`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`agent-and-appendorupdate-google-sheets-and-receive-form-events.json`](agent-and-appendorupdate-google-sheets-and-receive-form-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `googleSheetsOAuth2Api`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Code | `code` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| Append or update row in sheet | `googleSheets` | appendOrUpdate |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Send a message | `gmail` | Inspect parameters |
| Code1 | `code` | Inspect parameters |

## Connection map

- Code → Send a message (`main`, output 0, input 0)
- Google Gemini Chat Model1 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- AI Agent1 → Code (`main`, output 0, input 0)
- Append or update row in sheet → AI Agent1 (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- AI Agent → Code1 (`main`, output 0, input 0)
- On form submission → AI Agent (`main`, output 0, input 0)
- Code1 → Append or update row in sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/pointblank-club/n8n/blob/f6d1bbd805cdc4ba18185cfcfdd574acb08aa1f1/upload.json](https://github.com/pointblank-club/n8n/blob/f6d1bbd805cdc4ba18185cfcfdd574acb08aa1f1/upload.json). License: **Apache-2.0**; preserve [the notice](../../licenses/pointblank-club--n8n.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
