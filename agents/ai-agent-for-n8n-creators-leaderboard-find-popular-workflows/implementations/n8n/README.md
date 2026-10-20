# 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows

This folder contains the **🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `convertToFile`, `executeWorkflowTrigger`, `filter`, `httpRequest`, `limit`, `lmChatOllama`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `readWriteFile`, `set`, `sort`, `splitOut`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-agent-for-n8n-creators-leaderboard-find-popular-workflows.json`](ai-agent-for-n8n-creators-leaderboard-find-popular-workflows.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`, `openAiApi`

**Entry nodes:** When Executed by Another Workflow, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| stats_aggregate_creators | `httpRequest` | Inspect parameters |
| stats_aggregate_workflows | `httpRequest` | Inspect parameters |
| Global Variables | `set` | Inspect parameters |
| Parse Workflow Data | `set` | Inspect parameters |
| Parse Creators Data | `set` | Inspect parameters |
| Take Top 25 Creators | `limit` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Filter By Creator Username | `filter` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Workflow Tool | `toolWorkflow` | Inspect parameters |
| creator-summary | `convertToFile` | toText |
| Workflow Response | `set` | Inspect parameters |
| n8n Creator Stats Agent | `agent` | Inspect parameters |
| Save creator-summary.md | `readWriteFile` | write |
| Summary Report | `set` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| Creators Data | `set` | Inspect parameters |
| Workflows Data | `set` | Inspect parameters |
| Merge Creators & Workflows | `merge` | Inspect parameters |
| Split Out Creators | `splitOut` | Inspect parameters |
| Split Out Workflows | `splitOut` | Inspect parameters |
| Sort By Top Weekly Creator Inserts | `sort` | Inspect parameters |
| Sort By Top Weekly Workflow Inserts | `sort` | Inspect parameters |
| Take Top 300 Workflows | `limit` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Aggregate → Workflow Response (`main`, output 0, input 0)
- gpt-4o-mini → n8n Creator Stats Agent (`ai_languageModel`, output 0, input 0)
- Creators Data → Merge Creators & Workflows (`main`, output 0, input 0)
- Workflow Tool → n8n Creator Stats Agent (`ai_tool`, output 0, input 0)
- Workflows Data → Merge Creators & Workflows (`main`, output 0, input 1)
- creator-summary → Save creator-summary.md (`main`, output 0, input 0)
- Global Variables → stats_aggregate_creators (`main`, output 0, input 0)
- Global Variables → stats_aggregate_workflows (`main`, output 0, input 0)
- Split Out Creators → Sort By Top Weekly Creator Inserts (`main`, output 0, input 0)
- Parse Creators Data → Split Out Creators (`main`, output 0, input 0)
- Parse Workflow Data → Split Out Workflows (`main`, output 0, input 0)
- Split Out Workflows → Sort By Top Weekly Workflow Inserts (`main`, output 0, input 0)
- Take Top 25 Creators → Creators Data (`main`, output 0, input 0)
- Window Buffer Memory → n8n Creator Stats Agent (`ai_memory`, output 0, input 0)
- Take Top 300 Workflows → Workflows Data (`main`, output 0, input 0)
- n8n Creator Stats Agent → Summary Report (`main`, output 0, input 0)
- n8n Creator Stats Agent → creator-summary (`main`, output 0, input 0)
- stats_aggregate_creators → Parse Creators Data (`main`, output 0, input 0)
- stats_aggregate_workflows → Parse Workflow Data (`main`, output 0, input 0)
- Filter By Creator Username → Aggregate (`main`, output 0, input 0)
- Merge Creators & Workflows → Filter By Creator Username (`main`, output 0, input 0)
- When chat message received → n8n Creator Stats Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → Global Variables (`main`, output 0, input 0)
- Sort By Top Weekly Creator Inserts → Take Top 25 Creators (`main`, output 0, input 0)
- Sort By Top Weekly Workflow Inserts → Take Top 300 Workflows (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/2049_Limit_Splitout_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/2049_Limit_Splitout_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
