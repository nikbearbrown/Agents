# New member or Member left

This folder contains the **New member or Member left** workflow. Its executable nodes use `executeWorkflow`, `googleSheets`, `if`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`new-member-or-member-left.json`](new-member-or-member-left.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `telegramApi`

**Entry nodes:** Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Trigger | `telegramTrigger` | Inspect parameters |
| Global data | `set` | Inspect parameters |
| Telegram1 | `telegram` | Inspect parameters |
| Telegram2 | `telegram` | Inspect parameters |
| Telegram3 | `telegram` | Inspect parameters |
| Telegram4 | `telegram` | Inspect parameters |
| Telegram5 | `telegram` | Inspect parameters |
| Switch_MessageType | `switch` | Inspect parameters |
| Telegram6 | `telegram` | Inspect parameters |
| Menu | `switch` | Inspect parameters |
| Command? | `if` | Inspect parameters |
| Change status | `googleSheets` | update |
| Start bot? | `if` | Inspect parameters |
| Register | `executeWorkflow` | Inspect parameters |
| Payment Handler | `executeWorkflow` | Inspect parameters |
| Trigger Data for Payment | `set` | Inspect parameters |
| Trigger Data for Register | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Data for Invoice | `set` | Inspect parameters |
| Send Invoice | `executeWorkflow` | Inspect parameters |
| Switch_Commands | `switch` | Inspect parameters |

## Connection map

- Switch → Switch_MessageType (`main`, output 0, input 0)
- Switch → Telegram3 (`main`, output 1, input 0)
- Switch → Start bot? (`main`, output 2, input 0)
- Switch → Trigger Data for Payment (`main`, output 3, input 0)
- Trigger → Global data (`main`, output 0, input 0)
- Command? → Switch_Commands (`main`, output 0, input 0)
- Command? → Telegram4 (`main`, output 1, input 0)
- Telegram3 → Menu (`main`, output 0, input 0)
- Start bot? → Trigger Data for Register (`main`, output 0, input 0)
- Start bot? → Change status (`main`, output 1, input 0)
- Global data → Switch (`main`, output 0, input 0)
- Switch_Commands → Data for Invoice (`main`, output 0, input 0)
- Switch_Commands → Telegram6 (`main`, output 1, input 0)
- Data for Invoice → Send Invoice (`main`, output 0, input 0)
- Switch_MessageType → Command? (`main`, output 0, input 0)
- Switch_MessageType → Telegram1 (`main`, output 1, input 0)
- Switch_MessageType → Telegram2 (`main`, output 2, input 0)
- Switch_MessageType → Telegram5 (`main`, output 3, input 0)
- Trigger Data for Payment → Payment Handler (`main`, output 0, input 0)
- Trigger Data for Register → Register (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0569_Executeworkflow_Telegram_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0569_Executeworkflow_Telegram_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
