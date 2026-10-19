# Job-App

This folder contains the **Job-App** workflow. Its executable nodes use `agent`, `code`, `convertToFile`, `extractFromFile`, `googleDrive`, `googleSheets`, `httpRequest`, `lmChatDeepSeek`, `outputParserStructured`, `set`, `splitInBatches`, `toolThink`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`job-app.json`](job-app.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Frontend input

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Frontend input | `webhook` | Inspect parameters |
| Extract data from pdf | `extractFromFile` | pdf |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| DeepSeek Chat Model | `lmChatDeepSeek` | Inspect parameters |
| Personal Details Extract | `agent` | Inspect parameters |
| Drive Details Set | `set` | Inspect parameters |
| Google Drive | `googleDrive` | folder |
| Primary Details | `set` | Inspect parameters |
| Google Sheets | `googleSheets` | appendOrUpdate |
| Sheets Title Set | `set` | Inspect parameters |
| Sheet Titles | `set` | Inspect parameters |
| Google Sheets2 | `googleSheets` | append |
| URL Fields | `set` | Inspect parameters |
| Job Request URL | `httpRequest` | POST |
| Job Details Set | `set` | Inspect parameters |
| Store Job details | `googleSheets` | appendOrUpdate |
| Create Personal Sheet | `googleSheets` | create |
| Extract Job from Sheets | `googleSheets` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| DeepSeek Chat Model1 | `lmChatDeepSeek` | Inspect parameters |
| Think | `toolThink` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Code1 | `code` | Inspect parameters |
| HTTP Request | `httpRequest` | POST |
| Edit Fields | `set` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Google Drive1 | `googleDrive` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |
| Google Sheets1 | `googleSheets` | appendOrUpdate |

## Connection map

- Frontend input → Extract data from pdf (`main`, output 0, input 0)
- Extract data from pdf → Personal Details Extract (`main`, output 0, input 0)
- Structured Output Parser → Personal Details Extract (`ai_outputParser`, output 0, input 0)
- DeepSeek Chat Model → Personal Details Extract (`ai_languageModel`, output 0, input 0)
- Personal Details Extract → Drive Details Set (`main`, output 0, input 0)
- Drive Details Set → Google Drive (`main`, output 0, input 0)
- Google Drive → Primary Details (`main`, output 0, input 0)
- Primary Details → Google Sheets (`main`, output 0, input 0)
- Google Sheets → Sheets Title Set (`main`, output 0, input 0)
- Sheets Title Set → Create Personal Sheet (`main`, output 0, input 0)
- Sheet Titles → Google Sheets2 (`main`, output 0, input 0)
- Google Sheets2 → URL Fields (`main`, output 0, input 0)
- URL Fields → Job Request URL (`main`, output 0, input 0)
- Job Request URL → Code1 (`main`, output 0, input 0)
- Job Details Set → Store Job details (`main`, output 0, input 0)
- Store Job details → Extract Job from Sheets (`main`, output 0, input 0)
- Create Personal Sheet → Sheet Titles (`main`, output 0, input 0)
- Extract Job from Sheets → Code (`main`, output 0, input 0)
- Code → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Edit Fields1 (`main`, output 1, input 0)
- AI Agent → Convert to File (`main`, output 0, input 0)
- DeepSeek Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- Think → AI Agent (`ai_tool`, output 0, input 0)
- Structured Output Parser1 → AI Agent (`ai_outputParser`, output 0, input 0)
- Convert to File → Edit Fields (`main`, output 0, input 0)
- Code1 → Job Details Set (`main`, output 0, input 0)
- HTTP Request → Google Drive1 (`main`, output 0, input 0)
- Edit Fields → HTTP Request (`main`, output 0, input 0)
- Edit Fields1 → AI Agent (`main`, output 0, input 0)
- Google Drive1 → Edit Fields2 (`main`, output 0, input 0)
- Edit Fields2 → Google Sheets1 (`main`, output 0, input 0)
- Google Sheets1 → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/AloysJehwin/job-app/blob/000b8dd5f0eb2a89197faf64724a88d6473533fe/Job_App.json](https://github.com/AloysJehwin/job-app/blob/000b8dd5f0eb2a89197faf64724a88d6473533fe/Job_App.json). License: **MIT**; preserve [the notice](../../licenses/AloysJehwin--job-app.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
