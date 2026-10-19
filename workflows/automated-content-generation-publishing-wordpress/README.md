# Automated Content Generation & Publishing - Wordpress

This folder contains the **Automated Content Generation & Publishing - Wordpress** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `manualTrigger`, `openAi`, `scheduleTrigger`, `wait`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-content-generation-publishing-wordpress.json`](automated-content-generation-publishing-wordpress.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `wordpressApi`

**Entry nodes:** 1. Auto Start, 2. When clicking ‘Test workflow’, 3. Schedule Your Posts

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create posts on Wordpress | `wordpress` | Inspect parameters |
| Processing Delay | `code` | Inspect parameters |
| Random Wait | `wait` | Inspect parameters |
| Save to Sheet | `googleSheets` | append |
| 1. Auto Start | `scheduleTrigger` | Inspect parameters |
| 2. When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| 3. Schedule Your Posts | `scheduleTrigger` | Inspect parameters |
| Automated Image Retrieval from Pexels | `httpRequest` | Inspect parameters |
| Generate AI Content | `openAi` | Inspect parameters |

## Connection map

- Random Wait → Generate AI Content (`main`, output 0, input 0)
- Save to Sheet → Automated Image Retrieval from Pexels (`main`, output 0, input 0)
- Processing Delay → Random Wait (`main`, output 0, input 0)
- Generate AI Content → Save to Sheet (`main`, output 0, input 0)
- 3. Schedule Your Posts → Processing Delay (`main`, output 0, input 0)
- Automated Image Retrieval from Pexels → Create posts on Wordpress (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1771_Wait_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1771_Wait_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
