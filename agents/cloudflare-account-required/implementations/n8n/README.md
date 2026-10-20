# Cloudflare Account Required

This folder contains the **Cloudflare Account Required** workflow. Its executable nodes use `code`, `convertToFile`, `gmail`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `set`, `sort`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cloudflare-account-required.json`](cloudflare-account-required.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `cloudflareApi`, `gmailOAuth2`, `googlePalmApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Term Dates Excel | `httpRequest` | Inspect parameters |
| Extract Key Events and Dates | `informationExtractor` | Inspect parameters |
| Extract Target Sheet | `set` | Inspect parameters |
| Fix Dates | `set` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Create ICS File | `convertToFile` | toBinary |
| Events to ICS Document | `code` | Inspect parameters |
| Sort Events by Date | `sort` | Inspect parameters |
| Markdown Conversion Service | `httpRequest` | POST |
| Events to Items | `splitOut` | Inspect parameters |
| Send Email with Attachment | `gmail` | Inspect parameters |

## Connection map

- Fix Dates → Sort Events by Date (`main`, output 0, input 0)
- Create ICS File → Send Email with Attachment (`main`, output 0, input 0)
- Events to Items → Fix Dates (`main`, output 0, input 0)
- Sort Events by Date → Events to ICS Document (`main`, output 0, input 0)
- Extract Target Sheet → Extract Key Events and Dates (`main`, output 0, input 0)
- Get Term Dates Excel → Markdown Conversion Service (`main`, output 0, input 0)
- Events to ICS Document → Create ICS File (`main`, output 0, input 0)
- Google Gemini Chat Model → Extract Key Events and Dates (`ai_languageModel`, output 0, input 0)
- Markdown Conversion Service → Extract Target Sheet (`main`, output 0, input 0)
- Extract Key Events and Dates → Events to Items (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Term Dates Excel (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0846_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0846_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
