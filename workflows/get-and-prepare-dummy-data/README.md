# Get and prepare Dummy Data

This folder contains the **Get and prepare Dummy Data** workflow. Its executable nodes use `emailSend`, `extractFromFile`, `html`, `httpRequest`, `if`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `merge`, `set`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-and-prepare-dummy-data.json`](get-and-prepare-dummy-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `smtp`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Extract from File | `extractFromFile` | xls |
| Some Options for the Campaign | `set` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| AI did fail us1 | `stopAndError` | Inspect parameters |
| Fake coupon | `set` | Inspect parameters |
| Download dummy data | `httpRequest` | Inspect parameters |
| AI Output + Prev Data | `merge` | Inspect parameters |
| Is the result valid? | `if` | Inspect parameters |
| Coupon them or not to Coupon them | `if` | Inspect parameters |
| Html Template for our Email | `html` | Inspect parameters |
| The composed E-Mail + Prev Data | `merge` | Inspect parameters |
| Html Template for our Email with a Coupon | `html` | Inspect parameters |
| The composed E-Mail with Coupon + Prev Data | `merge` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |

## Connection map

- Fake coupon → Html Template for our Email with a Coupon (`main`, output 0, input 0)
- Extract from File → Some Options for the Campaign (`main`, output 0, input 0)
- OpenAI Chat Model1 → Information Extractor (`ai_languageModel`, output 0, input 0)
- Download dummy data → Extract from File (`main`, output 0, input 0)
- Is the result valid? → Coupon them or not to Coupon them (`main`, output 0, input 0)
- Is the result valid? → AI did fail us1 (`main`, output 1, input 0)
- AI Output + Prev Data → Is the result valid? (`main`, output 0, input 0)
- Information Extractor → AI Output + Prev Data (`main`, output 0, input 0)
- Html Template for our Email → The composed E-Mail + Prev Data (`main`, output 0, input 0)
- Some Options for the Campaign → Information Extractor (`main`, output 0, input 0)
- Some Options for the Campaign → AI Output + Prev Data (`main`, output 0, input 1)
- The composed E-Mail + Prev Data → Send Email (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Download dummy data (`main`, output 0, input 0)
- Coupon them or not to Coupon them → Html Template for our Email (`main`, output 0, input 0)
- Coupon them or not to Coupon them → The composed E-Mail + Prev Data (`main`, output 0, input 1)
- Coupon them or not to Coupon them → Fake coupon (`main`, output 1, input 0)
- Coupon them or not to Coupon them → The composed E-Mail with Coupon + Prev Data (`main`, output 1, input 0)
- Html Template for our Email with a Coupon → The composed E-Mail with Coupon + Prev Data (`main`, output 0, input 1)
- The composed E-Mail with Coupon + Prev Data → Send Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0331_Stopanderror_Extractfromfile_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0331_Stopanderror_Extractfromfile_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
