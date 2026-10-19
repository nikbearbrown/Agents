# Linkedin Automation

This folder contains the **Linkedin Automation** workflow. Its executable nodes use `airtable`, `code`, `filter`, `httpRequest`, `if`, `linkedIn`, `scheduleTrigger`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-automation.json`](linkedin-automation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `linkedInOAuth2Api`, `telegramApi`

**Entry nodes:** Morning  9 Clock

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get List of records used | `airtable` | search |
| Update the used node | `airtable` | create |
| map used articls ids | `code` | Inspect parameters |
| filter only unused Ids | `filter` | Inspect parameters |
| get random tags | `code` | Inspect parameters |
| sent the status | `telegram` | Inspect parameters |
| Morning  9 Clock | `scheduleTrigger` | Inspect parameters |
| fetch article ids from tag | `httpRequest` | Inspect parameters |
| Fetch Medium post using Article Id | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| make Linkedin post | `linkedIn` | Inspect parameters |
| Fetch Medium post content | `httpRequest` | Inspect parameters |
| download image for post | `httpRequest` | Inspect parameters |

## Connection map

- If → Fetch Medium post content (`main`, output 0, input 0)
- If → get random tags (`main`, output 1, input 0)
- get random tags → Get List of records used (`main`, output 0, input 0)
- Morning  9 Clock → get random tags (`main`, output 0, input 0)
- make Linkedin post → Update the used node (`main`, output 0, input 0)
- Update the used node → sent the status (`main`, output 0, input 0)
- map used articls ids → fetch article ids from tag (`main`, output 0, input 0)
- filter only unused Ids → Fetch Medium post using Article Id (`main`, output 0, input 0)
- download image for post → make Linkedin post (`main`, output 0, input 0)
- Get List of records used → map used articls ids (`main`, output 0, input 0)
- Fetch Medium post content → download image for post (`main`, output 0, input 0)
- fetch article ids from tag → filter only unused Ids (`main`, output 0, input 0)
- Fetch Medium post using Article Id → If (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/2024_Linkedin_Telegram_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/2024_Linkedin_Telegram_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
