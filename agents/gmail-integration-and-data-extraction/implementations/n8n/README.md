# Gmail Integration and Data Extraction

This folder contains the **Gmail Integration and Data Extraction** workflow. Its executable nodes use `code`, `gmailTrigger`, `httpRequest`, `jira`, `microsoftOutlookTrigger`, `openAi`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`gmail-integration-and-data-extraction.json`](gmail-integration-and-data-extraction.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `httpBasicAuth`, `jiraSoftwareCloudApi`, `microsoftOutlookOAuth2Api`, `openAiApi`

**Entry nodes:** Gmail Trigger, Microsoft Outlook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Microsoft Outlook Trigger | `microsoftOutlookTrigger` | Inspect parameters |
| Screenshot HTML | `httpRequest` | POST |
| Retrieve Screenshot | `httpRequest` | Inspect parameters |
| Set Outlook Variables | `set` | Inspect parameters |
| Set Gmail Variables | `set` | Inspect parameters |
| Retrieve Headers of Email | `httpRequest` | Inspect parameters |
| Format Headers | `code` | Inspect parameters |
| Set Email Variables | `set` | Inspect parameters |
| ChatGPT Analysis | `openAi` | image / analyze |
| Create Jira Ticket | `jira` | Inspect parameters |
| Rename Screenshot | `code` | Inspect parameters |
| Upload Screenshot of Email to Jira | `jira` | issueAttachment |

## Connection map

- Gmail Trigger → Set Gmail Variables (`main`, output 0, input 0)
- Format Headers → Set Outlook Variables (`main`, output 0, input 0)
- Screenshot HTML → Retrieve Screenshot (`main`, output 0, input 0)
- ChatGPT Analysis → Create Jira Ticket (`main`, output 0, input 0)
- Rename Screenshot → Upload Screenshot of Email to Jira (`main`, output 0, input 0)
- Create Jira Ticket → Rename Screenshot (`main`, output 0, input 0)
- Retrieve Screenshot → ChatGPT Analysis (`main`, output 0, input 0)
- Set Email Variables → Screenshot HTML (`main`, output 0, input 0)
- Set Gmail Variables → Set Email Variables (`main`, output 0, input 0)
- Set Outlook Variables → Set Email Variables (`main`, output 0, input 0)
- Microsoft Outlook Trigger → Retrieve Headers of Email (`main`, output 0, input 0)
- Retrieve Headers of Email → Format Headers (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1308_Code_Microsoftoutlook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1308_Code_Microsoftoutlook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
