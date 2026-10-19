# WordPress Contact Form (CF7) Responses and Classification

This folder contains the **WordPress Contact Form (CF7) Responses and Classification** workflow. Its executable nodes use `chainLlm`, `gmail`, `googleSheets`, `lmChatGoogleGemini`, `outputParserStructured`, `set`, `textClassifier`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`wordpress-contact-form-cf7-responses-and-classification.json`](wordpress-contact-form-cf7-responses-and-classification.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `googleSheetsOAuth2Api`

**Entry nodes:** From Wordpress

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| From Wordpress | `webhook` | Inspect parameters |
| Set Fields | `set` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Message Classifier | `textClassifier` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Email draft - Other info | `gmail` | draft |
| Email writer (Others) | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Email writer (Order info) | `chainLlm` | Inspect parameters |
| Email writer (Product info) | `chainLlm` | Inspect parameters |
| Email draft - Product info | `gmail` | draft |
| Email draft - Order info | `gmail` | draft |
| Save on Sheet (product) | `googleSheets` | append |
| Save on Sheet (order) | `googleSheets` | append |
| Save on Sheet (other) | `googleSheets` | append |
| Subject and Text | `outputParserStructured` | Inspect parameters |
| Subject and Text 2 | `outputParserStructured` | Inspect parameters |
| Subject and Text 3 | `outputParserStructured` | Inspect parameters |

## Connection map

- Set Fields → Message Classifier (`main`, output 0, input 0)
- From Wordpress → Set Fields (`main`, output 0, input 0)
- Subject and Text → Email writer (Product info) (`ai_outputParser`, output 0, input 0)
- Message Classifier → Email writer (Product info) (`main`, output 0, input 0)
- Message Classifier → Email writer (Order info) (`main`, output 1, input 0)
- Message Classifier → Email writer (Others) (`main`, output 2, input 0)
- Subject and Text 2 → Email writer (Order info) (`ai_outputParser`, output 0, input 0)
- Subject and Text 3 → Email writer (Others) (`ai_outputParser`, output 0, input 0)
- Email writer (Others) → Email draft - Other info (`main`, output 0, input 0)
- Email draft - Order info → Save on Sheet (order) (`main`, output 0, input 0)
- Email draft - Other info → Save on Sheet (other) (`main`, output 0, input 0)
- Google Gemini Chat Model → Message Classifier (`ai_languageModel`, output 0, input 0)
- Email writer (Order info) → Email draft - Order info (`main`, output 0, input 0)
- Google Gemini Chat Model1 → Email writer (Others) (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Email writer (Order info) (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model3 → Email writer (Product info) (`ai_languageModel`, output 0, input 0)
- Email draft - Product info → Save on Sheet (product) (`main`, output 0, input 0)
- Email writer (Product info) → Email draft - Product info (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/1860_GoogleSheets_Gmail_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googlesheets/1860_GoogleSheets_Gmail_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
