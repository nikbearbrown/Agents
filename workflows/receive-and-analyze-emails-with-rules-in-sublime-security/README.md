# Receive_and_analyze_emails_with_rules_in_Sublime_Security

This folder contains the **Receive_and_analyze_emails_with_rules_in_Sublime_Security** workflow. Its executable nodes use `code`, `emailReadImap`, `httpRequest`, `if`, `manualTrigger`, `moveBinaryData`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-and-analyze-emails-with-rules-in-sublime-security.json`](receive-and-analyze-emails-with-rules-in-sublime-security.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `imap`, `slackApi`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| IF email has attachment | `if` | Inspect parameters |
| Split to matched and unmatched | `code` | Inspect parameters |
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Format the message | `set` | Inspect parameters |
| Notify about missing attachment | `slack` | Inspect parameters |
| Analyze email with Sublime Security | `httpRequest` | POST |

## Connection map

- Move Binary Data → Analyze email with Sublime Security (`main`, output 0, input 0)
- Format the message → Slack (`main`, output 0, input 0)
- Email Trigger (IMAP) → IF email has attachment (`main`, output 0, input 0)
- IF email has attachment → Move Binary Data (`main`, output 0, input 0)
- IF email has attachment → Notify about missing attachment (`main`, output 1, input 0)
- Split to matched and unmatched → Format the message (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Move Binary Data (`main`, output 0, input 0)
- Analyze email with Sublime Security → Split to matched and unmatched (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1161_Code_Slack_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1161_Code_Slack_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
