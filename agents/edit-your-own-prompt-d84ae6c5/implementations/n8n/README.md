# Edit your own prompt ⬇️

This folder contains the **Edit your own prompt ⬇️** workflow. Its executable nodes use `chainLlm`, `code`, `httpRequest`, `if`, `lmChatOpenAi`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`edit-your-own-prompt-d84ae6c5.json`](edit-your-own-prompt-d84ae6c5.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Get Changes1 | `httpRequest` | Inspect parameters |
| Skip File Change1 | `if` | Inspect parameters |
| Parse Last Diff Line1 | `code` | Inspect parameters |
| Post Discussions1 | `httpRequest` | POST |
| Need Review1 | `if` | Inspect parameters |
| Basic LLM Chain1 | `chainLlm` | Inspect parameters |

## Connection map

- Code → Basic LLM Chain1 (`main`, output 0, input 0)
- Webhook → Need Review1 (`main`, output 0, input 0)
- Split Out1 → Skip File Change1 (`main`, output 0, input 0)
- Get Changes1 → Split Out1 (`main`, output 0, input 0)
- Need Review1 → Get Changes1 (`main`, output 0, input 0)
- Basic LLM Chain1 → Post Discussions1 (`main`, output 0, input 0)
- Skip File Change1 → Parse Last Diff Line1 (`main`, output 0, input 0)
- OpenAI Chat Model1 → Basic LLM Chain1 (`ai_languageModel`, output 0, input 0)
- Parse Last Diff Line1 → Code (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1381_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1381_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
