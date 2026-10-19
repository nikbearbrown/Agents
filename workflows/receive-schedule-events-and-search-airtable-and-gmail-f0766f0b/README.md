# receive schedule events and search airtable and gmail f0766f0b

This folder contains the **receive schedule events and search airtable and gmail f0766f0b** workflow. Its executable nodes use `agent`, `airtable`, `code`, `editImage`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `filter`, `formTrigger`, `gmail`, `lmChatGroq`, `memoryBufferWindow`, `openAi`, `scheduleTrigger`, `set`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-search-airtable-and-gmail-f0766f0b.json`](receive-schedule-events-and-search-airtable-and-gmail-f0766f0b.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`, `groqApi`, `openAiApi`

**Entry nodes:** Schedule Trigger, Execute Workflow Trigger, Unsubscribe Form, Subscribe Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Search daily | `airtable` | search |
| Search weekly | `airtable` | search |
| confirmation email1 | `gmail` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Create Event | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Unsubscribe Form | `formTrigger` | Inspect parameters |
| Set Email Vars | `set` | Inspect parameters |
| Log Last Sent | `airtable` | update |
| Search surprise | `airtable` | search |
| Should Send = True | `filter` | Inspect parameters |
| Should Send? | `code` | Inspect parameters |
| Create Subscriber | `airtable` | upsert |
| Update Subscriber | `airtable` | update |
| Subscribe Form | `formTrigger` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Content Generation Agent | `agent` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Generate Image | `openAi` | image |
| Resize Image | `editImage` | resize |
| Send Message | `gmail` | Inspect parameters |

## Connection map

- Wikipedia → Content Generation Agent (`ai_tool`, output 0, input 0)
- Create Event → Execute Workflow (`main`, output 0, input 0)
- Resize Image → Set Email Vars (`main`, output 0, input 0)
- Search daily → Create Event (`main`, output 0, input 0)
- Send Message → Log Last Sent (`main`, output 0, input 0)
- Should Send? → Should Send = True (`main`, output 0, input 0)
- Search weekly → Create Event (`main`, output 0, input 0)
- Execution Data → Content Generation Agent (`main`, output 0, input 0)
- Generate Image → Resize Image (`main`, output 0, input 0)
- Set Email Vars → Send Message (`main`, output 0, input 0)
- Subscribe Form → Create Subscriber (`main`, output 0, input 0)
- Groq Chat Model → Content Generation Agent (`ai_languageModel`, output 0, input 0)
- Search surprise → Should Send? (`main`, output 0, input 0)
- Schedule Trigger → Search surprise (`main`, output 0, input 0)
- Schedule Trigger → Search daily (`main`, output 0, input 0)
- Schedule Trigger → Search weekly (`main`, output 0, input 0)
- Unsubscribe Form → Update Subscriber (`main`, output 0, input 0)
- Create Subscriber → confirmation email1 (`main`, output 0, input 0)
- Should Send = True → Create Event (`main`, output 0, input 0)
- Window Buffer Memory → Content Generation Agent (`ai_memory`, output 0, input 0)
- Content Generation Agent → Generate Image (`main`, output 0, input 0)
- Execute Workflow Trigger → Execution Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 6 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1428_Code_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1428_Code_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
