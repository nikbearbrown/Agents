# history channel slack and split out and slack

This folder contains the **history channel slack and split out and slack** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `if`, `lmChatGoogleGemini`, `noOp`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `splitOut`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`history-channel-slack-and-split-out-and-slack.json`](history-channel-slack-and-split-out-and-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `slackApi`

**Entry nodes:** When Executed by Another Workflow, Monday @ 6am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Last Week's Messages | `slack` | channel / history |
| Simplify Message | `set` | Inspect parameters |
| Group By User | `code` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Messages to Items | `code` | Inspect parameters |
| Get User | `slack` | user |
| Aggregate | `aggregate` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Get Thread | `slack` | channel / replies |
| Aggregate1 | `aggregate` | Inspect parameters |
| Simplify Thread Comments | `set` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Message Ref | `noOp` | Inspect parameters |
| Split Out2 | `splitOut` | Inspect parameters |
| Map Reply UserIds | `set` | Inspect parameters |
| Get Reply Users | `slack` | user |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Summarise Threads | `chainLlm` | Inspect parameters |
| Aggregate2 | `aggregate` | Inspect parameters |
| Aggregate Reply Users | `aggregate` | Inspect parameters |
| Reply Users | `set` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Aggregate3 | `set` | Inspect parameters |
| Aggregate4 | `aggregate` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Map Users to Messages | `executeWorkflow` | Inspect parameters |
| Get User Info | `set` | Inspect parameters |
| Fetch Message Replies | `executeWorkflow` | Inspect parameters |
| Has ReplyUsers? | `if` | Inspect parameters |
| Messages to Items1 | `code` | Inspect parameters |
| Aggregate Results | `set` | Inspect parameters |
| Team Member Weekly Report Agent | `chainLlm` | Inspect parameters |
| Merge with Results | `set` | Inspect parameters |
| Team Weekly Report Agent | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Post Report in Team Channel | `slack` | Inspect parameters |
| Summarize Message Threads | `executeWorkflow` | Inspect parameters |
| Monday @ 6am | `scheduleTrigger` | Inspect parameters |

## Connection map

- Filter → Simplify Thread Comments (`main`, output 0, input 0)
- Switch → Get User (`main`, output 0, input 0)
- Switch → Split Out1 (`main`, output 1, input 0)
- Switch → Map Reply UserIds (`main`, output 2, input 0)
- Get User → Messages to Items (`main`, output 0, input 0)
- Aggregate → Get User Info (`main`, output 0, input 0)
- Split Out → Map Users to Messages (`main`, output 0, input 0)
- Aggregate1 → Loop Over Items (`main`, output 0, input 0)
- Aggregate3 → Aggregate4 (`main`, output 0, input 0)
- Get Thread → Filter (`main`, output 0, input 0)
- Split Out1 → Loop Over Items (`main`, output 0, input 0)
- Split Out2 → Get Reply Users (`main`, output 0, input 0)
- Message Ref → Get Thread (`main`, output 0, input 0)
- Reply Users → Messages to Items1 (`main`, output 0, input 0)
- Monday @ 6am → Get Last Week's Messages (`main`, output 0, input 0)
- Group By User → Split Out (`main`, output 0, input 0)
- Get Reply Users → Aggregate Reply Users (`main`, output 0, input 0)
- Has ReplyUsers? → Split Out2 (`main`, output 0, input 0)
- Has ReplyUsers? → Reply Users (`main`, output 1, input 0)
- Loop Over Items → Aggregate3 (`main`, output 0, input 0)
- Loop Over Items → Message Ref (`main`, output 1, input 0)
- Simplify Message → Aggregate (`main`, output 0, input 0)
- Aggregate Results → Team Member Weekly Report Agent (`main`, output 0, input 0)
- Map Reply UserIds → Has ReplyUsers? (`main`, output 0, input 0)
- Messages to Items → Simplify Message (`main`, output 0, input 0)
- Summarise Threads → Aggregate2 (`main`, output 0, input 0)
- Merge with Results → Team Weekly Report Agent (`main`, output 0, input 0)
- Messages to Items1 → Summarise Threads (`main`, output 0, input 0)
- Aggregate Reply Users → Reply Users (`main`, output 0, input 0)
- Fetch Message Replies → Summarize Message Threads (`main`, output 0, input 0)
- Map Users to Messages → Fetch Message Replies (`main`, output 0, input 0)
- Get Last Week's Messages → Group By User (`main`, output 0, input 0)
- Google Gemini Chat Model → Summarise Threads (`ai_languageModel`, output 0, input 0)
- Simplify Thread Comments → Aggregate1 (`main`, output 0, input 0)
- Team Weekly Report Agent → Post Report in Team Channel (`main`, output 0, input 0)
- Google Gemini Chat Model1 → Team Member Weekly Report Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Team Weekly Report Agent (`ai_languageModel`, output 0, input 0)
- Summarize Message Threads → Aggregate Results (`main`, output 0, input 0)
- Team Member Weekly Report Agent → Merge with Results (`main`, output 0, input 0)
- When Executed by Another Workflow → Switch (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0921_Splitout_Code_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0921_Splitout_Code_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
