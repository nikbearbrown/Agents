# Intelligent Web Query and Semantic Re-Ranking Flow

This folder contains the **Intelligent Web Query and Semantic Re-Ranking Flow** workflow. Its executable nodes use `chainLlm`, `code`, `dateTime`, `httpRequest`, `lmChatAnthropic`, `lmChatGoogleGemini`, `lmChatOpenAi`, `outputParserAutofixing`, `outputParserStructured`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`intelligent-web-query-and-semantic-re-ranking-flow.json`](intelligent-web-query-and-semantic-re-ranking-flow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `googlePalmApi`, `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Date & Time | `dateTime` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Auto-fixing Output Parser6 | `outputParserAutofixing` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Query-1 Combined | `code` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Semantic Search - Result Re-Ranker | `chainLlm` | Inspect parameters |
| Query | `httpRequest` | Inspect parameters |
| Webhook Call | `httpRequest` | Inspect parameters |
| Semantic Search -Query Maker | `chainLlm` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser2 | `outputParserStructured` | Inspect parameters |
| Parser Model | `lmChatGoogleGemini` | Inspect parameters |
| Agent Model | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Query → Query-1 Combined (`main`, output 0, input 0)
- Webhook → Date & Time (`main`, output 0, input 0)
- Agent Model → Semantic Search - Result Re-Ranker (`ai_languageModel`, output 0, input 0)
- Agent Model → Semantic Search -Query Maker (`ai_languageModel`, output 0, input 0)
- Date & Time → Semantic Search -Query Maker (`main`, output 0, input 0)
- Parser Model → Auto-fixing Output Parser6 (`ai_languageModel`, output 0, input 0)
- Parser Model → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Query-1 Combined → Semantic Search - Result Re-Ranker (`main`, output 0, input 0)
- Auto-fixing Output Parser → Semantic Search -Query Maker (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Structured Output Parser2 → Auto-fixing Output Parser6 (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser6 → Semantic Search - Result Re-Ranker (`ai_outputParser`, output 0, input 0)
- Semantic Search -Query Maker → Query (`main`, output 0, input 0)
- Semantic Search - Result Re-Ranker → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/2003_Datetime_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/2003_Datetime_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
