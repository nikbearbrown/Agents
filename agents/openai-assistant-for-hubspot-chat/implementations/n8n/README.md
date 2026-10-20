# OpenAI Assistant for Hubspot Chat

This folder contains the **OpenAI Assistant for Hubspot Chat** workflow. Its executable nodes use `airtable`, `code`, `httpRequest`, `if`, `openAi`, `switch`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`openai-assistant-for-hubspot-chat.json`](openai-assistant-for-hubspot-chat.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `hubspotAppToken`, `hubspotDeveloperApi`, `hubspotOAuth2Api`, `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| getHubspotMessage | `httpRequest` | Inspect parameters |
| OpenAi Create Thread | `httpRequest` | POST |
| OpenAI Run | `httpRequest` | POST |
| Get Run | `httpRequest` | Inspect parameters |
| Get Last Message | `httpRequest` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Completed, Action or Inprogress | `switch` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Submit Data | `httpRequest` | POST |
| Select Function | `switch` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| HTTP Request1 | `httpRequest` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Submit Data1 | `httpRequest` | POST |
| Wait3 | `wait` | Inspect parameters |
| respondHubspotMessage1 | `httpRequest` | POST |
| IF | `if` | Inspect parameters |
| Airtable | `airtable` | search |
| IF1 | `if` | Inspect parameters |
| createThread | `airtable` | create |
| OpenAI Run1 | `httpRequest` | POST |
| IF2 | `if` | Inspect parameters |
| OpenAI | `openAi` | assistant |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- IF → Airtable (`main`, output 0, input 0)
- IF1 → OpenAi Create Thread (`main`, output 0, input 0)
- IF1 → OpenAI (`main`, output 1, input 0)
- IF2 → getHubspotMessage (`main`, output 0, input 0)
- Code → Submit Data1 (`main`, output 0, input 0)
- Wait → Get Run (`main`, output 0, input 0)
- Code1 → Submit Data (`main`, output 0, input 0)
- Wait1 → Get Run (`main`, output 0, input 0)
- Wait2 → Get Run (`main`, output 0, input 0)
- Wait3 → Get Run (`main`, output 0, input 0)
- OpenAI → OpenAI Run1 (`main`, output 0, input 0)
- Get Run → Completed, Action or Inprogress (`main`, output 0, input 0)
- Webhook → IF2 (`main`, output 0, input 0)
- Airtable → IF1 (`main`, output 0, input 0)
- OpenAI Run → Get Run (`main`, output 0, input 0)
- OpenAI Run1 → Get Run (`main`, output 0, input 0)
- Submit Data → Wait2 (`main`, output 0, input 0)
- HTTP Request → Code1 (`main`, output 0, input 0)
- Submit Data1 → Wait3 (`main`, output 0, input 0)
- createThread → OpenAI Run (`main`, output 0, input 0)
- HTTP Request1 → Code (`main`, output 0, input 0)
- Select Function → HTTP Request (`main`, output 0, input 0)
- Select Function → HTTP Request1 (`main`, output 1, input 0)
- Get Last Message → respondHubspotMessage1 (`main`, output 0, input 0)
- getHubspotMessage → IF (`main`, output 0, input 0)
- OpenAi Create Thread → createThread (`main`, output 0, input 0)
- Completed, Action or Inprogress → Get Last Message (`main`, output 0, input 0)
- Completed, Action or Inprogress → Select Function (`main`, output 1, input 0)
- Completed, Action or Inprogress → Wait1 (`main`, output 2, input 0)
- Completed, Action or Inprogress → Wait (`main`, output 3, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1990_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1990_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
