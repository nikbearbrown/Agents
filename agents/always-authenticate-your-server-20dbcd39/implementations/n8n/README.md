# Always Authenticate Your Server!

This folder contains the **Always Authenticate Your Server!** workflow. Its executable nodes use `executeWorkflowTrigger`, `extractFromFile`, `googleDrive`, `googleDriveTool`, `mcpTrigger`, `openAi`, `set`, `switch`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`always-authenticate-your-server-20dbcd39.json`](always-authenticate-your-server-20dbcd39.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow, Google Drive MCP Server

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Google Drive MCP Server | `mcpTrigger` | Inspect parameters |
| Download File1 | `googleDrive` | download |
| FileType | `switch` | Inspect parameters |
| Operation | `switch` | Inspect parameters |
| Extract from PDF | `extractFromFile` | pdf |
| Extract from CSV | `extractFromFile` | Inspect parameters |
| Get PDF Response | `set` | Inspect parameters |
| Get CSV Response | `set` | Inspect parameters |
| Read File From GDrive | `toolWorkflow` | Inspect parameters |
| Search Files from Gdrive | `googleDriveTool` | fileFolder |
| Analyse Image | `openAi` | image / analyze |
| Transcribe Audio | `openAi` | audio / transcribe |

## Connection map

- FileType → Extract from PDF (`main`, output 0, input 0)
- FileType → Extract from CSV (`main`, output 1, input 0)
- FileType → Analyse Image (`main`, output 2, input 0)
- FileType → Transcribe Audio (`main`, output 3, input 0)
- Operation → Download File1 (`main`, output 0, input 0)
- Download File1 → FileType (`main`, output 0, input 0)
- Extract from CSV → Get CSV Response (`main`, output 0, input 0)
- Extract from PDF → Get PDF Response (`main`, output 0, input 0)
- Read File From GDrive → Google Drive MCP Server (`ai_tool`, output 0, input 0)
- Search Files from Gdrive → Google Drive MCP Server (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → Operation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledrivetool/0875_Googledrivetool_Extractfromfile_Import_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googledrivetool/0875_Googledrivetool_Extractfromfile_Import_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
