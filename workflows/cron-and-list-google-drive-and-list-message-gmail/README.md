# Orlen

This folder contains the **Orlen** workflow. Its executable nodes use `cron`, `function`, `gmail`, `googleDrive`, `manualTrigger`, `merge`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cron-and-list-google-drive-and-list-message-gmail.json`](cron-and-list-google-drive-and-list-message-gmail.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `slackOAuth2Api`

**Entry nodes:** On clicking 'execute', Every 23:45

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Current date | `function` | Inspect parameters |
| Every 23:45 | `cron` | Inspect parameters |
| Get Year folder | `googleDrive` | list |
| Get Month folder | `googleDrive` | list |
| Orlen Invoice | `gmail` | message / getAll |
| Upload Invoice to Google Drive | `googleDrive` | Inspect parameters |
| Mark as Read | `gmail` | messageLabel / remove |
| Merge | `merge` | Inspect parameters |
| Slack | `slack` | Inspect parameters |

## Connection map

- Merge → Upload Invoice to Google Drive (`main`, output 0, input 0)
- Every 23:45 → Orlen Invoice (`main`, output 0, input 0)
- Current date → Get Year folder (`main`, output 0, input 0)
- Mark as Read → Slack (`main`, output 0, input 0)
- Orlen Invoice → Merge (`main`, output 0, input 1)
- Get Year folder → Get Month folder (`main`, output 0, input 0)
- Get Month folder → Merge (`main`, output 0, input 0)
- On clicking 'execute' → Orlen Invoice (`main`, output 0, input 0)
- Upload Invoice to Google Drive → Mark as Read (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0940_Slack_Manual_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0940_Slack_Manual_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
