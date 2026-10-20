# Send Emails from Obsidian

This folder contains the **Send Emails from Obsidian** workflow. Its executable nodes use `aggregate`, `convertToFile`, `dateTime`, `gmail`, `if`, `respondToWebhook`, `set`, `splitInBatches`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-emails-from-obsidian.json`](send-emails-from-obsidian.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check if attachments exist | `if` | Inspect parameters |
| Separate attachment data | `splitOut` | Inspect parameters |
| Process Each Attachment | `splitInBatches` | Inspect parameters |
| Convert Attachment to File | `convertToFile` | toBinary |
| Prepare Attachments for Email | `aggregate` | Inspect parameters |
| Email With Attachments | `gmail` | Inspect parameters |
| Email Without Attachments | `gmail` | Inspect parameters |
| Check if it is a test | `if` | Inspect parameters |
| Respond to Obsidian | `respondToWebhook` | Inspect parameters |
| Fix Base64 string | `set` | Inspect parameters |
| Test Succesfull | `respondToWebhook` | Inspect parameters |
| Get date | `dateTime` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Webhook → Check if attachments exist (`main`, output 0, input 0)
- Get date → Respond to Obsidian (`main`, output 0, input 0)
- Fix Base64 string → Process Each Attachment (`main`, output 0, input 0)
- Check if it is a test → Test Succesfull (`main`, output 0, input 0)
- Check if it is a test → Email Without Attachments (`main`, output 1, input 0)
- Email With Attachments → Get date (`main`, output 0, input 0)
- Process Each Attachment → Prepare Attachments for Email (`main`, output 0, input 0)
- Process Each Attachment → Convert Attachment to File (`main`, output 1, input 0)
- Separate attachment data → Fix Base64 string (`main`, output 0, input 0)
- Email Without Attachments → Get date (`main`, output 0, input 0)
- Check if attachments exist → Separate attachment data (`main`, output 0, input 0)
- Check if attachments exist → Check if it is a test (`main`, output 1, input 0)
- Convert Attachment to File → Process Each Attachment (`main`, output 0, input 0)
- Prepare Attachments for Email → Email With Attachments (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1403_Splitout_Datetime_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1403_Splitout_Datetime_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
