# google drive list files1 and executequery postgres and download google drive

This folder contains the **google drive list files1 and executequery postgres and download google drive** workflow. Its executable nodes use `code`, `extractFromFile`, `googleDrive`, `httpRequest`, `manualTrigger`, `postgres`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-drive-list-files1-and-executequery-postgres-and-download-google-drive.json`](google-drive-list-files1-and-executequery-postgres-and-download-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `postgres`

**Entry nodes:** When clicking Test workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking Test workflow | `manualTrigger` | Inspect parameters |
| Google Drive - List Files1 | `googleDrive` | fileFolder |
| Delete old chunks | `postgres` | executeQuery |
| Google Drive - Download File1 | `googleDrive` | download |
| Extract PDF Text | `extractFromFile` | pdf |
| Parse File to Text1 | `code` | Inspect parameters |
| Chunk Text1 | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Ollama - Embed Chunk1 | `httpRequest` | POST |
| Merge Embedding + Metadata1 | `code` | Inspect parameters |
| Supabase - Replace Chunk1 | `postgres` | executeQuery |

## Connection map

- When clicking Test workflow → Google Drive - List Files1 (`main`, output 0, input 0)
- Google Drive - List Files1 → Delete old chunks (`main`, output 0, input 0)
- Delete old chunks → Google Drive - Download File1 (`main`, output 0, input 0)
- Google Drive - Download File1 → Extract PDF Text (`main`, output 0, input 0)
- Extract PDF Text → Parse File to Text1 (`main`, output 0, input 0)
- Parse File to Text1 → Chunk Text1 (`main`, output 0, input 0)
- Chunk Text1 → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Merge Embedding + Metadata1 (`main`, output 0, input 0)
- Loop Over Items → Ollama - Embed Chunk1 (`main`, output 1, input 0)
- Ollama - Embed Chunk1 → Loop Over Items (`main`, output 0, input 0)
- Merge Embedding + Metadata1 → Supabase - Replace Chunk1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/TahsinTanni/RAG-slackbot/blob/f51615aee91eb029228fc0a9853df0ad2cd5d0b0/index.json](https://github.com/TahsinTanni/RAG-slackbot/blob/f51615aee91eb029228fc0a9853df0ad2cd5d0b0/index.json). License: **MIT**; preserve [the notice](../../licenses/TahsinTanni--RAG-slackbot.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
