# download google drive and http request and upload to drive

This folder contains the **download google drive and http request and upload to drive** workflow. Its executable nodes use `aggregate`, `chainLlm`, `filter`, `googleDrive`, `googleSheets`, `httpRequest`, `linear`, `lmChatGoogleGemini`, `manualTrigger`, `merge`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`download-google-drive-and-http-request-and-upload-to-drive.json`](download-google-drive-and-http-request-and-upload-to-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `httpQueryAuth`, `linearApi`

**Entry nodes:** Schedule Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Base Image | `googleDrive` | download |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Download Screenshot | `httpRequest` | Inspect parameters |
| Upload to Drive | `googleDrive` | Inspect parameters |
| Update Base Image | `googleSheets` | appendOrUpdate |
| Merge | `merge` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get URLs with Missing Base Images | `googleSheets` | Inspect parameters |
| Run Webpage Screenshot | `httpRequest` | POST |
| Run Webpage Screenshot1 | `httpRequest` | POST |
| Has Changes | `filter` | Inspect parameters |
| Combine Row and Result | `set` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Create Report | `linear` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Webpages List | `googleSheets` | Inspect parameters |
| For Each Webpage... | `splitInBatches` | Inspect parameters |
| Download New Screenshot | `httpRequest` | Inspect parameters |
| Combine Screenshots | `merge` | Inspect parameters |
| Visual Regression Agent | `chainLlm` | Inspect parameters |

## Connection map

- Wait → Loop Over Items (`main`, output 0, input 0)
- Merge → Download Screenshot (`main`, output 0, input 0)
- Wait1 → For Each Webpage... (`main`, output 0, input 0)
- Aggregate → Create Report (`main`, output 0, input 0)
- Base Image → Combine Screenshots (`main`, output 0, input 0)
- Has Changes → Aggregate (`main`, output 0, input 0)
- Loop Over Items → Merge (`main`, output 0, input 1)
- Loop Over Items → Run Webpage Screenshot (`main`, output 1, input 0)
- Upload to Drive → Update Base Image (`main`, output 0, input 0)
- Schedule Trigger → Get Webpages List (`main`, output 0, input 0)
- Get Webpages List → For Each Webpage... (`main`, output 0, input 0)
- Combine Screenshots → Visual Regression Agent (`main`, output 0, input 0)
- Download Screenshot → Upload to Drive (`main`, output 0, input 0)
- For Each Webpage... → Combine Row and Result (`main`, output 0, input 0)
- For Each Webpage... → Base Image (`main`, output 1, input 0)
- For Each Webpage... → Run Webpage Screenshot1 (`main`, output 1, input 0)
- Combine Row and Result → Has Changes (`main`, output 0, input 0)
- Run Webpage Screenshot → Wait (`main`, output 0, input 0)
- Download New Screenshot → Combine Screenshots (`main`, output 0, input 1)
- Run Webpage Screenshot1 → Download New Screenshot (`main`, output 0, input 0)
- Visual Regression Agent → Wait1 (`main`, output 0, input 0)
- Google Gemini Chat Model → Visual Regression Agent (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Visual Regression Agent (`ai_outputParser`, output 0, input 0)
- Get URLs with Missing Base Images → Loop Over Items (`main`, output 0, input 0)
- Get URLs with Missing Base Images → Merge (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get URLs with Missing Base Images (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0578_Wait_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0578_Wait_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `download-google-drive-and-http-request-and-upload-to-drive-55d88aa4` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
