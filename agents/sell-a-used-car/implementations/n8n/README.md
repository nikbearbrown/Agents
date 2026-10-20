# Sell a Used Car

This folder contains the **Sell a Used Car** workflow. Its executable nodes use `airtop`, `code`, `manualTrigger`, `set`, `switch`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sell-a-used-car.json`](sell-a-used-car.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtopApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Variables | `set` | Inspect parameters |
| Wait 7 secs | `wait` | Inspect parameters |
| Parse response | `code` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Offer received | `set` | Inspect parameters |
| Type | `airtop` | interaction / type |
| Click | `airtop` | interaction |
| Create session | `airtop` | Inspect parameters |
| Load website | `airtop` | window |
| Click VIN button | `airtop` | interaction |
| Terminate session | `airtop` | terminate |
| Take screenshot | `airtop` | window / takeScreenshot |
| Think next action | `airtop` | extraction / query |

## Connection map

- Type → Wait 7 secs (`main`, output 0, input 0)
- Click → Wait 7 secs (`main`, output 0, input 0)
- Switch → Type (`main`, output 0, input 0)
- Switch → Click (`main`, output 1, input 0)
- Switch → Offer received (`main`, output 2, input 0)
- Variables → Create session (`main`, output 0, input 0)
- Wait 7 secs → Take screenshot (`main`, output 0, input 0)
- Load website → Click VIN button (`main`, output 0, input 0)
- Create session → Load website (`main`, output 0, input 0)
- Offer received → Terminate session (`main`, output 0, input 0)
- Parse response → Switch (`main`, output 0, input 0)
- Take screenshot → Think next action (`main`, output 0, input 0)
- Click VIN button → Wait 7 secs (`main`, output 0, input 0)
- Think next action → Parse response (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1735_Manual_Airtop_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1735_Manual_Airtop_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
