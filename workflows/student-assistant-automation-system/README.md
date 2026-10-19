# Student Assistant Automation System

This folder contains the **Student Assistant Automation System** workflow. Its executable nodes use `code`, `discord`, `gmailTrigger`, `googleSheets`, `if`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`student-assistant-automation-system.json`](student-assistant-automation-system.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordWebhookApi`, `gmailOAuth2`, `googleSheetsOAuth2Api`

**Entry nodes:** Gmail Trigger, Schedule Trigger, Schedule Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| Code in JavaScript | `code` | Inspect parameters |
| Code in JavaScript1 | `code` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Code in JavaScript2 | `code` | Inspect parameters |
| 2 days filter | `code` | Inspect parameters |
| combine | `code` | Inspect parameters |
| deadline | `discord` | Inspect parameters |
| schedule | `discord` | Inspect parameters |
| emails | `discord` | Inspect parameters |
| Code in JavaScript3 | `code` | Inspect parameters |
| Delete rows or columns from sheet | `googleSheets` | delete |
| time table | `googleSheets` | Inspect parameters |
| deadline1 | `googleSheets` | Inspect parameters |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |

## Connection map

- Gmail Trigger → Code in JavaScript2 (`main`, output 0, input 0)
- If → Code in JavaScript1 (`main`, output 0, input 0)
- Code in JavaScript → If (`main`, output 0, input 0)
- Code in JavaScript1 → schedule (`main`, output 0, input 0)
- Schedule Trigger → time table (`main`, output 0, input 0)
- Code in JavaScript2 → emails (`main`, output 0, input 0)
- 2 days filter → combine (`main`, output 0, input 0)
- combine → deadline (`main`, output 0, input 0)
- Code in JavaScript3 → Delete rows or columns from sheet (`main`, output 0, input 0)
- time table → Code in JavaScript (`main`, output 0, input 0)
- deadline1 → Code in JavaScript3 (`main`, output 0, input 0)
- deadline1 → 2 days filter (`main`, output 0, input 0)
- Schedule Trigger1 → deadline1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/nadjibdje/Student-Assistant-Automation-System/blob/c3907654055b9d0481fe4cc345da019801e3817e/main.json](https://github.com/nadjibdje/Student-Assistant-Automation-System/blob/c3907654055b9d0481fe4cc345da019801e3817e/main.json). License: **MIT**; preserve [the notice](../../licenses/nadjibdje--Student-Assistant-Automation-System.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
