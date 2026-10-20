# Example subworkflow for command WITHOUT Slack thread..

This folder contains the **Example subworkflow for command WITHOUT Slack thread..** workflow. Its executable nodes use `code`, `executeWorkflow`, `executeWorkflowTrigger`, `httpRequest`, `if`, `merge`, `postgres`, `set`, `slack`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`example-subworkflow-for-command-without-slack-thread.json`](example-subworkflow-for-command-without-slack-thread.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`

**Entry nodes:** Webhook to call for Slack command, Command workflow trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start thread | `slack` | Inspect parameters |
| send help | `httpRequest` | Inspect parameters |
| Validate Slack token | `if` | Inspect parameters |
| Reply to user that command was received | `httpRequest` | Inspect parameters |
| if has workflow | `if` | Inspect parameters |
| Set config | `set` | Inspect parameters |
| Send debug url | `httpRequest` | Inspect parameters |
| if create thread | `if` | Inspect parameters |
| Alert user that thread was created | `httpRequest` | Inspect parameters |
| Add debug info | `slack` | Inspect parameters |
| Execute target workflow | `executeWorkflow` | Inspect parameters |
| Add thread info | `merge` | Inspect parameters |
| Handle other commands | `switch` | Inspect parameters |
| Set thread info | `set` | Inspect parameters |
| Unknown command | `httpRequest` | Inspect parameters |
| Set vars | `set` | Inspect parameters |
| Webhook to call for Slack command | `webhook` | Inspect parameters |
| Reply to user directly | `httpRequest` | Inspect parameters |
| Command workflow trigger | `executeWorkflowTrigger` | Inspect parameters |
| if has flag | `if` | Inspect parameters |
| If matches env variable | `if` | Inspect parameters |
| Found user | `httpRequest` | Inspect parameters |
| Format data into nice structure | `code` | Inspect parameters |
| REPLACE ME WITH TRIGGER | `set` | Inspect parameters |
| Delete user here for example | `postgres` | deleteTable |
| Get user here for example | `postgres` | select |
| Confirm user was deleted | `slack` | Inspect parameters |
| Replying to thread | `slack` | Inspect parameters |
| parse command | `code` | Inspect parameters |
| Validate webhook signature | `code` | Inspect parameters |

## Connection map

- Set vars → Set config (`main`, output 0, input 0)
- Set config → Validate webhook signature (`main`, output 0, input 0)
- if has flag → If matches env variable (`main`, output 0, input 0)
- Start thread → Add debug info (`main`, output 0, input 0)
- Start thread → Set thread info (`main`, output 0, input 0)
- parse command → if has workflow (`main`, output 0, input 0)
- Add thread info → Execute target workflow (`main`, output 0, input 0)
- Set thread info → Add thread info (`main`, output 0, input 0)
- if has workflow → if create thread (`main`, output 0, input 0)
- if has workflow → Handle other commands (`main`, output 1, input 0)
- if create thread → Start thread (`main`, output 0, input 0)
- if create thread → Alert user that thread was created (`main`, output 0, input 0)
- if create thread → Add thread info (`main`, output 0, input 1)
- if create thread → Send debug url (`main`, output 1, input 0)
- if create thread → Execute target workflow (`main`, output 1, input 0)
- Validate Slack token → Reply to user that command was received (`main`, output 0, input 0)
- Validate Slack token → parse command (`main`, output 0, input 0)
- Handle other commands → send help (`main`, output 0, input 0)
- Handle other commands → Unknown command (`main`, output 1, input 0)
- If matches env variable → Get user here for example (`main`, output 0, input 0)
- REPLACE ME WITH TRIGGER → Replying to thread (`main`, output 0, input 0)
- REPLACE ME WITH TRIGGER → Delete user here for example (`main`, output 0, input 0)
- Command workflow trigger → Reply to user directly (`main`, output 0, input 0)
- Command workflow trigger → if has flag (`main`, output 0, input 0)
- Get user here for example → Format data into nice structure (`main`, output 0, input 0)
- Validate webhook signature → Validate Slack token (`main`, output 0, input 0)
- Delete user here for example → Confirm user was deleted (`main`, output 0, input 0)
- Format data into nice structure → Found user (`main`, output 0, input 0)
- Webhook to call for Slack command → Set vars (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0453_Webhook_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0453_Webhook_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
