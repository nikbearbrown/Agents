# 🎥 Analyze YouTube Video for Summaries, Transcripts & Content + Google Gemini AI

This folder contains the **🎥 Analyze YouTube Video for Summaries, Transcripts & Content + Google Gemini AI** workflow. Its executable nodes use `code`, `form`, `formTrigger`, `gmail`, `googleDrive`, `httpRequest`, `markdown`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`analyze-youtube-video-for-summaries-transcripts-content-google-gemini-ai.json`](analyze-youtube-video-for-summaries-transcripts-content-google-gemini-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`

**Entry nodes:** Start Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Config | `set` | Inspect parameters |
| Get Video Audience MetaData | `httpRequest` | POST |
| Compose Prompts | `set` | Inspect parameters |
| Extract MetaData Object | `set` | Inspect parameters |
| Get Prompt by Prompt Type | `code` | Inspect parameters |
| Define Audience Meta Prompt | `set` | Inspect parameters |
| Get YouTube Information by Prompt Type | `httpRequest` | POST |
| Save to Google Drive as Text File | `googleDrive` | createFromText |
| Send to Gmail as HTML | `gmail` | Inspect parameters |
| Convert Markdown to HTML | `markdown` | Inspect parameters |
| Provide YouTube Information to User as HTML | `form` | completion |
| Start Workflow | `formTrigger` | Inspect parameters |
| Create YouTube API URL | `code` | Inspect parameters |
| Get YouTube Video Details | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |

## Connection map

- Merge → Compose Prompts (`main`, output 0, input 0)
- Config → Create YouTube API URL (`main`, output 0, input 0)
- Config → Define Audience Meta Prompt (`main`, output 0, input 0)
- Start Workflow → Config (`main`, output 0, input 0)
- Compose Prompts → Get Prompt by Prompt Type (`main`, output 0, input 0)
- Create YouTube API URL → Get YouTube Video Details (`main`, output 0, input 0)
- Extract MetaData Object → Merge (`main`, output 0, input 1)
- Convert Markdown to HTML → Send to Gmail as HTML (`main`, output 0, input 0)
- Convert Markdown to HTML → Provide YouTube Information to User as HTML (`main`, output 0, input 0)
- Get Prompt by Prompt Type → Get YouTube Information by Prompt Type (`main`, output 0, input 0)
- Get YouTube Video Details → Merge (`main`, output 0, input 0)
- Define Audience Meta Prompt → Get Video Audience MetaData (`main`, output 0, input 0)
- Get Video Audience MetaData → Extract MetaData Object (`main`, output 0, input 0)
- Get YouTube Information by Prompt Type → Convert Markdown to HTML (`main`, output 0, input 0)
- Get YouTube Information by Prompt Type → Save to Google Drive as Text File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1313_Code_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1313_Code_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
