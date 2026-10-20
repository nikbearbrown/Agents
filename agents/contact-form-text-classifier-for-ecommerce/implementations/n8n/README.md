# Contact Form Text Classifier for eCommerce

This folder contains the **Contact Form Text Classifier for eCommerce** workflow. Its executable nodes use `emailSend`, `formTrigger`, `googleSheets`, `lmChatOpenAi`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`contact-form-text-classifier-for-ecommerce.json`](contact-form-text-classifier-for-ecommerce.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `smtp`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| OpenAI | `lmChatOpenAi` | Inspect parameters |
| Prod. Dep. | `emailSend` | Inspect parameters |
| Quote Dep. | `emailSend` | Inspect parameters |
| Gen. Dep. | `emailSend` | Inspect parameters |
| Order Dep. | `emailSend` | Inspect parameters |
| Other Dep. | `emailSend` | Inspect parameters |
| Quote DB | `googleSheets` | append |
| Prod DB | `googleSheets` | append |
| General DB | `googleSheets` | append |
| Order DB | `googleSheets` | append |
| Other DB | `googleSheets` | append |

## Connection map

- OpenAI → Text Classifier (`ai_languageModel`, output 0, input 0)
- Gen. Dep. → General DB (`main`, output 0, input 0)
- Order Dep. → Order DB (`main`, output 0, input 0)
- Other Dep. → Other DB (`main`, output 0, input 0)
- Prod. Dep. → Prod DB (`main`, output 0, input 0)
- Quote Dep. → Quote DB (`main`, output 0, input 0)
- Text Classifier → Quote Dep. (`main`, output 0, input 0)
- Text Classifier → Prod. Dep. (`main`, output 0, input 0)
- Text Classifier → Gen. Dep. (`main`, output 2, input 0)
- Text Classifier → Order Dep. (`main`, output 3, input 0)
- Text Classifier → Other Dep. (`main`, output 4, input 0)
- On form submission → Text Classifier (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1537_Form_GoogleSheets_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1537_Form_GoogleSheets_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
