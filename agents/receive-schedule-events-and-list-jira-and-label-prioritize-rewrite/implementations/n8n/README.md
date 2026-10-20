# receive schedule events and list jira and label prioritize rewrite

This folder contains the **receive schedule events and list jira and label prioritize rewrite** workflow. Its executable nodes use `aggregate`, `chainLlm`, `jira`, `lmChatOpenAi`, `noOp`, `outputParserStructured`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-jira-and-label-prioritize-rewrite.json`](receive-schedule-events-and-list-jira-and-label-prioritize-rewrite.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `jiraSoftwareCloudApi`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Open Tickets | `jira` | getAll |
| Simplify Ticket | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Label, Prioritize & Rewrite | `chainLlm` | Inspect parameters |
| Update Labels, Priority and Description | `jira` | update |
| Get Recent Similar Issues Resolved | `jira` | getAll |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Issue Ref | `noOp` | Inspect parameters |
| Get Comments | `jira` | issueComment / getAll |
| Simplify Comments | `set` | Inspect parameters |
| Summarise Resolution | `chainLlm` | Inspect parameters |
| Simplify Issue | `set` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Return Fields | `set` | Inspect parameters |
| Attempt to Resolve Issue | `chainLlm` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Add Comment to Issue | `jira` | issueComment |
| Mark as Seen | `removeDuplicates` | removeItemsSeenInPreviousExecutions |

## Connection map

- Aggregate → Summarise Resolution (`main`, output 0, input 0)
- Issue Ref → Simplify Issue (`main`, output 0, input 0)
- Aggregate1 → Attempt to Resolve Issue (`main`, output 0, input 0)
- Get Comments → Simplify Comments (`main`, output 0, input 0)
- Mark as Seen → Simplify Ticket (`main`, output 0, input 0)
- Return Fields → Loop Over Items (`main`, output 0, input 0)
- Simplify Issue → Get Comments (`main`, output 0, input 0)
- Loop Over Items → Aggregate1 (`main`, output 0, input 0)
- Loop Over Items → Issue Ref (`main`, output 1, input 0)
- Simplify Ticket → Label, Prioritize & Rewrite (`main`, output 0, input 0)
- Get Open Tickets → Mark as Seen (`main`, output 0, input 0)
- Schedule Trigger → Get Open Tickets (`main`, output 0, input 0)
- OpenAI Chat Model → Label, Prioritize & Rewrite (`ai_languageModel`, output 0, input 0)
- Simplify Comments → Aggregate (`main`, output 0, input 0)
- OpenAI Chat Model1 → Summarise Resolution (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Attempt to Resolve Issue (`ai_languageModel`, output 0, input 0)
- Summarise Resolution → Return Fields (`main`, output 0, input 0)
- Attempt to Resolve Issue → Add Comment to Issue (`main`, output 0, input 0)
- Structured Output Parser → Label, Prioritize & Rewrite (`ai_outputParser`, output 0, input 0)
- Label, Prioritize & Rewrite → Update Labels, Priority and Description (`main`, output 0, input 0)
- Get Recent Similar Issues Resolved → Loop Over Items (`main`, output 0, input 0)
- Update Labels, Priority and Description → Get Recent Similar Issues Resolved (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0907_Schedule_Removeduplicates_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0907_Schedule_Removeduplicates_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
