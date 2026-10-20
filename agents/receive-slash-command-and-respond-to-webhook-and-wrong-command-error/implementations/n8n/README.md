# receive slash command and respond to webhook and wrong command error

This folder contains the **receive slash command and respond to webhook and wrong command error** workflow. Its executable nodes use `airtable`, `crypto`, `executeWorkflow`, `function`, `httpRequest`, `if`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-slash-command-and-respond-to-webhook-and-wrong-command-error.json`](receive-slash-command-and-respond-to-webhook-and-wrong-command-error.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`

**Entry nodes:** Receive Slash Command

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Receive Slash Command | `webhook` | Inspect parameters |
| Reject | `respondToWebhook` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Read Command | `switch` | Inspect parameters |
| Wrong Command Error | `respondToWebhook` | Inspect parameters |
| Acknowledge | `respondToWebhook` | Inspect parameters |
| Empty Email? | `if` | Inspect parameters |
| Missing Email Error | `respondToWebhook` | Inspect parameters |
| Valid Token? | `if` | Inspect parameters |
| Paddle Data Deletion | `executeWorkflow` | Inspect parameters |
| Customer.io Data Deletion | `executeWorkflow` | Inspect parameters |
| Zendesk Data Deletion | `executeWorkflow` | Inspect parameters |
| Airtable | `airtable` | append |
| Prepare Log Entry | `function` | Inspect parameters |
| Crypto | `crypto` | Inspect parameters |
| Respond to Slack | `httpRequest` | Inspect parameters |

## Connection map

- Set → Read Command (`main`, output 0, input 0)
- Crypto → Airtable (`main`, output 0, input 0)
- Airtable → Respond to Slack (`main`, output 0, input 0)
- Acknowledge → Paddle Data Deletion (`main`, output 0, input 0)
- Empty Email? → Missing Email Error (`main`, output 0, input 0)
- Empty Email? → Acknowledge (`main`, output 1, input 0)
- Read Command → Empty Email? (`main`, output 0, input 0)
- Read Command → Wrong Command Error (`main`, output 3, input 0)
- Valid Token? → Set (`main`, output 0, input 0)
- Valid Token? → Reject (`main`, output 1, input 0)
- Prepare Log Entry → Crypto (`main`, output 0, input 0)
- Paddle Data Deletion → Customer.io Data Deletion (`main`, output 0, input 0)
- Receive Slash Command → Valid Token? (`main`, output 0, input 0)
- Zendesk Data Deletion → Prepare Log Entry (`main`, output 0, input 0)
- Customer.io Data Deletion → Zendesk Data Deletion (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0165_Webhook_Respondtowebhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0165_Webhook_Respondtowebhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
