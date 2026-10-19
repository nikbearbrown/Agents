# 🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting

This folder contains the **🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting** workflow. Its executable nodes use `agent`, `aggregate`, `chainLlm`, `convertToFile`, `executeWorkflowTrigger`, `gmail`, `googleDrive`, `httpRequest`, `limit`, `lmChatGoogleGemini`, `lmChatOpenAi`, `markdown`, `merge`, `readWriteFile`, `scheduleTrigger`, `set`, `sort`, `splitOut`, `telegram`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-agent-for-top-n8n-creators-leaderboard-reporting.json`](ai-agent-for-top-n8n-creators-leaderboard-reporting.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googlePalmApi`, `openAiApi`, `telegramApi`

**Entry nodes:** When Executed by Another Workflow, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| stats_aggregate_creators | `httpRequest` | Inspect parameters |
| stats_aggregate_workflows | `httpRequest` | Inspect parameters |
| Global Variables | `set` | Inspect parameters |
| Parse Workflow Data | `set` | Inspect parameters |
| Parse Creators Data | `set` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Workflow Tool | `toolWorkflow` | Inspect parameters |
| creator-summary | `convertToFile` | toText |
| Workflow Response | `set` | Inspect parameters |
| Save creator-summary.md | `readWriteFile` | write |
| Creators Data | `set` | Inspect parameters |
| Workflows Data | `set` | Inspect parameters |
| Merge Creators & Workflows | `merge` | Inspect parameters |
| Split Out Creators | `splitOut` | Inspect parameters |
| Split Out Workflows | `splitOut` | Inspect parameters |
| Sort By Top Weekly Creator Inserts | `sort` | Inspect parameters |
| Sort By Top Weekly Workflow Inserts | `sort` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Take Top 10 Creators | `limit` | Inspect parameters |
| Take Top 50 Workflows | `limit` | Inspect parameters |
| Google Drive | `googleDrive` | createFromText |
| Convert Markdown to HTML | `markdown` | Inspect parameters |
| n8n Creators Stats Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Create Top 10 Workflows List | `chainLlm` | Inspect parameters |
| Convert Top 10 Markdown to HTML | `markdown` | Inspect parameters |
| Gmail Creators & Workflows Report | `gmail` | Inspect parameters |
| Telegram Top 10  Workflows List | `telegram` | Inspect parameters |
| Gmail Top 10 Workflows List | `gmail` | Inspect parameters |

## Connection map

- Aggregate → Workflow Response (`main`, output 0, input 0)
- gpt-4o-mini → n8n Creators Stats Agent (`ai_languageModel`, output 0, input 0)
- Creators Data → Merge Creators & Workflows (`main`, output 0, input 0)
- Workflow Tool → n8n Creators Stats Agent (`ai_tool`, output 0, input 0)
- Workflows Data → Merge Creators & Workflows (`main`, output 0, input 1)
- creator-summary → Save creator-summary.md (`main`, output 0, input 0)
- Global Variables → stats_aggregate_creators (`main`, output 0, input 0)
- Global Variables → stats_aggregate_workflows (`main`, output 0, input 0)
- Schedule Trigger → n8n Creators Stats Agent (`main`, output 0, input 0)
- Split Out Creators → Sort By Top Weekly Creator Inserts (`main`, output 0, input 0)
- Parse Creators Data → Split Out Creators (`main`, output 0, input 0)
- Parse Workflow Data → Split Out Workflows (`main`, output 0, input 0)
- Split Out Workflows → Sort By Top Weekly Workflow Inserts (`main`, output 0, input 0)
- Take Top 10 Creators → Creators Data (`main`, output 0, input 0)
- Take Top 50 Workflows → Workflows Data (`main`, output 0, input 0)
- Convert Markdown to HTML → Gmail Creators & Workflows Report (`main`, output 0, input 0)
- Google Gemini Chat Model → Create Top 10 Workflows List (`ai_languageModel`, output 0, input 0)
- n8n Creators Stats Agent → creator-summary (`main`, output 0, input 0)
- n8n Creators Stats Agent → Google Drive (`main`, output 0, input 0)
- n8n Creators Stats Agent → Convert Markdown to HTML (`main`, output 0, input 0)
- n8n Creators Stats Agent → Create Top 10 Workflows List (`main`, output 0, input 0)
- stats_aggregate_creators → Parse Creators Data (`main`, output 0, input 0)
- stats_aggregate_workflows → Parse Workflow Data (`main`, output 0, input 0)
- Merge Creators & Workflows → Aggregate (`main`, output 0, input 0)
- Create Top 10 Workflows List → Convert Top 10 Markdown to HTML (`main`, output 0, input 0)
- Create Top 10 Workflows List → Telegram Top 10  Workflows List (`main`, output 0, input 0)
- Convert Top 10 Markdown to HTML → Gmail Top 10 Workflows List (`main`, output 0, input 0)
- When Executed by Another Workflow → Global Variables (`main`, output 0, input 0)
- Sort By Top Weekly Creator Inserts → Take Top 10 Creators (`main`, output 0, input 0)
- Sort By Top Weekly Workflow Inserts → Take Top 50 Workflows (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1113_Telegram_Splitout_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1113_Telegram_Splitout_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
