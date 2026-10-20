# 🔍🛠️Perplexity Researcher to HTML Web Page

This folder contains the **🔍🛠️Perplexity Researcher to HTML Web Page** workflow. Its executable nodes use `agent`, `chainLlm`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `noOp`, `outputParserStructured`, `respondToWebhook`, `set`, `telegram`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`perplexity-researcher-to-html-web-page.json`](perplexity-researcher-to-html-web-page.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpCustomAuth`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Webhook, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| gpt-4o-mini2 | `lmChatOpenAi` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| gpt-4o-mini5 | `lmChatOpenAi` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Do Nothing1 | `noOp` | Inspect parameters |
| gpt-4o-mini3 | `lmChatOpenAi` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| Prompts | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Telegram2 | `telegram` | Inspect parameters |
| If | `if` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Perplexity Topic Agent | `agent` | Inspect parameters |
| Call Perplexity Researcher | `toolWorkflow` | Inspect parameters |
| Do Nothing | `noOp` | Inspect parameters |
| Do Nothing2 | `noOp` | Inspect parameters |
| Do Nothing3 | `noOp` | Inspect parameters |
| Do Nothing4 | `noOp` | Inspect parameters |
| Get Topic | `set` | Inspect parameters |
| If Topic Exists | `if` | Inspect parameters |
| Improve Users Topic | `chainLlm` | Inspect parameters |
| If Topic | `if` | Inspect parameters |
| Chat Id | `set` | Inspect parameters |
| Article | `set` | Inspect parameters |
| Extract JSON | `agent` | Inspect parameters |
| If Article | `if` | Inspect parameters |
| Create HTML Article | `agent` | Inspect parameters |
| If HTML | `if` | Inspect parameters |
| Contents | `set` | Inspect parameters |
| Chat Id1 | `set` | Inspect parameters |
| Success Response | `set` | Inspect parameters |
| Error Response | `set` | Inspect parameters |
| Perplexity | `httpRequest` | POST |

## Connection map

- If → Prompts (`main`, output 0, input 0)
- If → No Operation, do nothing (`main`, output 1, input 0)
- If2 → Extract JSON (`main`, output 0, input 0)
- If2 → Do Nothing (`main`, output 1, input 0)
- Article → If Article (`main`, output 0, input 0)
- Chat Id → Telegram (`main`, output 0, input 0)
- If HTML → Contents (`main`, output 0, input 0)
- If HTML → Do Nothing3 (`main`, output 1, input 0)
- Prompts → Perplexity (`main`, output 0, input 0)
- Webhook → Get Topic (`main`, output 0, input 0)
- Chat Id1 → Telegram2 (`main`, output 0, input 0)
- Contents → Basic LLM Chain (`main`, output 0, input 0)
- If Topic → Perplexity Topic Agent (`main`, output 0, input 0)
- If Topic → Do Nothing4 (`main`, output 1, input 0)
- Get Topic → If Topic Exists (`main`, output 0, input 0)
- Telegram2 → If (`main`, output 0, input 0)
- If Article → Create HTML Article (`main`, output 0, input 0)
- If Article → Do Nothing2 (`main`, output 1, input 0)
- Perplexity → Success Response (`main`, output 0, input 0)
- gpt-4o-mini → Create HTML Article (`ai_languageModel`, output 0, input 0)
- Extract JSON → Article (`main`, output 0, input 0)
- gpt-4o-mini1 → Perplexity Topic Agent (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini2 → Extract JSON (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini3 → Improve Users Topic (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini5 → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Basic LLM Chain → Respond to Webhook (`main`, output 0, input 0)
- If Topic Exists → Improve Users Topic (`main`, output 0, input 0)
- If Topic Exists → Do Nothing1 (`main`, output 1, input 0)
- Create HTML Article → If HTML (`main`, output 0, input 0)
- Improve Users Topic → If Topic (`main`, output 0, input 0)
- Perplexity Topic Agent → If2 (`main`, output 0, input 0)
- Perplexity Topic Agent → Chat Id (`main`, output 0, input 0)
- Execute Workflow Trigger → Chat Id1 (`main`, output 0, input 0)
- No Operation, do nothing → Error Response (`main`, output 0, input 0)
- Structured Output Parser1 → Extract JSON (`ai_outputParser`, output 0, input 0)
- Call Perplexity Researcher → Perplexity Topic Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1496_Telegram_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1496_Telegram_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
