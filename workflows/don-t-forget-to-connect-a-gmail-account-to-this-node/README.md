# Don't forget to connect a GMail account to this node!

This folder contains the **Don't forget to connect a GMail account to this node!** workflow. Its executable nodes use `code`, `gmail`, `htmlExtract`, `httpRequest`, `if`, `itemLists`, `scheduleTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`don-t-forget-to-connect-a-gmail-account-to-this-node.json`](don-t-forget-to-connect-a-gmail-account-to-this-node.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** 🤖 Each month

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get events page | `httpRequest` | Inspect parameters |
| Last page? | `if` | Inspect parameters |
| Get all events from the page | `htmlExtract` | Inspect parameters |
| Get each event data | `htmlExtract` | Inspect parameters |
| Limit to one | `itemLists` | limit |
| Wait 3s | `wait` | Inspect parameters |
| Split events | `itemLists` | Inspect parameters |
| Collect all results | `code` | Inspect parameters |
| 🤖 Each month | `scheduleTrigger` | Inspect parameters |
| Setup location and email | `set` | Inspect parameters |
| 💄 Lick the stamp | `code` | Inspect parameters |
| ✉️ Send it | `gmail` | Inspect parameters |

## Connection map

- Wait 3s → Limit to one (`main`, output 0, input 0)
- Last page? → Collect all results (`main`, output 0, input 0)
- Last page? → Wait 3s (`main`, output 1, input 0)
- Limit to one → Setup location and email (`main`, output 0, input 0)
- Split events → Last page? (`main`, output 0, input 0)
- Get events page → Get all events from the page (`main`, output 0, input 0)
- 🤖 Each month → Setup location and email (`main`, output 0, input 0)
- Collect all results → Get each event data (`main`, output 0, input 0)
- Get each event data → 💄 Lick the stamp (`main`, output 0, input 0)
- 💄 Lick the stamp → ✉️ Send it (`main`, output 0, input 0)
- Setup location and email → Get events page (`main`, output 0, input 0)
- Get all events from the page → Split events (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0385_Wait_Code_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0385_Wait_Code_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
