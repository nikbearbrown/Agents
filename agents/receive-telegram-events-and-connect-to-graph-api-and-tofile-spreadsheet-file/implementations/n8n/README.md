# receive telegram events and connect to graph api and tofile spreadsheet file

This folder contains the **receive telegram events and connect to graph api and tofile spreadsheet file** workflow. Its executable nodes use `code`, `facebookGraphApi`, `if`, `noOp`, `spreadsheetFile`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-connect-to-graph-api-and-tofile-spreadsheet-file.json`](receive-telegram-events-and-connect-to-graph-api-and-tofile-spreadsheet-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `telegramApi`

**Entry nodes:** Get interest name

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| No Operation, do nothing | `noOp` | Inspect parameters |
| Get interest name | `telegramTrigger` | Inspect parameters |
| Check message contents | `if` | Inspect parameters |
| Extract message | `code` | Inspect parameters |
| Split Message | `code` | Inspect parameters |
| Connect to Graph API | `facebookGraphApi` | Inspect parameters |
| Split Interests into a Table | `code` | Inspect parameters |
| Get variables | `code` | Inspect parameters |
| Create a Spreadsheet | `spreadsheetFile` | toFile |
| Send the Spreadsheet file | `telegram` | sendDocument |

## Connection map

- Get variables → Create a Spreadsheet (`main`, output 0, input 0)
- Split Message → Connect to Graph API (`main`, output 0, input 0)
- Extract message → Split Message (`main`, output 0, input 0)
- Get interest name → Check message contents (`main`, output 0, input 0)
- Connect to Graph API → Split Interests into a Table (`main`, output 0, input 0)
- Create a Spreadsheet → Send the Spreadsheet file (`main`, output 0, input 0)
- Check message contents → Extract message (`main`, output 0, input 0)
- Check message contents → No Operation, do nothing (`main`, output 1, input 0)
- Split Interests into a Table → Get variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0388_Telegram_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0388_Telegram_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
