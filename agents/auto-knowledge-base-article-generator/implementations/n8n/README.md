# Auto Knowledge Base Article Generator

This folder contains the **Auto Knowledge Base Article Generator** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflow`, `function`, `httpRequest`, `if`, `lmChatOpenAi`, `merge`, `noOp`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auto-knowledge-base-article-generator.json`](auto-knowledge-base-article-generator.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create Perplexity Content | `httpRequest` | POST |
| AI Writer Agent | `agent` | Inspect parameters |
| AI Editor Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Accept and Publish | `toolWorkflow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| JSON.parse1 | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Format | `code` | Inspect parameters |
| JSON.parse | `code` | Inspect parameters |
| Format Perplexity Output & Add Citations | `code` | Inspect parameters |
| Initialize Count | `set` | Inspect parameters |
| Increment Count | `function` | Inspect parameters |
| Check Limit | `if` | Inspect parameters |
| Stop Here | `noOp` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| JSON.parse3 | `code` | Inspect parameters |
| should submit | `if` | Inspect parameters |

## Connection map

- Merge → Format (`main`, output 0, input 0)
- Format → AI Editor Agent (`main`, output 0, input 0)
- Stop Here → JSON.parse3 (`main`, output 0, input 0)
- JSON.parse → AI Writer Agent (`main`, output 0, input 0)
- JSON.parse → Increment Count (`main`, output 0, input 0)
- Check Limit → Stop Here (`main`, output 0, input 0)
- Check Limit → should submit (`main`, output 1, input 0)
- JSON.parse1 → Merge (`main`, output 0, input 0)
- JSON.parse3 → Execute Workflow (`main`, output 0, input 0)
- should submit → JSON.parse3 (`main`, output 0, input 0)
- should submit → JSON.parse (`main`, output 1, input 0)
- AI Editor Agent → Check Limit (`main`, output 0, input 0)
- AI Writer Agent → Create Perplexity Content (`main`, output 0, input 0)
- AI Writer Agent → JSON.parse1 (`main`, output 0, input 0)
- Increment Count → Merge (`main`, output 0, input 2)
- Initialize Count → AI Writer Agent (`main`, output 0, input 0)
- Initialize Count → Increment Count (`main`, output 0, input 0)
- OpenAI Chat Model → AI Writer Agent (`ai_languageModel`, output 0, input 0)
- Accept and Publish → AI Editor Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model1 → AI Editor Agent (`ai_languageModel`, output 0, input 0)
- Create Perplexity Content → Format Perplexity Output & Add Citations (`main`, output 0, input 0)
- When chat message received → Initialize Count (`main`, output 0, input 0)
- Format Perplexity Output & Add Citations → Merge (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1756_Code_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1756_Code_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
