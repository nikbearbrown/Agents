# Example Webhook Request

This folder contains the **Example Webhook Request** workflow. Its executable nodes use `chainLlm`, `extractFromFile`, `gmail`, `googleDocs`, `lmChatOpenAi`, `openAi`, `outputParserItemList`, `set`, `slack`, `splitInBatches`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`example-webhook-request.json`](example-webhook-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDocsOAuth2Api`, `openAiApi`, `slackApi`

**Entry nodes:** Wait for Request

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get RFP Data | `extractFromFile` | pdf |
| Item List Output Parser | `outputParserItemList` | Inspect parameters |
| For Each Question... | `splitInBatches` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Create new RFP Response Document | `googleDocs` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Send Chat Notification | `slack` | Inspect parameters |
| Send Email Notification | `gmail` | Inspect parameters |
| Add Metadata to Response Doc | `googleDocs` | update |
| Record Question & Answer in Response Doc | `googleDocs` | update |
| Answer Question with Context | `openAi` | assistant |
| Wait for Request | `webhook` | Inspect parameters |
| Extract Questions From RFP | `chainLlm` | Inspect parameters |

## Connection map

- Get RFP Data → Set Variables (`main`, output 0, input 0)
- Set Variables → Create new RFP Response Document (`main`, output 0, input 0)
- Wait for Request → Get RFP Data (`main`, output 0, input 0)
- OpenAI Chat Model → Extract Questions From RFP (`ai_languageModel`, output 0, input 0)
- For Each Question... → Send Email Notification (`main`, output 0, input 0)
- For Each Question... → Answer Question with Context (`main`, output 1, input 0)
- Item List Output Parser → Extract Questions From RFP (`ai_outputParser`, output 0, input 0)
- Send Email Notification → Send Chat Notification (`main`, output 0, input 0)
- Extract Questions From RFP → For Each Question... (`main`, output 0, input 0)
- Add Metadata to Response Doc → Extract Questions From RFP (`main`, output 0, input 0)
- Answer Question with Context → Record Question & Answer in Response Doc (`main`, output 0, input 0)
- Create new RFP Response Document → Add Metadata to Response Doc (`main`, output 0, input 0)
- Record Question & Answer in Response Doc → For Each Question... (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/0524_Googledocs_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledocs/0524_Googledocs_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
