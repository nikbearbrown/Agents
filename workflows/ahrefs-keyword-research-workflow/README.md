# Ahrefs Keyword Research Workflow

This folder contains the **Ahrefs Keyword Research Workflow** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `code`, `httpRequest`, `lmChatGoogleGemini`, `memoryBufferWindow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ahrefs-keyword-research-workflow.json`](ahrefs-keyword-research-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Keyword Data Response Formatter | `agent` | Inspect parameters |
| Keyword Query Extraction & Cleaning Agent | `agent` | Inspect parameters |
| Extract Main Keyword & 10 related Keyword data | `code` | Inspect parameters |
| Aggregate Keyword Data | `aggregate` | Inspect parameters |
| Ahrefs Keyword API Request | `httpRequest` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Aggregate Keyword Data → Keyword Data Response Formatter (`main`, output 0, input 0)
- Google Gemini Chat Model → Keyword Query Extraction & Cleaning Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model1 → Keyword Data Response Formatter (`ai_languageModel`, output 0, input 0)
- Ahrefs Keyword API Request → Extract Main Keyword & 10 related Keyword data (`main`, output 0, input 0)
- When chat message received → Keyword Query Extraction & Cleaning Agent (`main`, output 0, input 0)
- Keyword Query Extraction & Cleaning Agent → Ahrefs Keyword API Request (`main`, output 0, input 0)
- Extract Main Keyword & 10 related Keyword data → Aggregate Keyword Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1576_Aggregate_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1576_Aggregate_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
