# Simple conversion to XML

This folder contains the **Simple conversion to XML** workflow. Its executable nodes use `itemLists`, `manualTrigger`, `moveBinaryData`, `mySql`, `set`, `writeBinaryFile`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`simple-conversion-to-xml.json`](simple-conversion-to-xml.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Show 16 random products | `mySql` | executeQuery |
| Define file structure | `set` | Inspect parameters |
| Concatenate Items | `itemLists` | concatenateItems |
| Convert to XML | `xml` | Inspect parameters |
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| Define file structure1 | `set` | Inspect parameters |
| Concatenate Items1 | `itemLists` | concatenateItems |
| Convert to XML1 | `xml` | Inspect parameters |
| Move Binary Data1 | `moveBinaryData` | Inspect parameters |
| Write Binary File | `writeBinaryFile` | Inspect parameters |

## Connection map

- Convert to XML → Move Binary Data (`main`, output 0, input 0)
- Convert to XML1 → Move Binary Data1 (`main`, output 0, input 0)
- Move Binary Data → Write Binary File (`main`, output 0, input 0)
- Concatenate Items → Convert to XML (`main`, output 0, input 0)
- Move Binary Data1 → Write Binary File (`main`, output 0, input 0)
- Concatenate Items1 → Convert to XML1 (`main`, output 0, input 0)
- Define file structure → Concatenate Items (`main`, output 0, input 0)
- Define file structure1 → Concatenate Items1 (`main`, output 0, input 0)
- Show 16 random products → Define file structure (`main`, output 0, input 0)
- Show 16 random products → Define file structure1 (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Show 16 random products (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0317_Manual_Movebinarydata_Process_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0317_Manual_Movebinarydata_Process_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
