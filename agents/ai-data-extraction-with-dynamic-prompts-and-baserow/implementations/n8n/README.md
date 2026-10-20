# ai data extraction with dynamic prompts and baserow

This folder contains the **ai data extraction with dynamic prompts and baserow** workflow. Its executable nodes use `airtable`, `chainLlm`, `code`, `extractFromFile`, `filter`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `noOp`, `set`, `splitInBatches`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-data-extraction-with-dynamic-prompts-and-baserow.json`](ai-data-extraction-with-dynamic-prompts-and-baserow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`

**Entry nodes:** Airtable Webhook, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Event Type | `switch` | Inspect parameters |
| Get Prompt Fields | `code` | Inspect parameters |
| Get File Data | `httpRequest` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| Get Result | `set` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Row Reference | `noOp` | Inspect parameters |
| Generate Field Value | `chainLlm` | Inspect parameters |
| Fields to Update | `code` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Row Ref | `noOp` | Inspect parameters |
| Get File Data1 | `httpRequest` | Inspect parameters |
| Extract from File1 | `extractFromFile` | pdf |
| Get Result1 | `set` | Inspect parameters |
| Generate Field Value1 | `chainLlm` | Inspect parameters |
| Filter Valid Rows | `filter` | Inspect parameters |
| Filter Valid Fields | `filter` | Inspect parameters |
| Event Ref | `noOp` | Inspect parameters |
| Event Ref1 | `noOp` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Get Webhook Payload | `httpRequest` | Inspect parameters |
| Parse Event | `code` | Inspect parameters |
| Get Table Schema | `airtable` | base / getSchema |
| Fetch Records | `airtable` | search |
| Update Row | `airtable` | update |
| Get Row | `airtable` | Inspect parameters |
| Add Row ID to Payload | `set` | Inspect parameters |
| Update Record | `airtable` | update |
| Airtable Webhook | `webhook` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set Airtable Vars | `set` | Inspect parameters |
| Get Table Schema1 | `airtable` | base / getSchema |
| Get "Input" Field | `set` | Inspect parameters |
| RecordsChanged Webhook | `httpRequest` | POST |
| FieldsChanged Webhook | `httpRequest` | POST |

## Connection map

- Get Row → Filter Valid Rows (`main`, output 0, input 0)
- Row Ref → Get File Data1 (`main`, output 0, input 0)
- Event Ref → Filter Valid Fields (`main`, output 0, input 0)
- Event Ref1 → Get Row (`main`, output 0, input 0)
- Event Type → Event Ref1 (`main`, output 0, input 0)
- Event Type → Event Ref (`main`, output 1, input 0)
- Event Type → Event Ref (`main`, output 2, input 0)
- Get Result → Update Row (`main`, output 0, input 0)
- Update Row → Loop Over Items (`main`, output 0, input 0)
- Get Result1 → Add Row ID to Payload (`main`, output 0, input 0)
- Parse Event → Event Type (`main`, output 0, input 0)
- Fetch Records → Loop Over Items (`main`, output 0, input 0)
- Get File Data → Extract from File (`main`, output 0, input 0)
- Row Reference → Get File Data (`main`, output 0, input 0)
- Update Record → Loop Over Items1 (`main`, output 0, input 0)
- Get File Data1 → Extract from File1 (`main`, output 0, input 0)
- Loop Over Items → Row Reference (`main`, output 1, input 0)
- Airtable Webhook → Get Table Schema (`main`, output 0, input 0)
- Fields to Update → Generate Field Value1 (`main`, output 0, input 0)
- Get Table Schema → Get Prompt Fields (`main`, output 0, input 0)
- Loop Over Items1 → Row Ref (`main`, output 1, input 0)
- Extract from File → Generate Field Value (`main`, output 0, input 0)
- Filter Valid Rows → Loop Over Items1 (`main`, output 0, input 0)
- Get "Input" Field → RecordsChanged Webhook (`main`, output 0, input 0)
- Get Prompt Fields → Get Webhook Payload (`main`, output 0, input 0)
- Get Table Schema1 → Get "Input" Field (`main`, output 0, input 0)
- OpenAI Chat Model → Generate Field Value1 (`ai_languageModel`, output 0, input 0)
- Set Airtable Vars → Get Table Schema1 (`main`, output 0, input 0)
- Set Airtable Vars → FieldsChanged Webhook (`main`, output 0, input 0)
- Extract from File1 → Fields to Update (`main`, output 0, input 0)
- OpenAI Chat Model1 → Generate Field Value (`ai_languageModel`, output 0, input 0)
- Filter Valid Fields → Fetch Records (`main`, output 0, input 0)
- Get Webhook Payload → Parse Event (`main`, output 0, input 0)
- Generate Field Value → Get Result (`main`, output 0, input 0)
- Add Row ID to Payload → Update Record (`main`, output 0, input 0)
- Generate Field Value1 → Get Result1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Airtable Vars (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0696_Code_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0696_Code_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
