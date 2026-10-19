# html extract and cron and function item

This folder contains the **html extract and cron and function item** workflow. Its executable nodes use `cron`, `emailSend`, `executeCommand`, `functionItem`, `htmlExtract`, `httpRequest`, `if`, `moveBinaryData`, `readBinaryFile`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`html-extract-and-cron-and-function-item.json`](html-extract-and-cron-and-function-item.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| HTML Extract | `htmlExtract` | Inspect parameters |
| Cron | `cron` | Inspect parameters |
| getActualPrice | `functionItem` | Inspect parameters |
| fetchWeb | `httpRequest` | Inspect parameters |
| FunctionItem | `functionItem` | Inspect parameters |
| Write Binary File1 | `writeBinaryFile` | Inspect parameters |
| Move Binary Data1 | `moveBinaryData` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| checkifexists | `executeCommand` | Inspect parameters |
| IF3 | `if` | Inspect parameters |
| SaveToFile | `writeBinaryFile` | Inspect parameters |
| JsonToBinary | `moveBinaryData` | Inspect parameters |
| changeME | `functionItem` | Inspect parameters |
| initItem | `functionItem` | Inspect parameters |
| savedItems | `readBinaryFile` | Inspect parameters |
| itemsToJSON | `moveBinaryData` | Inspect parameters |
| IF | `if` | Inspect parameters |
| initItem1 | `functionItem` | Inspect parameters |
| IF2 | `if` | Inspect parameters |
| updateSavedItems | `functionItem` | Inspect parameters |
| updateSavedItems1 | `functionItem` | Inspect parameters |
| cleanData | `executeCommand` | Inspect parameters |
| IF4 | `if` | Inspect parameters |
| NotifyBetterPrice | `emailSend` | Inspect parameters |
| NotifyIncorrectPrice | `emailSend` | Inspect parameters |

## Connection map

- IF → changeME (`main`, output 0, input 0)
- IF1 → FunctionItem (`main`, output 0, input 0)
- IF1 → IF3 (`main`, output 1, input 0)
- IF2 → NotifyBetterPrice (`main`, output 0, input 0)
- IF2 → IF (`main`, output 1, input 0)
- IF3 → savedItems (`main`, output 0, input 0)
- IF4 → NotifyIncorrectPrice (`main`, output 0, input 0)
- IF4 → checkifexists (`main`, output 1, input 0)
- Cron → initItem1 (`main`, output 0, input 0)
- changeME → initItem (`main`, output 0, input 0)
- fetchWeb → HTML Extract (`main`, output 0, input 0)
- initItem → fetchWeb (`main`, output 0, input 0)
- initItem1 → changeME (`main`, output 0, input 0)
- SaveToFile → IF2 (`main`, output 0, input 0)
- savedItems → itemsToJSON (`main`, output 0, input 0)
- itemsToJSON → updateSavedItems1 (`main`, output 0, input 0)
- FunctionItem → Move Binary Data1 (`main`, output 0, input 0)
- HTML Extract → getActualPrice (`main`, output 0, input 0)
- JsonToBinary → SaveToFile (`main`, output 0, input 0)
- checkifexists → IF1 (`main`, output 0, input 0)
- getActualPrice → IF4 (`main`, output 0, input 0)
- updateSavedItems → JsonToBinary (`main`, output 0, input 0)
- Move Binary Data1 → Write Binary File1 (`main`, output 0, input 0)
- NotifyBetterPrice → IF (`main`, output 0, input 0)
- updateSavedItems1 → updateSavedItems (`main`, output 0, input 0)
- Write Binary File1 → IF (`main`, output 0, input 0)
- NotifyIncorrectPrice → checkifexists (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/1157_Functionitem_Executecommand_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/1157_Functionitem_Executecommand_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
