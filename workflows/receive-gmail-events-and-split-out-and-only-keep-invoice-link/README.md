# receive gmail events and split out and only keep invoice link

This folder contains the **receive gmail events and split out and only keep invoice link** workflow. Its executable nodes use `filter`, `gmailTrigger`, `googleDrive`, `html`, `httpRequest`, `if`, `noOp`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-gmail-events-and-split-out-and-only-keep-invoice-link.json`](receive-gmail-events-and-split-out-and-only-keep-invoice-link.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Only n8n Paddle invoice mails | `if` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Only keep invoice link | `filter` | Inspect parameters |
| Do nothing on other emails | `noOp` | Inspect parameters |
| Setup | `set` | Inspect parameters |
| Download Invoice PDF from URL | `httpRequest` | Inspect parameters |
| Rename file | `googleDrive` | update |
| Move to the correct folder | `googleDrive` | move |
| Upload PDF to Drive | `httpRequest` | POST |
| Extract "a-tags" from email | `html` | extractHtmlContent |

## Connection map

- Setup → Only n8n Paddle invoice mails (`main`, output 0, input 0)
- Split Out → Only keep invoice link (`main`, output 0, input 0)
- Rename file → Move to the correct folder (`main`, output 0, input 0)
- Gmail Trigger → Setup (`main`, output 0, input 0)
- Upload PDF to Drive → Rename file (`main`, output 0, input 0)
- Only keep invoice link → Download Invoice PDF from URL (`main`, output 0, input 0)
- Extract "a-tags" from email → Split Out (`main`, output 0, input 0)
- Download Invoice PDF from URL → Upload PDF to Drive (`main`, output 0, input 0)
- Only n8n Paddle invoice mails → Extract "a-tags" from email (`main`, output 0, input 0)
- Only n8n Paddle invoice mails → Do nothing on other emails (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0562_Splitout_Filter_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0562_Splitout_Filter_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
