# sort item lists and markdown and email send

This folder contains the **sort item lists and markdown and email send** workflow. Its executable nodes use `emailSend`, `function`, `httpRequest`, `itemLists`, `manualTrigger`, `markdown`, `merge`, `moveBinaryData`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sort-item-lists-and-markdown-and-email-send.json`](sort-item-lists-and-markdown-and-email-send.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| SortElements | `itemLists` | sort |
| Markdown | `markdown` | Inspect parameters |
| CreateMDReport | `function` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| GetImg | `itemLists` | removeDuplicates |
| ImgBinary | `httpRequest` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Move Binary Data1 | `moveBinaryData` | Inspect parameters |
| GetTimesheetRecords | `function` | Inspect parameters |

## Connection map

- GetImg → ImgBinary (`main`, output 0, input 0)
- Merge2 → CreateMDReport (`main`, output 0, input 0)
- Markdown → Move Binary Data1 (`main`, output 0, input 0)
- ImgBinary → Merge2 (`main`, output 0, input 1)
- SortElements → GetImg (`main`, output 0, input 0)
- SortElements → Merge2 (`main`, output 0, input 0)
- CreateMDReport → Markdown (`main`, output 0, input 0)
- Move Binary Data1 → Send Email (`main`, output 0, input 0)
- GetTimesheetRecords → SortElements (`main`, output 0, input 0)
- On clicking 'execute' → GetTimesheetRecords (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0214_Manual_Markdown_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0214_Manual_Markdown_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
