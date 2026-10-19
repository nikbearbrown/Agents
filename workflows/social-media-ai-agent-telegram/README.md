# Social Media AI Agent - Telegram

This folder contains the **Social Media AI Agent - Telegram** workflow. Its executable nodes use `airtable`, `code`, `filter`, `httpRequest`, `linkedIn`, `markdown`, `merge`, `noOp`, `openAi`, `scheduleTrigger`, `telegram`, `twitter`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`social-media-ai-agent-telegram.json`](social-media-ai-agent-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `linkedInOAuth2Api`, `openAiApi`, `telegramApi`, `twitterOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Crawl HN Home | `httpRequest` | Inspect parameters |
| Extract Meta | `code` | Inspect parameters |
| Filter Unposted Items | `code` | Inspect parameters |
| Visit GH Page | `httpRequest` | Inspect parameters |
| Convert HTML To Markdown | `markdown` | Inspect parameters |
| Filter Errored | `filter` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Update X Status | `airtable` | update |
| LinkedIn | `linkedIn` | Inspect parameters |
| Update L Status | `airtable` | update |
| Search Item | `airtable` | search |
| Create Item | `airtable` | create |
| X | `twitter` | Inspect parameters |
| Validate Generate Content | `code` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Generate Content | `openAi` | Inspect parameters |
| Ping Me | `telegram` | Inspect parameters |
| Wait for 5 mins before posting | `wait` | Inspect parameters |

## Connection map

- X → Update X Status (`main`, output 0, input 0)
- Merge → Filter Unposted Items (`main`, output 0, input 0)
- Ping Me → Wait for 5 mins before posting (`main`, output 0, input 0)
- LinkedIn → Update L Status (`main`, output 0, input 0)
- Create Item → Ping Me (`main`, output 0, input 0)
- Search Item → Merge (`main`, output 0, input 0)
- Extract Meta → Search Item (`main`, output 0, input 0)
- Extract Meta → Merge (`main`, output 0, input 1)
- Crawl HN Home → Extract Meta (`main`, output 0, input 0)
- Visit GH Page → Convert HTML To Markdown (`main`, output 0, input 0)
- Filter Errored → Create Item (`main`, output 0, input 0)
- Update L Status → No Operation, do nothing (`main`, output 0, input 0)
- Update X Status → No Operation, do nothing (`main`, output 0, input 0)
- Generate Content → Validate Generate Content (`main`, output 0, input 0)
- Schedule Trigger → Crawl HN Home (`main`, output 0, input 0)
- Filter Unposted Items → Visit GH Page (`main`, output 0, input 0)
- Convert HTML To Markdown → Generate Content (`main`, output 0, input 0)
- Validate Generate Content → Filter Errored (`main`, output 0, input 0)
- Wait for 5 mins before posting → X (`main`, output 0, input 0)
- Wait for 5 mins before posting → LinkedIn (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1280_Linkedin_Telegram_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1280_Linkedin_Telegram_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
