# Standup Bot - Worker

This folder contains the **Standup Bot - Worker** workflow. Its executable nodes use `cron`, `executeWorkflow`, `function`, `httpRequest`, `if`, `mattermost`, `noOp`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`standup-bot-worker.json`](standup-bot-worker.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mattermostApi`

**Entry nodes:** Action from MM, Slash Cmd from MM, Every hour

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| publish report | `mattermost` | Inspect parameters |
| get user data | `httpRequest` | Inspect parameters |
| open-standup-dialog? | `if` | Inspect parameters |
| Action from MM | `webhook` | Inspect parameters |
| Slash Cmd from MM | `webhook` | Inspect parameters |
| config? | `if` | Inspect parameters |
| open config dialog | `httpRequest` | Inspect parameters |
| Prep Config Dialog | `function` | Inspect parameters |
| callback ID? | `switch` | Inspect parameters |
| standup-config | `noOp` | Inspect parameters |
| standup-answers | `noOp` | Inspect parameters |
| Prep Config Override | `function` | Inspect parameters |
| Override Config | `executeWorkflow` | Inspect parameters |
| Read Config 1 | `executeWorkflow` | Inspect parameters |
| Read Config 2 | `executeWorkflow` | Inspect parameters |
| confirm success | `mattermost` | postEphemeral |
| Read Config 3 | `executeWorkflow` | Inspect parameters |
| Filter Due Standups | `function` | Inspect parameters |
| Prep Request Standup | `function` | Inspect parameters |
| Create Channel | `httpRequest` | Inspect parameters |
| Remind Users | `httpRequest` | Inspect parameters |
| Get User | `httpRequest` | Inspect parameters |
| Prep Reminder | `function` | Inspect parameters |
| Prep Standup Dialog | `function` | Inspect parameters |
| open standup dialog | `httpRequest` | Inspect parameters |
| Prep Report | `function` | Inspect parameters |
| Delete ReminderPost | `mattermost` | delete |
| Update Post | `httpRequest` | Inspect parameters |
| Every hour | `cron` | Inspect parameters |

## Connection map

- config? → Read Config 1 (`main`, output 0, input 0)
- Get User → Create Channel (`main`, output 0, input 0)
- Every hour → Read Config 3 (`main`, output 0, input 0)
- Prep Report → publish report (`main`, output 0, input 0)
- callback ID? → standup-config (`main`, output 0, input 0)
- callback ID? → standup-answers (`main`, output 1, input 0)
- callback ID? → open-standup-dialog? (`main`, output 3, input 0)
- Prep Reminder → Remind Users (`main`, output 0, input 0)
- Read Config 1 → Prep Config Dialog (`main`, output 0, input 0)
- Read Config 2 → callback ID? (`main`, output 0, input 0)
- Read Config 3 → Filter Due Standups (`main`, output 0, input 0)
- get user data → Prep Report (`main`, output 0, input 0)
- Action from MM → Read Config 2 (`main`, output 0, input 0)
- Create Channel → Prep Reminder (`main`, output 0, input 0)
- publish report → Update Post (`main`, output 0, input 0)
- standup-config → Prep Config Override (`main`, output 0, input 0)
- Override Config → confirm success (`main`, output 0, input 0)
- standup-answers → get user data (`main`, output 0, input 0)
- Slash Cmd from MM → config? (`main`, output 0, input 0)
- Prep Config Dialog → open config dialog (`main`, output 0, input 0)
- Filter Due Standups → Prep Request Standup (`main`, output 0, input 0)
- Prep Standup Dialog → open standup dialog (`main`, output 0, input 0)
- Prep Config Override → Override Config (`main`, output 0, input 0)
- Prep Request Standup → Get User (`main`, output 0, input 0)
- open-standup-dialog? → Prep Standup Dialog (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0066_Webhook_Cron_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0066_Webhook_Cron_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
