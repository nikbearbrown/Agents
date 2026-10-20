# PURCHASE ORDER EXAMPLE

This folder contains the **PURCHASE ORDER EXAMPLE** workflow. Its executable nodes use `code`, `extractFromFile`, `if`, `informationExtractor`, `lmChatOpenAi`, `microsoftOutlook`, `microsoftOutlookTrigger`, `noOp`, `set`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`purchase-order-example.json`](purchase-order-example.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftOutlookOAuth2Api`, `openAiApi`

**Entry nodes:** Outlook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract Purchase Order Details | `informationExtractor` | Inspect parameters |
| Is Excel Document? | `if` | Inspect parameters |
| Run Checks | `set` | Inspect parameters |
| Is Valid Purchase Order? | `if` | Inspect parameters |
| Extract from File | `extractFromFile` | xlsx |
| XLSX to Markdown Table | `code` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Reply Invalid Format | `microsoftOutlook` | reply |
| Outlook Trigger | `microsoftOutlookTrigger` | Inspect parameters |
| Reply Rejection | `microsoftOutlook` | reply |
| Reply Accepted | `microsoftOutlook` | reply |
| Do Something with Purchase Order | `noOp` | Inspect parameters |
| Fix Excel Dates | `set` | Inspect parameters |
| Is Submitting a Purchase Order? | `textClassifier` | Inspect parameters |
| Do Nothing | `noOp` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Run Checks → Is Valid Purchase Order? (`main`, output 0, input 0)
- Reply Accepted → Do Something with Purchase Order (`main`, output 0, input 0)
- Fix Excel Dates → Run Checks (`main`, output 0, input 0)
- Outlook Trigger → Is Submitting a Purchase Order? (`main`, output 0, input 0)
- Extract from File → XLSX to Markdown Table (`main`, output 0, input 0)
- OpenAI Chat Model → Extract Purchase Order Details (`ai_languageModel`, output 0, input 0)
- Is Excel Document? → Extract from File (`main`, output 0, input 0)
- Is Excel Document? → Reply Invalid Format (`main`, output 1, input 0)
- OpenAI Chat Model1 → Is Submitting a Purchase Order? (`ai_languageModel`, output 0, input 0)
- XLSX to Markdown Table → Extract Purchase Order Details (`main`, output 0, input 0)
- Is Valid Purchase Order? → Reply Accepted (`main`, output 0, input 0)
- Is Valid Purchase Order? → Reply Rejection (`main`, output 1, input 0)
- Extract Purchase Order Details → Fix Excel Dates (`main`, output 0, input 0)
- Is Submitting a Purchase Order? → Is Excel Document? (`main`, output 0, input 0)
- Is Submitting a Purchase Order? → Do Nothing (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0851_Code_Extractfromfile_Monitor_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0851_Code_Extractfromfile_Monitor_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
