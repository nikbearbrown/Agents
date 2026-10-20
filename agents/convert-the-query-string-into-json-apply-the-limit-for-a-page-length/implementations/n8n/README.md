# Convert the query string into JSON, apply the limit for a page length

This folder contains the **Convert the query string into JSON, apply the limit for a page length** workflow. Its executable nodes use `agent`, `chatTrigger`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `markdown`, `set`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`convert-the-query-string-into-json-apply-the-limit-for-a-page-length.json`](convert-the-query-string-into-json-apply-the-limit-for-a-page-length.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| QUERY_PARAMS | `set` | Inspect parameters |
| CONFIG | `set` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Is error? | `if` | Inspect parameters |
| Stringify error message | `set` | Inspect parameters |
| Exctract HTML Body | `set` | Inspect parameters |
| Remove extra tags | `set` | Inspect parameters |
| Simplify? | `if` | Inspect parameters |
| Simplify output | `set` | Inspect parameters |
| Convert to Markdown | `markdown` | Inspect parameters |
| Send Page Content | `set` | Inspect parameters |
| HTTP_Request_Tool | `toolWorkflow` | Inspect parameters |

## Connection map

- CONFIG → HTTP Request (`main`, output 0, input 0)
- Is error? → Stringify error message (`main`, output 0, input 0)
- Is error? → Exctract HTML Body (`main`, output 1, input 0)
- Simplify? → Simplify output (`main`, output 0, input 0)
- Simplify? → Convert to Markdown (`main`, output 1, input 0)
- HTTP Request → Is error? (`main`, output 0, input 0)
- QUERY_PARAMS → CONFIG (`main`, output 0, input 0)
- Simplify output → Convert to Markdown (`main`, output 0, input 0)
- HTTP_Request_Tool → AI Agent (`ai_tool`, output 0, input 0)
- Remove extra tags → Simplify? (`main`, output 0, input 0)
- Exctract HTML Body → Remove extra tags (`main`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- Convert to Markdown → Send Page Content (`main`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- When Executed by Another Workflow → QUERY_PARAMS (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0363_HTTP_Executeworkflow_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0363_HTTP_Executeworkflow_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
