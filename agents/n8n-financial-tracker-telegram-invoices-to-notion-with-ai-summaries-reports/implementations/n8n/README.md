# N8N Financial Tracker Telegram Invoices to Notion with AI Summaries & Reports

This folder contains the **N8N Financial Tracker Telegram Invoices to Notion with AI Summaries & Reports** workflow. Its executable nodes use `chainLlm`, `code`, `editImage`, `lmChatGoogleGemini`, `notion`, `outputParserStructured`, `quickChart`, `scheduleTrigger`, `splitOut`, `summarize`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-financial-tracker-telegram-invoices-to-notion-with-ai-summaries-reports.json`](n8n-financial-tracker-telegram-invoices-to-notion-with-ai-summaries-reports.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `notionApi`, `telegramApi`

**Entry nodes:** Schedule Trigger \| for send chart report, Telegram Trigger \| When recive photo

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Schedule Trigger \| for send chart report | `scheduleTrigger` | Inspect parameters |
| Get Recent Data from Notions | `notion` | databasePage / getAll |
| Summarize Transaction Data | `summarize` | Inspect parameters |
| Generate Chart | `quickChart` | Inspect parameters |
| Send Chart Image to Group or Private Chat | `telegram` | sendPhoto |
| Convert Data to JSON chart payload | `code` | Inspect parameters |
| Telegram Trigger \| When recive photo | `telegramTrigger` | Inspect parameters |
| Get Image Info | `editImage` | information |
| Parse To your object \| Table | `outputParserStructured` | Inspect parameters |
| Split Out \| data transaction | `splitOut` | Inspect parameters |
| Sendback to chat and give summarize text | `telegram` | Inspect parameters |
| Record To Notion Database | `notion` | databasePage |
| Telegram | `telegram` | file |

## Connection map

- Telegram → Get Image Info (`main`, output 0, input 0)
- Generate Chart → Send Chart Image to Group or Private Chat (`main`, output 0, input 0)
- Get Image Info → Basic LLM Chain (`main`, output 0, input 0)
- Basic LLM Chain → Split Out \| data transaction (`main`, output 0, input 0)
- Basic LLM Chain → Sendback to chat and give summarize text (`main`, output 0, input 0)
- Google Gemini Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Summarize Transaction Data → Convert Data to JSON chart payload (`main`, output 0, input 0)
- Get Recent Data from Notions → Summarize Transaction Data (`main`, output 0, input 0)
- Parse To your object \| Table → Basic LLM Chain (`ai_outputParser`, output 0, input 0)
- Split Out \| data transaction → Record To Notion Database (`main`, output 0, input 0)
- Convert Data to JSON chart payload → Generate Chart (`main`, output 0, input 0)
- Telegram Trigger \| When recive photo → Telegram (`main`, output 0, input 0)
- Schedule Trigger \| for send chart report → Get Recent Data from Notions (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0931_Telegram_Splitout_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0931_Telegram_Splitout_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
