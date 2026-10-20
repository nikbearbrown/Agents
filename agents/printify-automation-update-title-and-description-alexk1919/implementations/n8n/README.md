# Printify Automation - Update Title and Description - AlexK1919

This folder contains the **Printify Automation - Update Title and Description - AlexK1919** workflow. Its executable nodes use `code`, `googleSheets`, `googleSheetsTrigger`, `httpRequest`, `if`, `manualTrigger`, `openAi`, `set`, `splitInBatches`, `splitOut`, `toolCalculator`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`printify-automation-update-title-and-description-alexk1919.json`](printify-automation-update-title-and-description-alexk1919.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’, Google Sheets Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Printify - Get Shops | `httpRequest` | Inspect parameters |
| Printify - Get Products | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Split - id, title, desc | `splitOut` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Printify - Update Product | `httpRequest` | PUT |
| Brand Guidelines + Custom Instructions | `set` | Inspect parameters |
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| Printify - Get Shops1 | `httpRequest` | Inspect parameters |
| GS - Add Product Option | `googleSheets` | append |
| Update Product Option | `googleSheets` | appendOrUpdate |
| If1 | `if` | Inspect parameters |
| Number of Options | `set` | Inspect parameters |
| Calculate Options | `code` | Inspect parameters |
| Remember Options | `set` | Inspect parameters |
| Generate Title and Desc | `openAi` | Inspect parameters |
| If | `if` | Inspect parameters |

## Connection map

- If → Printify - Get Shops1 (`main`, output 0, input 0)
- If1 → Loop Over Items (`main`, output 0, input 0)
- If1 → GS - Add Product Option (`main`, output 1, input 0)
- Split Out → Loop Over Items (`main`, output 0, input 0)
- Wikipedia → Generate Title and Desc (`ai_tool`, output 0, input 0)
- Calculator → Generate Title and Desc (`ai_tool`, output 0, input 0)
- Loop Over Items → Split - id, title, desc (`main`, output 1, input 0)
- Remember Options → Calculate Options (`main`, output 0, input 0)
- Calculate Options → If1 (`main`, output 0, input 0)
- Number of Options → Calculate Options (`main`, output 0, input 0)
- Printify - Get Shops → Printify - Get Products (`main`, output 0, input 0)
- Google Sheets Trigger → If (`main`, output 0, input 0)
- Printify - Get Shops1 → Printify - Update Product (`main`, output 0, input 0)
- Update Product Option → Remember Options (`main`, output 0, input 0)
- GS - Add Product Option → Generate Title and Desc (`main`, output 0, input 0)
- Generate Title and Desc → Update Product Option (`main`, output 0, input 0)
- Printify - Get Products → Split Out (`main`, output 0, input 0)
- Split - id, title, desc → Number of Options (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Brand Guidelines + Custom Instructions (`main`, output 0, input 0)
- Brand Guidelines + Custom Instructions → Printify - Get Shops (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0339_Splitout_Code_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0339_Splitout_Code_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
