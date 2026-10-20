# webhook and execute command and respond to webhook1

This folder contains the **webhook and execute command and respond to webhook1** workflow. Its executable nodes use `code`, `executeCommand`, `respondToWebhook`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-execute-command-and-respond-to-webhook1.json`](webhook-and-execute-command-and-respond-to-webhook1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| 模式 | `switch` | Inspect parameters |
| chores | `executeCommand` | Inspect parameters |
| chores-code | `code` | Inspect parameters |
| Respond to Webhook1 | `respondToWebhook` | Inspect parameters |
| Switch-Chores | `switch` | Inspect parameters |
| Respond to Webhook2 | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → 模式 (`main`, output 0, input 0)
- 模式 → chores (`main`, output 0, input 0)
- chores → Switch-Chores (`main`, output 0, input 0)
- chores-code → Respond to Webhook1 (`main`, output 0, input 0)
- Switch-Chores → chores-code (`main`, output 0, input 0)
- Switch-Chores → Respond to Webhook2 (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/osnsyc/chores-automation/blob/72e1933f98a5cac5ba5cabdf88ce1fa44e711f45/n8n.json](https://github.com/osnsyc/chores-automation/blob/72e1933f98a5cac5ba5cabdf88ce1fa44e711f45/n8n.json). License: **MIT**; preserve [the notice](../../../../licenses/osnsyc--chores-automation.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
