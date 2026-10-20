# 🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive

This folder contains the **🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive** workflow. Its executable nodes use `filter`, `gmail`, `googleDrive`, `googleDriveTrigger`, `limit`, `manualTrigger`, `merge`, `openAi`, `set`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`use-openai-to-transcribe-audio-summarize-with-ai-save-to-google-drive.json`](use-openai-to-transcribe-audio-summarize-with-ai-save-to-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Start Workflow, On File Created Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail User for Approval | `gmail` | sendAndWait |
| Set Config | `set` | Inspect parameters |
| Transcribe with OpenAI | `openAi` | audio / transcribe |
| Filter by .m4a extension | `filter` | Inspect parameters |
| Limit to last file | `limit` | Inspect parameters |
| Download audio file | `googleDrive` | download |
| Search Google Drive | `googleDrive` | fileFolder |
| Send Telegram Message | `telegram` | Inspect parameters |
| Send Gmail Message | `gmail` | Inspect parameters |
| Email Content Formatter | `openAi` | Inspect parameters |
| Summarize to Structured JSON | `openAi` | Inspect parameters |
| Summarize to JSON | `openAi` | Inspect parameters |
| Convert JSON to Markdown | `openAi` | Inspect parameters |
| Get Filename for JSON | `set` | Inspect parameters |
| Get Filename for Markdown | `set` | Inspect parameters |
| Save JSON file to Google Drive | `googleDrive` | createFromText |
| Save Markdown file to Google Drive | `googleDrive` | createFromText |
| Get JSON File Meta | `googleDrive` | fileFolder |
| Get Markdown File Meta | `googleDrive` | fileFolder |
| Prepare Response JSON | `set` | Inspect parameters |
| Prepare Response Markdown | `set` | Inspect parameters |
| Merge All Paths | `merge` | Inspect parameters |
| Save Raw Transcript to Google Drive | `googleDrive` | createFromText |
| Start Workflow | `manualTrigger` | Inspect parameters |
| On File Created Trigger | `googleDriveTrigger` | Inspect parameters |

## Connection map

- Set Config → Summarize to JSON (`main`, output 0, input 0)
- Set Config → Summarize to Structured JSON (`main`, output 0, input 0)
- Set Config → Save Raw Transcript to Google Drive (`main`, output 0, input 0)
- Start Workflow → Search Google Drive (`main`, output 0, input 0)
- Merge All Paths → Send Telegram Message (`main`, output 0, input 0)
- Merge All Paths → Email Content Formatter (`main`, output 0, input 0)
- Summarize to JSON → Convert JSON to Markdown (`main`, output 0, input 0)
- Get JSON File Meta → Prepare Response JSON (`main`, output 0, input 0)
- Limit to last file → Download audio file (`main`, output 0, input 0)
- Download audio file → Transcribe with OpenAI (`main`, output 0, input 0)
- Search Google Drive → Filter by .m4a extension (`main`, output 0, input 0)
- Get Filename for JSON → Save JSON file to Google Drive (`main`, output 0, input 0)
- Prepare Response JSON → Merge All Paths (`main`, output 0, input 0)
- Get Markdown File Meta → Prepare Response Markdown (`main`, output 0, input 0)
- Transcribe with OpenAI → Set Config (`main`, output 0, input 0)
- Email Content Formatter → Send Gmail Message (`main`, output 0, input 0)
- Gmail User for Approval → Search Google Drive (`main`, output 0, input 0)
- On File Created Trigger → Gmail User for Approval (`main`, output 0, input 0)
- Convert JSON to Markdown → Get Filename for Markdown (`main`, output 0, input 0)
- Filter by .m4a extension → Limit to last file (`main`, output 0, input 0)
- Get Filename for Markdown → Save Markdown file to Google Drive (`main`, output 0, input 0)
- Prepare Response Markdown → Merge All Paths (`main`, output 0, input 1)
- Summarize to Structured JSON → Get Filename for JSON (`main`, output 0, input 0)
- Save JSON file to Google Drive → Get JSON File Meta (`main`, output 0, input 0)
- Save Markdown file to Google Drive → Get Markdown File Meta (`main`, output 0, input 0)
- Save Raw Transcript to Google Drive → Merge All Paths (`main`, output 0, input 2)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1368_Telegram_Limit_Export_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1368_Telegram_Limit_Export_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
