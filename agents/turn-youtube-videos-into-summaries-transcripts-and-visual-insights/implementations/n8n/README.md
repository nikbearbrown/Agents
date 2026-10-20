# Turn YouTube Videos into Summaries, Transcripts, and Visual Insights

This folder contains the **Turn YouTube Videos into Summaries, Transcripts, and Visual Insights** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`turn-youtube-videos-into-summaries-transcripts-and-visual-insights.json`](turn-youtube-videos-into-summaries-transcripts-and-visual-insights.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set: Define Initial Variables | `set` | Inspect parameters |
| Switch: What kind of question do we want to ask? | `switch` | Inspect parameters |
| Set: Scene Prompt | `set` | Inspect parameters |
| Set: Summarize Prompt | `set` | Inspect parameters |
| Set: Transcript Prompt | `set` | Inspect parameters |
| Set: Fallback | `set` | Inspect parameters |
| Set: Transcript with Timestamps Prompt | `set` | Inspect parameters |
| Set: Scene Clips | `set` | Inspect parameters |
| Set Fields: Define Outcome | `set` | Inspect parameters |
| HTTP Request to Google | `httpRequest` | POST |
| Set: Merged Values | `set` | Inspect parameters |
| If: Was an error detected? | `if` | Inspect parameters |
| Code: Merge data from prior nodes with HTTP Output | `code` | Inspect parameters |

## Connection map

- Set: Fallback → Set: Merged Values (`main`, output 0, input 0)
- Set: Scene Clips → Set: Merged Values (`main`, output 0, input 0)
- Set: Scene Prompt → Set: Merged Values (`main`, output 0, input 0)
- Set: Merged Values → HTTP Request to Google (`main`, output 0, input 0)
- Set: Summarize Prompt → Set: Merged Values (`main`, output 0, input 0)
- HTTP Request to Google → Code: Merge data from prior nodes with HTTP Output (`main`, output 0, input 0)
- HTTP Request to Google → If: Was an error detected? (`main`, output 0, input 0)
- Set: Transcript Prompt → Set: Merged Values (`main`, output 0, input 0)
- Set: Define Initial Variables → Switch: What kind of question do we want to ask? (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set: Define Initial Variables (`main`, output 0, input 0)
- Set: Transcript with Timestamps Prompt → Set: Merged Values (`main`, output 0, input 0)
- Switch: What kind of question do we want to ask? → Set: Transcript Prompt (`main`, output 0, input 0)
- Switch: What kind of question do we want to ask? → Set: Transcript with Timestamps Prompt (`main`, output 1, input 0)
- Switch: What kind of question do we want to ask? → Set: Summarize Prompt (`main`, output 2, input 0)
- Switch: What kind of question do we want to ask? → Set: Scene Prompt (`main`, output 3, input 0)
- Switch: What kind of question do we want to ask? → Set: Scene Clips (`main`, output 4, input 0)
- Switch: What kind of question do we want to ask? → Set: Fallback (`main`, output 5, input 0)
- Code: Merge data from prior nodes with HTTP Output → Set Fields: Define Outcome (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2002_Manual_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/2002_Manual_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
