# search slack and receive schedule events and list linear

This folder contains the **search slack and receive schedule events and list linear** workflow. Its executable nodes use `aggregate`, `chainLlm`, `if`, `linear`, `lmChatOpenAi`, `merge`, `outputParserStructured`, `scheduleTrigger`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-slack-and-receive-schedule-events-and-list-linear.json`](search-slack-and-receive-schedule-events-and-list-linear.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `linearApi`, `openAiApi`, `slackApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Slack | `slack` | search |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Values | `set` | Inspect parameters |
| Create New Ticket? | `if` | Inspect parameters |
| Get Existing Issues | `linear` | getAll |
| Generate Ticket Using ChatGPT | `chainLlm` | Inspect parameters |
| Create Ticket | `linear` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Get Hashes Only | `set` | Inspect parameters |
| Collect Descriptions | `aggregate` | Inspect parameters |

## Connection map

- Merge → Create New Ticket? (`main`, output 0, input 0)
- Slack → Get Values (`main`, output 0, input 0)
- Get Values → Merge (`main`, output 0, input 0)
- Get Values → Get Existing Issues (`main`, output 0, input 0)
- Get Hashes Only → Merge (`main`, output 0, input 1)
- Schedule Trigger → Slack (`main`, output 0, input 0)
- OpenAI Chat Model → Generate Ticket Using ChatGPT (`ai_languageModel`, output 0, input 0)
- Create New Ticket? → Generate Ticket Using ChatGPT (`main`, output 0, input 0)
- Get Existing Issues → Collect Descriptions (`main`, output 0, input 0)
- Collect Descriptions → Get Hashes Only (`main`, output 0, input 0)
- Structured Output Parser → Generate Ticket Using ChatGPT (`ai_outputParser`, output 0, input 0)
- Generate Ticket Using ChatGPT → Create Ticket (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0526_Schedule_Slack_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0526_Schedule_Slack_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
