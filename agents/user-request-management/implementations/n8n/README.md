# User Request Management

This folder contains the **User Request Management** workflow. Its executable nodes use `clickUp`, `set`, `switch`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`user-request-management.json`](user-request-management.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clickUpOAuth2Api`, `typeformApi`

**Entry nodes:** Typeform Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| ClickUp | `clickUp` | Inspect parameters |
| Typeform Trigger | `typeformTrigger` | Inspect parameters |
| ListID 54684957 | `set` | Inspect parameters |
| ListID 54685003 | `set` | Inspect parameters |
| ListID 54685000 | `set` | Inspect parameters |
| ListID 54684997 | `set` | Inspect parameters |
| Pick List | `switch` | Inspect parameters |

## Connection map

- Pick List → ListID 54685003 (`main`, output 0, input 0)
- Pick List → ListID 54685000 (`main`, output 1, input 0)
- Pick List → ListID 54684957 (`main`, output 2, input 0)
- Pick List → ListID 54684997 (`main`, output 3, input 0)
- ListID 54684957 → ClickUp (`main`, output 0, input 0)
- ListID 54684997 → ClickUp (`main`, output 0, input 0)
- ListID 54685000 → ClickUp (`main`, output 0, input 0)
- ListID 54685003 → ClickUp (`main`, output 0, input 0)
- Typeform Trigger → Pick List (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Typeform/0215_Typeform_Clickup_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Typeform/0215_Typeform_Clickup_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
