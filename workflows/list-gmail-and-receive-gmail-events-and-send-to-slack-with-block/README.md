# 外送記帳

This folder contains the **外送記帳** workflow. Its executable nodes use `gmail`, `gmailTrigger`, `manualTrigger`, `set`, `slack`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-gmail-and-receive-gmail-events-and-send-to-slack-with-block.json`](list-gmail-and-receive-gmail-events-and-send-to-slack-with-block.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `slackOAuth2Api`

**Entry nodes:** Click to Test Flow, Receive certain keyword Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Click to Test Flow | `manualTrigger` | Inspect parameters |
| Get emails from Gmail with certain subject | `gmail` | getAll |
| Receive certain keyword Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Extract Price, Shop, Date, TIme | `set` | Inspect parameters |
| Send to Slack with Block | `slack` | Inspect parameters |

## Connection map

- Loop Over Items → Extract Price, Shop, Date, TIme (`main`, output 1, input 0)
- Click to Test Flow → Get emails from Gmail with certain subject (`main`, output 0, input 0)
- Send to Slack with Block → Loop Over Items (`main`, output 0, input 0)
- Extract Price, Shop, Date, TIme → Send to Slack with Block (`main`, output 0, input 0)
- Receive certain keyword Gmail Trigger → Loop Over Items (`main`, output 0, input 0)
- Get emails from Gmail with certain subject → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1835_Manual_Slack_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1835_Manual_Slack_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
