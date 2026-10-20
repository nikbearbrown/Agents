# text classifier and list message discord and removeitemsseeninpreviousexecutions remove duplicates

This folder contains the **text classifier and list message discord and removeitemsseeninpreviousexecutions remove duplicates** workflow. Its executable nodes use `code`, `discord`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `if`, `lmChatOpenAi`, `merge`, `noOp`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `switch`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`text-classifier-and-list-message-discord-and-removeitemsseeninpreviousexecutions-remove-duplicates.json`](text-classifier-and-list-message-discord-and-removeitemsseeninpreviousexecutions-remove-duplicates.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Spam Detection | `textClassifier` | Inspect parameters |
| Get Recent Messages | `discord` | message / getAll |
| Only Once | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Model | `lmChatOpenAi` | Inspect parameters |
| Warn User | `discord` | message |
| Warn User Only | `discord` | message |
| Group By User | `code` | Inspect parameters |
| For Each User... | `splitInBatches` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Message to List | `code` | Inspect parameters |
| Notify Moderators with Send & Wait | `discord` | message / sendAndWait |
| Flag as Spam | `set` | Inspect parameters |
| Flag as Not Spam | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Spam Messages Only | `filter` | Inspect parameters |
| Has Flagged Messages? | `if` | Inspect parameters |
| Get Message IDs | `code` | Inspect parameters |
| Delete Messages | `discord` | message / deleteMessage |
| Receive Instructions | `switch` | Inspect parameters |
| Moderation Subworkflow | `executeWorkflow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| No Action Taken | `noOp` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Merge → Spam Messages Only (`main`, output 0, input 0)
- Model → Spam Detection (`ai_languageModel`, output 0, input 0)
- Only Once → Group By User (`main`, output 0, input 0)
- Split Out → For Each User... (`main`, output 0, input 0)
- Flag as Spam → Merge (`main`, output 0, input 0)
- Group By User → Split Out (`main`, output 0, input 0)
- Spam Detection → Flag as Spam (`main`, output 0, input 0)
- Spam Detection → Flag as Not Spam (`main`, output 1, input 0)
- Delete Messages → Warn User (`main`, output 0, input 0)
- Get Message IDs → Delete Messages (`main`, output 0, input 0)
- Message to List → Spam Detection (`main`, output 0, input 0)
- Flag as Not Spam → Merge (`main`, output 0, input 1)
- For Each User... → Message to List (`main`, output 1, input 0)
- Schedule Trigger → Get Recent Messages (`main`, output 0, input 0)
- Spam Messages Only → Has Flagged Messages? (`main`, output 0, input 0)
- Get Recent Messages → Only Once (`main`, output 0, input 0)
- Receive Instructions → Get Message IDs (`main`, output 0, input 0)
- Receive Instructions → Warn User Only (`main`, output 1, input 0)
- Receive Instructions → No Action Taken (`main`, output 2, input 0)
- Has Flagged Messages? → Moderation Subworkflow (`main`, output 0, input 0)
- Has Flagged Messages? → For Each User... (`main`, output 1, input 0)
- Moderation Subworkflow → For Each User... (`main`, output 0, input 0)
- When Executed by Another Workflow → Notify Moderators with Send & Wait (`main`, output 0, input 0)
- Notify Moderators with Send & Wait → Receive Instructions (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0816_Splitout_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0816_Splitout_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
