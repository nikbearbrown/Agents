# receive typeform events and google cloud natural language and notion

This folder contains the **receive typeform events and google cloud natural language and notion** workflow. Its executable nodes use `googleCloudNaturalLanguage`, `if`, `notion`, `slack`, `trello`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-typeform-events-and-google-cloud-natural-language-and-notion.json`](receive-typeform-events-and-google-cloud-natural-language-and-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCloudNaturalLanguageOAuth2Api`, `notionApi`, `slackApi`, `trelloApi`, `typeformApi`

**Entry nodes:** Typeform Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Typeform Trigger | `typeformTrigger` | Inspect parameters |
| Google Cloud Natural Language | `googleCloudNaturalLanguage` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Notion | `notion` | databasePage |
| Slack | `slack` | Inspect parameters |
| Trello | `trello` | Inspect parameters |

## Connection map

- IF → Notion (`main`, output 0, input 0)
- IF → Trello (`main`, output 1, input 0)
- Notion → Slack (`main`, output 0, input 0)
- Typeform Trigger → Google Cloud Natural Language (`main`, output 0, input 0)
- Google Cloud Natural Language → IF (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/1298_Trello_Googlecloudnaturallanguage_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/1298_Trello_Googlecloudnaturallanguage_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
