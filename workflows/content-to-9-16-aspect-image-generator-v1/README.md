# Content to 9:16 Aspect Image Generator v1

This folder contains the **Content to 9:16 Aspect Image Generator v1** workflow. Its executable nodes use `airtable`, `filter`, `httpRequest`, `limit`, `manualTrigger`, `openAi`, `removeDuplicates`, `set`, `splitInBatches`, `splitOut`, `toolWikipedia`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`content-to-9-16-aspect-image-generator-v1.json`](content-to-9-16-aspect-image-generator-v1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpCustomAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set Guidelines | `set` | Inspect parameters |
| Get Brand Guidelines | `airtable` | search |
| Get SEO Keywords | `airtable` | search |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Keyword Filter | `filter` | Inspect parameters |
| Get Content | `airtable` | Inspect parameters |
| Split Out Content | `splitOut` | Inspect parameters |
| Split Out Keywords | `splitOut` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Script Prep | `openAi` | Inspect parameters |
| Split Out Scenes | `splitOut` | Inspect parameters |
| Split Out TN Prompt | `splitOut` | Inspect parameters |
| Leo - Improve Prompt1 | `httpRequest` | POST |
| Leo - Get imageId1 | `httpRequest` | Inspect parameters |
| Prompt Settings | `set` | Inspect parameters |
| Leo - Generate Image1 | `httpRequest` | POST |
| Wait 30 Seconds | `wait` | Inspect parameters |
| Leo - Improve Prompt | `httpRequest` | POST |
| Leo - Get imageId | `httpRequest` | Inspect parameters |
| Prompt Settings1 | `set` | Inspect parameters |
| Leo - Generate Image | `httpRequest` | POST |
| Wait 30 Seconds1 | `wait` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Add Asset Info | `airtable` | create |
| Add Asset Info1 | `airtable` | create |
| Wikipedia | `toolWikipedia` | Inspect parameters |

## Connection map

- Limit → Script Prep (`main`, output 0, input 0)
- Wikipedia → Script Prep (`ai_tool`, output 0, input 0)
- Get Content → Split Out Content (`main`, output 0, input 0)
- Script Prep → Split Out TN Prompt (`main`, output 0, input 0)
- Script Prep → Split Out Scenes (`main`, output 0, input 0)
- Keyword Filter → Remove Duplicates (`main`, output 0, input 0)
- Set Guidelines → Get SEO Keywords (`main`, output 0, input 0)
- Add Asset Info1 → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Prompt Settings1 (`main`, output 1, input 0)
- Prompt Settings → Leo - Improve Prompt1 (`main`, output 0, input 0)
- Wait 30 Seconds → Leo - Get imageId1 (`main`, output 0, input 0)
- Get SEO Keywords → Keyword Filter (`main`, output 0, input 0)
- Prompt Settings1 → Leo - Improve Prompt (`main`, output 0, input 0)
- Split Out Scenes → Loop Over Items (`main`, output 0, input 0)
- Wait 30 Seconds1 → Leo - Get imageId (`main`, output 0, input 0)
- Leo - Get imageId → Add Asset Info1 (`main`, output 0, input 0)
- Remove Duplicates → Split Out Keywords (`main`, output 0, input 0)
- Split Out Content → Limit (`main`, output 0, input 0)
- Leo - Get imageId1 → Add Asset Info (`main`, output 0, input 0)
- Split Out Keywords → Get Content (`main`, output 0, input 0)
- Split Out TN Prompt → Prompt Settings (`main`, output 0, input 0)
- Get Brand Guidelines → Set Guidelines (`main`, output 0, input 0)
- Leo - Generate Image → Wait 30 Seconds1 (`main`, output 0, input 0)
- Leo - Improve Prompt → Leo - Generate Image (`main`, output 0, input 0)
- Leo - Generate Image1 → Wait 30 Seconds (`main`, output 0, input 0)
- Leo - Improve Prompt1 → Leo - Generate Image1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Brand Guidelines (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1469_Wait_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1469_Wait_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
