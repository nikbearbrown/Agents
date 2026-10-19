# Gmail PDF Invoice/Receipt Classifier & Google Drive Uploader (via n8n & OpenAI)

This folder contains the **Gmail PDF Invoice/Receipt Classifier & Google Drive Uploader (via n8n & OpenAI)** workflow. Its executable nodes use `code`, `filter`, `gmail`, `googleDrive`, `if`, `merge`, `noOp`, `openAi`, `readPDF`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`gmail-pdf-invoice-receipt-classifier-google-drive-uploader-via-n8n-openai.json`](gmail-pdf-invoice-receipt-classifier-google-drive-uploader-via-n8n-openai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI | `openAi` | Inspect parameters |
| Configure | `set` | Inspect parameters |
| Iterate over email attachments | `code` | Inspect parameters |
| Not a PDF | `noOp` | Inspect parameters |
| Is text within token limit? | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Is matched | `if` | Inspect parameters |
| Upload file to folder | `googleDrive` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Create folder | `googleDrive` | folder |
| Aggregate attachments | `code` | Inspect parameters |
| Send email with invoices? | `if` | Inspect parameters |
| Send to my accountant | `gmail` | Inspect parameters |
| Get emails with attachments | `gmail` | getAll |
| Read PDF email attachments | `readPDF` | Inspect parameters |
| Is attachment a PDF? | `if` | Inspect parameters |
| Optional filter for emails | `filter` | Inspect parameters |

## Connection map

- Merge → Is matched (`main`, output 0, input 0)
- OpenAI → Merge (`main`, output 0, input 0)
- Webhook → Create folder (`main`, output 0, input 0)
- Configure → Get emails with attachments (`main`, output 0, input 0)
- Is matched → Upload file to folder (`main`, output 0, input 0)
- Is matched → Send email with invoices? (`main`, output 0, input 0)
- Create folder → Configure (`main`, output 0, input 0)
- Create folder → Respond to Webhook (`main`, output 0, input 0)
- Is attachment a PDF? → Read PDF email attachments (`main`, output 0, input 0)
- Is attachment a PDF? → Not a PDF (`main`, output 1, input 0)
- Aggregate attachments → Send to my accountant (`main`, output 0, input 0)
- Send email with invoices? → Aggregate attachments (`main`, output 0, input 0)
- Optional filter for emails → Iterate over email attachments (`main`, output 0, input 0)
- Read PDF email attachments → Is text within token limit? (`main`, output 0, input 0)
- Get emails with attachments → Optional filter for emails (`main`, output 0, input 0)
- Is text within token limit? → OpenAI (`main`, output 0, input 0)
- Is text within token limit? → Merge (`main`, output 0, input 1)
- Iterate over email attachments → Is attachment a PDF? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0892_Webhook_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0892_Webhook_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
