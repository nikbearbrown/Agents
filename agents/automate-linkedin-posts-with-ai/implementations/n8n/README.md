# Automate LinkedIn Posts with AI

This folder contains the **Automate LinkedIn Posts with AI** workflow. Its executable nodes use `aggregate`, `httpRequest`, `linkedIn`, `merge`, `notion`, `openAi`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-linkedin-posts-with-ai.json`](automate-linkedin-posts-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `linkedInOAuth2Api`, `notionApi`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Set post status to "Done" | `notion` | databasePage / update |
| Post on LinkedIn | `linkedIn` | Inspect parameters |
| Combine text+image | `merge` | Inspect parameters |
| Fetch image from post | `httpRequest` | Inspect parameters |
| Reformat Post Text | `openAi` | assistant |
| get all content from post page | `notion` | block / getAll |
| Pull together all text blocks + image | `aggregate` | Inspect parameters |
| query entries from Notion table for today | `notion` | databasePage / getAll |

## Connection map

- Post on LinkedIn → Set post status to "Done" (`main`, output 0, input 0)
- Schedule Trigger → query entries from Notion table for today (`main`, output 0, input 0)
- Combine text+image → Post on LinkedIn (`main`, output 0, input 0)
- Reformat Post Text → Combine text+image (`main`, output 0, input 0)
- Fetch image from post → Combine text+image (`main`, output 0, input 1)
- get all content from post page → Pull together all text blocks + image (`main`, output 0, input 0)
- Pull together all text blocks + image → Fetch image from post (`main`, output 0, input 0)
- Pull together all text blocks + image → Reformat Post Text (`main`, output 0, input 0)
- query entries from Notion table for today → get all content from post page (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1330_Linkedin_Schedule_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1330_Linkedin_Schedule_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
