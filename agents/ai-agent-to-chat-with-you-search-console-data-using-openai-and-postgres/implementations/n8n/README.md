# AI Agent to chat with you Search Console Data, using OpenAI and Postgres

This folder contains the **AI Agent to chat with you Search Console Data, using OpenAI and Postgres** workflow. Its executable nodes use `agent`, `aggregate`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryPostgresChat`, `respondToWebhook`, `set`, `switch`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-agent-to-chat-with-you-search-console-data-using-openai-and-postgres.json`](ai-agent-to-chat-with-you-search-console-data-using-openai-and-postgres.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `oAuth2Api`, `openAiApi`, `postgres`

**Entry nodes:** Webhook - ChatInput, Tool calling

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Set fields | `set` | Inspect parameters |
| Webhook - ChatInput | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Call Search Console Tool | `toolWorkflow` | Inspect parameters |
| Tool calling | `executeWorkflowTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Set fields - Consruct API CALL | `set` | Inspect parameters |
| Set fields - Create searchConsoleDataArray | `set` | Inspect parameters |
| Set fields - Create searchConsoleDataArray 2 | `set` | Inspect parameters |
| Search Console - Get Custom Insights | `httpRequest` | POST |
| ## Search Console - Get List of Properties | `httpRequest` | Inspect parameters |
| Array aggregation - response to AI Agent | `aggregate` | Inspect parameters |
| Array aggregation - response to AI Agent1 | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- Switch → Search Console - Get Custom Insights (`main`, output 0, input 0)
- Switch → ## Search Console - Get List of Properties (`main`, output 1, input 0)
- AI Agent → Respond to Webhook (`main`, output 0, input 0)
- Set fields → AI Agent (`main`, output 0, input 0)
- Tool calling → Set fields - Consruct API CALL (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Webhook - ChatInput → Set fields (`main`, output 0, input 0)
- Postgres Chat Memory → AI Agent (`ai_memory`, output 0, input 0)
- Call Search Console Tool → AI Agent (`ai_tool`, output 0, input 0)
- Set fields - Consruct API CALL → Switch (`main`, output 0, input 0)
- Search Console - Get Custom Insights → Set fields - Create searchConsoleDataArray (`main`, output 0, input 0)
- ## Search Console - Get List of Properties → Set fields - Create searchConsoleDataArray 2 (`main`, output 0, input 0)
- Set fields - Create searchConsoleDataArray → Array aggregation - response to AI Agent (`main`, output 0, input 0)
- Set fields - Create searchConsoleDataArray 2 → Array aggregation - response to AI Agent1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1252_Webhook_Respondtowebhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1252_Webhook_Respondtowebhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
