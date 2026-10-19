# append google sheets and get aws transcribe and aws transcribe 1

This folder contains the **append google sheets and get aws transcribe and aws transcribe 1** workflow. Its executable nodes use `awsS3`, `awsTranscribe`, `googleDriveTrigger`, `googleSheets`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`append-google-sheets-and-get-aws-transcribe-and-aws-transcribe-1.json`](append-google-sheets-and-get-aws-transcribe-and-aws-transcribe-1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `aws`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Google Drive Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Sheets | `googleSheets` | append |
| AWS Transcribe 2 | `awsTranscribe` | get |
| AWS Transcribe 1 | `awsTranscribe` | Inspect parameters |
| AWS S3 1 | `awsS3` | upload |
| AWS S3 2 | `awsS3` | getAll |
| Set | `set` | Inspect parameters |
| Google Drive Trigger1 | `googleDriveTrigger` | Inspect parameters |
| Wait | `wait` | Inspect parameters |

## Connection map

- Set → Google Sheets (`main`, output 0, input 0)
- Wait → AWS Transcribe 2 (`main`, output 0, input 0)
- AWS S3 1 → AWS S3 2 (`main`, output 0, input 0)
- AWS S3 2 → AWS Transcribe 1 (`main`, output 0, input 0)
- AWS Transcribe 1 → Wait (`main`, output 0, input 0)
- AWS Transcribe 2 → Set (`main`, output 0, input 0)
- Google Drive Trigger1 → AWS S3 1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Awss3/0149_Awss3_Wait_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Awss3/0149_Awss3_Wait_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
