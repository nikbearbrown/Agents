# receive schedule events and default data loader and recursive character text splitter

This folder contains the **receive schedule events and default data loader and recursive character text splitter** workflow. Its executable nodes use `agent`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `if`, `informationExtractor`, `jira`, `lmChatOpenAi`, `noOp`, `removeDuplicates`, `scheduleTrigger`, `set`, `sort`, `splitInBatches`, `splitOut`, `summarize`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-default-data-loader-and-recursive-character-text-splitter.json`](receive-schedule-events-and-default-data-loader-and-recursive-character-text-splitter.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `jiraSoftwareCloudApi`, `openAiApi`, `supabaseApi`

**Entry nodes:** Schedule Trigger, Schedule Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Issues Similarity Database | `vectorStoreSupabase` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Find Similar Issues + Assignees | `agent` | Inspect parameters |
| Check User Workflow | `jira` | getAll |
| For Each User | `splitInBatches` | Inspect parameters |
| Assign User to Ticket | `jira` | update |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Collect Fields | `set` | Inspect parameters |
| Get Unassigned Tickets more than 5 days | `jira` | getAll |
| For Each Issue | `splitInBatches` | Inspect parameters |
| Issue Ref | `noOp` | Inspect parameters |
| Add Comment to Issue | `jira` | issueComment |
| Last 50 Resolved | `jira` | getAll |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Issues to Items | `splitOut` | Inspect parameters |
| To Structured Output | `informationExtractor` | Inspect parameters |
| Count Assigned Open Issues per User | `summarize` | Inspect parameters |
| Tally In-Progress Issues per User | `set` | Inspect parameters |
| Sort By Most Capacity | `sort` | Inspect parameters |
| If has Items? | `if` | Inspect parameters |
| Skip | `noOp` | Inspect parameters |

## Connection map

- Skip → For Each Issue (`main`, output 0, input 0)
- Issue Ref → Find Similar Issues + Assignees (`main`, output 0, input 0)
- For Each User → Count Assigned Open Issues per User (`main`, output 0, input 0)
- For Each User → Check User Workflow (`main`, output 1, input 0)
- If has Items? → For Each User (`main`, output 0, input 0)
- If has Items? → Skip (`main`, output 1, input 0)
- Collect Fields → Issues Similarity Database (`main`, output 0, input 0)
- For Each Issue → Issue Ref (`main`, output 1, input 0)
- Issues to Items → If has Items? (`main`, output 0, input 0)
- Last 50 Resolved → Remove Duplicates (`main`, output 0, input 0)
- Schedule Trigger → Last 50 Resolved (`main`, output 0, input 0)
- Embeddings OpenAI → Issues Similarity Database (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model → Find Similar Issues + Assignees (`ai_languageModel`, output 0, input 0)
- Remove Duplicates → Collect Fields (`main`, output 0, input 0)
- Schedule Trigger1 → Get Unassigned Tickets more than 5 days (`main`, output 0, input 0)
- Embeddings OpenAI1 → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → To Structured Output (`ai_languageModel`, output 0, input 0)
- Check User Workflow → Tally In-Progress Issues per User (`main`, output 0, input 0)
- Default Data Loader → Issues Similarity Database (`ai_document`, output 0, input 0)
- Add Comment to Issue → For Each Issue (`main`, output 0, input 0)
- To Structured Output → Issues to Items (`main`, output 0, input 0)
- Assign User to Ticket → Add Comment to Issue (`main`, output 0, input 0)
- Sort By Most Capacity → Assign User to Ticket (`main`, output 0, input 0)
- Supabase Vector Store → Find Similar Issues + Assignees (`ai_tool`, output 0, input 0)
- Find Similar Issues + Assignees → To Structured Output (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Tally In-Progress Issues per User → For Each User (`main`, output 0, input 0)
- Count Assigned Open Issues per User → Sort By Most Capacity (`main`, output 0, input 0)
- Get Unassigned Tickets more than 5 days → For Each Issue (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0819_Splitout_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0819_Splitout_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
