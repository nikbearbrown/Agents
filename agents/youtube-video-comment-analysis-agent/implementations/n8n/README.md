# 🎦🚀 YouTube Video Comment Analysis Agent

This folder contains the **🎦🚀 YouTube Video Comment Analysis Agent** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `executeWorkflowTrigger`, `gmail`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `merge`, `set`, `splitOut`, `summarize`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-video-comment-analysis-agent.json`](youtube-video-comment-analysis-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Create YouTube API URL | `code` | Inspect parameters |
| Get YouTube Video Details | `httpRequest` | Inspect parameters |
| Merge YouTube Details & Transcript | `merge` | Inspect parameters |
| Create One JSON Object | `aggregate` | Inspect parameters |
| Workflow Variables | `set` | Inspect parameters |
| Combine Comments | `summarize` | Inspect parameters |
| Split Out Comments | `splitOut` | Inspect parameters |
| Get YouTube Video Comments | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Create YouTube API URL for Comments | `code` | Inspect parameters |
| Gmail Report | `gmail` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Markdown to HTML | `markdown` | Inspect parameters |
| YouTube Video Report Agent | `agent` | Inspect parameters |
| Get Video Comments with Pagination | `code` | Inspect parameters |
| Save Report to Google Drive | `googleDrive` | createFromText |

## Connection map

- gpt-4o-mini → YouTube Video Report Agent (`ai_languageModel`, output 0, input 0)
- Combine Comments → Merge YouTube Details & Transcript (`main`, output 0, input 1)
- Markdown to HTML → Gmail Report (`main`, output 0, input 0)
- Markdown to HTML → Save Report to Google Drive (`main`, output 0, input 0)
- Split Out Comments → Combine Comments (`main`, output 0, input 0)
- Workflow Variables → Create YouTube API URL (`main`, output 0, input 0)
- Workflow Variables → Get Video Comments with Pagination (`main`, output 0, input 0)
- Create One JSON Object → YouTube Video Report Agent (`main`, output 0, input 0)
- Create YouTube API URL → Get YouTube Video Details (`main`, output 0, input 0)
- Get YouTube Video Details → Merge YouTube Details & Transcript (`main`, output 0, input 0)
- YouTube Video Report Agent → Markdown to HTML (`main`, output 0, input 0)
- When Executed by Another Workflow → Workflow Variables (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Workflow Variables (`main`, output 0, input 0)
- Get Video Comments with Pagination → Split Out Comments (`main`, output 0, input 0)
- Merge YouTube Details & Transcript → Create One JSON Object (`main`, output 0, input 0)
- Create YouTube API URL for Comments → Get YouTube Video Comments (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1831_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1831_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
