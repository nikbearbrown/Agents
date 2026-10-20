# HN Who is Hiring Scrape

This folder contains the **HN Who is Hiring Scrape** workflow. Its executable nodes use `airtable`, `chainLlm`, `code`, `filter`, `httpRequest`, `limit`, `lmChatOpenAi`, `manualTrigger`, `outputParserStructured`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hn-who-is-hiring-scrape.json`](hn-who-is-hiring-scrape.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Search for Who is hiring posts | `httpRequest` | POST |
| Get relevant data | `set` | Inspect parameters |
| Get latest post | `filter` | Inspect parameters |
| Split out children (jobs) | `splitOut` | Inspect parameters |
| Trun into structured data | `chainLlm` | Inspect parameters |
| Extract text | `set` | Inspect parameters |
| Clean text | `code` | Inspect parameters |
| Limit for testing (optional) | `limit` | Inspect parameters |
| Write results to airtable | `airtable` | create |
| HI API: Get the individual job post | `httpRequest` | Inspect parameters |
| HN API: Get Main Post | `httpRequest` | Inspect parameters |

## Connection map

- Split Out → Get relevant data (`main`, output 0, input 0)
- Clean text → Limit for testing (optional) (`main`, output 0, input 0)
- Extract text → Clean text (`main`, output 0, input 0)
- Get latest post → HN API: Get Main Post (`main`, output 0, input 0)
- Get relevant data → Get latest post (`main`, output 0, input 0)
- OpenAI Chat Model → Trun into structured data (`ai_languageModel`, output 0, input 0)
- HN API: Get Main Post → Split out children (jobs) (`main`, output 0, input 0)
- Structured Output Parser → Trun into structured data (`ai_outputParser`, output 0, input 0)
- Split out children (jobs) → HI API: Get the individual job post (`main`, output 0, input 0)
- Trun into structured data → Write results to airtable (`main`, output 0, input 0)
- Limit for testing (optional) → Trun into structured data (`main`, output 0, input 0)
- Search for Who is hiring posts → Split Out (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Search for Who is hiring posts (`main`, output 0, input 0)
- HI API: Get the individual job post → Extract text (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1880_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1880_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
