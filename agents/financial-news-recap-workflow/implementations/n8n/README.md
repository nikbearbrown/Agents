# Financial News Recap Workflow

This folder contains the **Financial News Recap Workflow** workflow. Its executable nodes use `agent`, `html`, `httpRequest`, `lmChatGoogleGemini`, `microsoftOutlook`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`financial-news-recap-workflow.json`](financial-news-recap-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `microsoftOutlookOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract specific content | `html` | extractHtmlContent |
| Get financial news online | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Gather the elements | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Send the summary by e-mail | `microsoftOutlook` | Inspect parameters |

## Connection map

- AI Agent → Send the summary by e-mail (`main`, output 0, input 0)
- Schedule Trigger → Get financial news online (`main`, output 0, input 0)
- Gather the elements → AI Agent (`main`, output 0, input 0)
- Extract specific content → Gather the elements (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Get financial news online → Extract specific content (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/2045_Schedule_HTTP_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/2045_Schedule_HTTP_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
