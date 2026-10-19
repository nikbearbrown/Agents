# piepdrive-test

This folder contains the **piepdrive-test** workflow. Its executable nodes use `code`, `httpRequest`, `markdown`, `openAi`, `pipedrive`, `pipedriveTrigger`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`enrich-pipedrive-s-organization-data-with-gpt-4o-when-an-organization-is-created-in-pipedrive.json`](enrich-pipedrive-s-organization-data-with-gpt-4o-when-an-organization-is-created-in-pipedrive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `pipedriveApi`, `slackOAuth2Api`

**Entry nodes:** Pipedrive Trigger - An Organization is created

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Pipedrive Trigger - An Organization is created | `pipedriveTrigger` | Inspect parameters |
| Pipedrive - Create a Note with OpenAI output | `pipedrive` | note |
| Code - Markdown to Slack Markdown | `code` | Inspect parameters |
| Scrapingbee - Get Organization's URL content | `httpRequest` | Inspect parameters |
| HTML To Markdown | `markdown` | Inspect parameters |
| Slack - Notify  | `slack` | Inspect parameters |
| OpenAI - Message GPT-4o with Scraped Data | `openAi` | Inspect parameters |

## Connection map

- HTML To Markdown → Code - Markdown to Slack Markdown (`main`, output 0, input 0)
- Code - Markdown to Slack Markdown → Slack - Notify  (`main`, output 0, input 0)
- OpenAI - Message GPT-4o with Scraped Data → Pipedrive - Create a Note with OpenAI output (`main`, output 0, input 0)
- Pipedrive - Create a Note with OpenAI output → HTML To Markdown (`main`, output 0, input 0)
- Scrapingbee - Get Organization's URL content → OpenAI - Message GPT-4o with Scraped Data (`main`, output 0, input 0)
- Pipedrive Trigger - An Organization is created → Scrapingbee - Get Organization's URL content (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1435_Code_Slack_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1435_Code_Slack_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
