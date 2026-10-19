# Hugging Face  to Notion

This folder contains the **Hugging Face  to Notion** workflow. Its executable nodes use `html`, `httpRequest`, `if`, `notion`, `openAi`, `scheduleTrigger`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hugging-face-to-notion.json`](hugging-face-to-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Request Hugging Face Paper | `httpRequest` | Inspect parameters |
| Extract Hugging Face Paper | `html` | extractHtmlContent |
| Check Paper URL Existed | `notion` | databasePage / getAll |
| Request Hugging Face Paper Detail | `httpRequest` | Inspect parameters |
| OpenAI Analysis Abstract | `openAi` | Inspect parameters |
| Store Abstract Notion | `notion` | databasePage |
| Extract Hugging Face Paper Abstract | `html` | extractHtmlContent |

## Connection map

- If → Request Hugging Face Paper Detail (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- Split Out → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Check Paper URL Existed (`main`, output 1, input 0)
- Schedule Trigger → Request Hugging Face Paper (`main`, output 0, input 0)
- Store Abstract Notion → Loop Over Items (`main`, output 0, input 0)
- Check Paper URL Existed → If (`main`, output 0, input 0)
- OpenAI Analysis Abstract → Store Abstract Notion (`main`, output 0, input 0)
- Extract Hugging Face Paper → Split Out (`main`, output 0, input 0)
- Request Hugging Face Paper → Extract Hugging Face Paper (`main`, output 0, input 0)
- Request Hugging Face Paper Detail → Extract Hugging Face Paper Abstract (`main`, output 0, input 0)
- Extract Hugging Face Paper Abstract → OpenAI Analysis Abstract (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1451_Splitout_Schedule_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1451_Splitout_Schedule_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
