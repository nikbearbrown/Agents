# 🙋‍♂️ Why not just use the built-in PDF convertor?

This folder contains the **🙋‍♂️ Why not just use the built-in PDF convertor?** workflow. Its executable nodes use `aggregate`, `chainLlm`, `gmail`, `gmailTrigger`, `googleSheets`, `httpRequest`, `if`, `lmOpenAi`, `merge`, `outputParserStructured`, `set`, `splitOut`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`why-not-just-use-the-built-in-pdf-convertor.json`](why-not-just-use-the-built-in-pdf-convertor.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** Receiving Invoices

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Model | `lmOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Upload to LlamaParse | `httpRequest` | POST |
| Receiving Invoices | `gmailTrigger` | Inspect parameters |
| Append to Reconciliation Sheet | `googleSheets` | append |
| Get Processing Status | `httpRequest` | Inspect parameters |
| Wait to stay within service limits | `wait` | Inspect parameters |
| Is Job Ready? | `switch` | Inspect parameters |
| Add "invoice synced" Label | `gmail` | addLabels |
| Get Parsed Invoice Data | `httpRequest` | Inspect parameters |
| Map Output | `set` | Inspect parameters |
| Apply Data Extraction Rules | `chainLlm` | Inspect parameters |
| Should Process Email? | `if` | Inspect parameters |
| Split Out Labels | `splitOut` | Inspect parameters |
| Get Labels Names | `gmail` | label / get |
| Combine Label Names | `aggregate` | Inspect parameters |
| Email with Label Names | `merge` | Inspect parameters |

## Connection map

- Map Output → Append to Reconciliation Sheet (`main`, output 0, input 0)
- OpenAI Model → Apply Data Extraction Rules (`ai_languageModel`, output 0, input 0)
- Is Job Ready? → Get Parsed Invoice Data (`main`, output 0, input 0)
- Is Job Ready? → Wait to stay within service limits (`main`, output 3, input 0)
- Get Labels Names → Combine Label Names (`main`, output 0, input 0)
- Split Out Labels → Get Labels Names (`main`, output 0, input 0)
- Receiving Invoices → Split Out Labels (`main`, output 0, input 0)
- Receiving Invoices → Email with Label Names (`main`, output 0, input 0)
- Combine Label Names → Email with Label Names (`main`, output 0, input 1)
- Upload to LlamaParse → Get Processing Status (`main`, output 0, input 0)
- Get Processing Status → Is Job Ready? (`main`, output 0, input 0)
- Should Process Email? → Upload to LlamaParse (`main`, output 0, input 0)
- Email with Label Names → Should Process Email? (`main`, output 0, input 0)
- Get Parsed Invoice Data → Apply Data Extraction Rules (`main`, output 0, input 0)
- Structured Output Parser → Apply Data Extraction Rules (`ai_outputParser`, output 0, input 0)
- Apply Data Extraction Rules → Map Output (`main`, output 0, input 0)
- Append to Reconciliation Sheet → Add "invoice synced" Label (`main`, output 0, input 0)
- Wait to stay within service limits → Get Processing Status (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0523_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0523_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
