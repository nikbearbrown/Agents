# Automated Research Report Generation with OpenAI, Wikipedia, Google Search, and Gmail/Telegram

This folder contains the **Automated Research Report Generation with OpenAI, Wikipedia, Google Search, and Gmail/Telegram** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `executeWorkflowTrigger`, `gmail`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `outputParserStructured`, `splitOut`, `telegram`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-research-report-generation-with-openai-wikipedia-google-search-and-gmail-telegram.json`](automated-research-report-generation-with-openai-wikipedia-google-search-and-gmail-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`, `serpApi`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Executed by Main AI Agent

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Search News | `toolHttpRequest` | Inspect parameters |
| Wikipedia | `toolHttpRequest` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Query Refiner | `agent` | Inspect parameters |
| Research AI Agent | `agent` | Inspect parameters |
| Google Search Web | `toolHttpRequest` | Inspect parameters |
| SerpApi | `toolHttpRequest` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Input Validation | `code` | Inspect parameters |
| Parse Research Output | `code` | Inspect parameters |
| Merge Split Items | `code` | Inspect parameters |
| Store Research Metadata | `googleSheets` | append |
| Generate PDF HTML | `code` | Inspect parameters |
| Convert HTML to PDF | `httpRequest` | POST |
| Aggregate | `aggregate` | Inspect parameters |
| Download PDF | `httpRequest` | Inspect parameters |
| Send Research to Gmail | `gmail` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Send PDF | `telegram` | sendDocument |
| Executed by Main AI Agent | `executeWorkflowTrigger` | Inspect parameters |
| Search Folder | `googleDrive` | fileFolder |
| If | `if` | Inspect parameters |

## Connection map

- SerpApi → Research AI Agent (`ai_tool`, output 0, input 0)
- Aggregate → Store Research Metadata (`main`, output 0, input 0)
- Aggregate → Generate PDF HTML (`main`, output 0, input 0)
- Split Out → Merge Split Items (`main`, output 0, input 0)
- Wikipedia → Research AI Agent (`ai_tool`, output 0, input 0)
- Search News → Research AI Agent (`ai_tool`, output 0, input 0)
- Download PDF → Send Research to Gmail (`main`, output 0, input 0)
- Download PDF → Send PDF (`main`, output 0, input 0)
- Query Refiner → Research AI Agent (`main`, output 0, input 0)
- Search Folder → If (`main`, output 0, input 0)
- Simple Memory → Research AI Agent (`ai_memory`, output 0, input 0)
- Input Validation → Query Refiner (`main`, output 0, input 0)
- Generate PDF HTML → Convert HTML to PDF (`main`, output 0, input 0)
- Google Search Web → Research AI Agent (`ai_tool`, output 0, input 0)
- Merge Split Items → Aggregate (`main`, output 0, input 0)
- OpenAI Chat Model → Research AI Agent (`ai_languageModel`, output 0, input 0)
- Research AI Agent → Parse Research Output (`main`, output 0, input 0)
- OpenAI Chat Model1 → Query Refiner (`ai_languageModel`, output 0, input 0)
- Convert HTML to PDF → Download PDF (`main`, output 0, input 0)
- Convert HTML to PDF → Search Folder (`main`, output 0, input 0)
- Parse Research Output → Split Out (`main`, output 0, input 0)
- Structured Output Parser → Query Refiner (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Input Validation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1341_Telegram_Splitout_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1341_Telegram_Splitout_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
