# Email mailbox as Todoist tasks

This folder contains the **Email mailbox as Todoist tasks** workflow. Its executable nodes use `agent`, `emailReadImap`, `gmail`, `if`, `lmChatOpenAi`, `manualTrigger`, `merge`, `noOp`, `outputParserStructured`, `scheduleTrigger`, `todoist`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`email-mailbox-as-todoist-tasks.json`](email-mailbox-as-todoist-tasks.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `imap`, `openAiApi`, `todoistApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Mark As Read | `gmail` | markAsRead |
| Star | `gmail` | addLabels |
| Get Starred From Inbox | `gmail` | getAll |
| Get Unread From Inbox | `gmail` | getAll |
| If Task Not Exist | `if` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structure Output Todoist Ready | `outputParserStructured` | Inspect parameters |
| If AI responded properly | `if` | Inspect parameters |
| Create Todoist Task | `todoist` | Inspect parameters |
| Get Full Message | `gmail` | get |
| Summarize Message | `agent` | Inspect parameters |
| Enrich Emails With Tasks | `merge` | Inspect parameters |
| Enrich Tasks with Emails | `merge` | Inspect parameters |
| If Email Unstarred (Not Exist) | `if` | Inspect parameters |
| Close Task | `todoist` | close |
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Merge Starred and Unread Messages | `merge` | Inspect parameters |
| Get Open Tasks | `todoist` | getAll |

## Connection map

- Mark As Read → Star (`main`, output 0, input 0)
- Get Open Tasks → Enrich Emails With Tasks (`main`, output 0, input 1)
- Get Open Tasks → Enrich Tasks with Emails (`main`, output 0, input 1)
- Get Full Message → Summarize Message (`main`, output 0, input 0)
- Schedule Trigger → No Operation, do nothing (`main`, output 0, input 0)
- If Task Not Exist → Get Full Message (`main`, output 0, input 0)
- OpenAI Chat Model → Summarize Message (`ai_languageModel`, output 0, input 0)
- Summarize Message → If AI responded properly (`main`, output 0, input 0)
- Email Trigger (IMAP) → No Operation, do nothing (`main`, output 0, input 0)
- Get Unread From Inbox → Mark As Read (`main`, output 0, input 0)
- Get Unread From Inbox → Merge Starred and Unread Messages (`main`, output 0, input 0)
- Get Starred From Inbox → Merge Starred and Unread Messages (`main`, output 0, input 1)
- Enrich Emails With Tasks → If Task Not Exist (`main`, output 0, input 0)
- Enrich Tasks with Emails → If Email Unstarred (Not Exist) (`main`, output 0, input 0)
- If AI responded properly → Create Todoist Task (`main`, output 0, input 0)
- No Operation, do nothing → Get Unread From Inbox (`main`, output 0, input 0)
- No Operation, do nothing → Get Starred From Inbox (`main`, output 0, input 0)
- No Operation, do nothing → Get Open Tasks (`main`, output 0, input 0)
- If Email Unstarred (Not Exist) → Close Task (`main`, output 0, input 0)
- Structure Output Todoist Ready → Summarize Message (`ai_outputParser`, output 0, input 0)
- Merge Starred and Unread Messages → Enrich Emails With Tasks (`main`, output 0, input 0)
- Merge Starred and Unread Messages → Enrich Tasks with Emails (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → No Operation, do nothing (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Todoist/1749_Todoist_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Todoist/1749_Todoist_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
