# ERP AI chatbot for Odoo sales module

This folder contains the **ERP AI chatbot for Odoo sales module** workflow. Its executable nodes use `agent`, `aggregate`, `chainSummarization`, `chatTrigger`, `convertToFile`, `extractFromFile`, `if`, `lmChatOpenAi`, `lmOpenAi`, `memoryBufferWindow`, `odoo`, `readWriteFile`, `scheduleTrigger`, `toolCalculator`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`erp-ai-chatbot-for-odoo-sales-module.json`](erp-ai-chatbot-for-odoo-sales-module.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `odooApi`, `openAiApi`

**Entry nodes:** Schedule Trigger, Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Save Summary to File | `readWriteFile` | write |
| Get All Opportunities from Odoo | `odoo` | opportunity / getAll |
| Read Summary From File | `readWriteFile` | Inspect parameters |
| If Summary Exists | `if` | Inspect parameters |
| Merge Opportunities | `aggregate` | Inspect parameters |
| Extract Text From File | `extractFromFile` | text |
| AI Conversational Agent | `agent` | Inspect parameters |
| Summarize Opportunities | `chainSummarization` | Inspect parameters |
| OpenAI Summarization Model | `lmOpenAi` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |

## Connection map

- Calculator → AI Conversational Agent (`ai_tool`, output 0, input 0)
- Chat Trigger → Read Summary From File (`main`, output 0, input 0)
- Convert to File → Save Summary to File (`main`, output 0, input 0)
- Schedule Trigger → Get All Opportunities from Odoo (`main`, output 0, input 0)
- If Summary Exists → Extract Text From File (`main`, output 0, input 0)
- If Summary Exists → Get All Opportunities from Odoo (`main`, output 1, input 0)
- OpenAI Chat Model → AI Conversational Agent (`ai_languageModel`, output 0, input 0)
- Merge Opportunities → Summarize Opportunities (`main`, output 0, input 0)
- Save Summary to File → Read Summary From File (`main`, output 0, input 0)
- Window Buffer Memory → AI Conversational Agent (`ai_memory`, output 0, input 0)
- Extract Text From File → AI Conversational Agent (`main`, output 0, input 0)
- Read Summary From File → If Summary Exists (`main`, output 0, input 0)
- Summarize Opportunities → Convert to File (`main`, output 0, input 0)
- OpenAI Summarization Model → Summarize Opportunities (`ai_languageModel`, output 0, input 0)
- Get All Opportunities from Odoo → Merge Opportunities (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Odoo/1929_Odoo_Schedule_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Odoo/1929_Odoo_Schedule_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
