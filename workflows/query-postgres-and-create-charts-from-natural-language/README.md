# nl2sql

This folder contains the **nl2sql** workflow. Its executable nodes use `agent`, `code`, `if`, `lmChatDeepSeek`, `lmChatGoogleGemini`, `memoryBufferWindow`, `memoryManager`, `postgres`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`query-postgres-and-create-charts-from-natural-language.json`](query-postgres-and-create-charts-from-natural-language.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `deepSeekApi`, `googlePalmApi`, `postgres`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| DeepSeek Chat Model | `lmChatDeepSeek` | Inspect parameters |
| Return Final Response | `respondToWebhook` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Format Success Result | `code` | Inspect parameters |
| Chat Memory Manager | `memoryManager` | Inspect parameters |
| Format History | `code` | Inspect parameters |
| DeepSeek Chat Model1 | `lmChatDeepSeek` | Inspect parameters |
| Format Charts | `code` | Inspect parameters |
| Charts Agent | `agent` | Inspect parameters |
| Loop Entry | `set` | Inspect parameters |
| If Can Retry | `if` | Inspect parameters |
| Format Error Prompt | `code` | Inspect parameters |
| If Error | `if` | Inspect parameters |
| Search Memory | `memoryBufferWindow` | Inspect parameters |
| Extract User Input | `code` | Inspect parameters |
| Get DB Schema | `postgres` | executeQuery |
| Format Schema | `code` | Inspect parameters |
| Prepare Initial Prompt | `code` | Inspect parameters |
| Execute Generated SQL | `postgres` | executeQuery |
| Insert Memory | `memoryBufferWindow` | Inspect parameters |
| If Charts | `if` | Inspect parameters |
| If Ai Error | `if` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- AI Agent → If Ai Error (`main`, output 0, input 0)
- Webhook → Extract User Input (`main`, output 0, input 0)
- Format Success Result → If Charts (`main`, output 0, input 0)
- Chat Memory Manager → Format History (`main`, output 0, input 0)
- Format History → Get DB Schema (`main`, output 0, input 0)
- DeepSeek Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- DeepSeek Chat Model1 → Charts Agent (`ai_languageModel`, output 0, input 0)
- Format Charts → Return Final Response (`main`, output 0, input 0)
- Charts Agent → Format Charts (`main`, output 0, input 0)
- Loop Entry → AI Agent (`main`, output 0, input 0)
- If Can Retry → Loop Entry (`main`, output 0, input 0)
- If Can Retry → Format Success Result (`main`, output 1, input 0)
- Format Error Prompt → If Can Retry (`main`, output 0, input 0)
- If Error → Format Error Prompt (`main`, output 0, input 0)
- If Error → Format Success Result (`main`, output 1, input 0)
- Search Memory → Chat Memory Manager (`ai_memory`, output 0, input 0)
- Extract User Input → Chat Memory Manager (`main`, output 0, input 0)
- Get DB Schema → Format Schema (`main`, output 0, input 0)
- Format Schema → Prepare Initial Prompt (`main`, output 0, input 0)
- Prepare Initial Prompt → Loop Entry (`main`, output 0, input 0)
- Execute Generated SQL → If Error (`main`, output 0, input 0)
- Insert Memory → AI Agent (`ai_memory`, output 0, input 0)
- If Charts → Format Charts (`main`, output 0, input 0)
- If Charts → Charts Agent (`main`, output 1, input 0)
- If Ai Error → Execute Generated SQL (`main`, output 0, input 0)
- If Ai Error → Format Charts (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Wilsonoonn/n8n_nl2sql/blob/fa7c4204d690b1817aa4f916267d8a2f48c5c136/nl2sql.json](https://github.com/Wilsonoonn/n8n_nl2sql/blob/fa7c4204d690b1817aa4f916267d8a2f48c5c136/nl2sql.json). License: **Apache-2.0**; preserve [the notice](../../licenses/Wilsonoonn--n8n_nl2sql.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
