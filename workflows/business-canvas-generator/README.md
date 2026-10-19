# Business Canvas Generator

This folder contains the **Business Canvas Generator** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `convertToFile`, `lmChatOllama`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`business-canvas-generator.json`](business-canvas-generator.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Key Partners Generator | `agent` | Inspect parameters |
| Key Activities Generator | `agent` | Inspect parameters |
| Value Proposition Generator | `agent` | Inspect parameters |
| Customer Relationship Generator | `agent` | Inspect parameters |
| Customer Segments Generator | `agent` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| Key Resources Generator | `agent` | Inspect parameters |
| Channels Generator | `agent` | Inspect parameters |
| Cost Structure Generator | `agent` | Inspect parameters |
| Title Generator | `agent` | Inspect parameters |
| Revenue Streams Generator | `agent` | Inspect parameters |
| Key Partners HTML Transformer | `code` | Inspect parameters |
| Key Activities HTML Transformer | `code` | Inspect parameters |
| Values proposition HTML Transformer | `code` | Inspect parameters |
| Customer Relationship HTML Transformer | `code` | Inspect parameters |
| Customer Segments HTML Transformer | `code` | Inspect parameters |
| Key Resources HTML Transformer | `code` | Inspect parameters |
| Channels HTML Transformer | `code` | Inspect parameters |
| Revenue streams HTML Transformer | `code` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Cost Structure HTML Transformer | `code` | Inspect parameters |
| Turn to HTML | `code` | Inspect parameters |
| HTML code to HTML file | `convertToFile` | toText |
| Merge All Data | `merge` | Inspect parameters |

## Connection map

- Code1 → Merge All Data (`main`, output 0, input 0)
- Turn to HTML → HTML code to HTML file (`main`, output 0, input 0)
- Merge All Data → Turn to HTML (`main`, output 0, input 0)
- Title Generator → Code1 (`main`, output 0, input 0)
- Ollama Chat Model → Key Partners Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Key Activities Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Value Proposition Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Customer Relationship Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Customer Segments Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Key Resources Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Channels Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Cost Structure Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Title Generator (`ai_languageModel`, output 0, input 0)
- Ollama Chat Model → Revenue Streams Generator (`ai_languageModel`, output 0, input 0)
- Channels Generator → Channels HTML Transformer (`main`, output 0, input 0)
- Key Partners Generator → Key Partners HTML Transformer (`main`, output 0, input 0)
- Key Resources Generator → Key Resources HTML Transformer (`main`, output 0, input 0)
- Cost Structure Generator → Cost Structure HTML Transformer (`main`, output 0, input 0)
- Key Activities Generator → Key Activities HTML Transformer (`main`, output 0, input 0)
- Channels HTML Transformer → Merge All Data (`main`, output 0, input 7)
- Revenue Streams Generator → Revenue streams HTML Transformer (`main`, output 0, input 0)
- When chat message received → Key Partners Generator (`main`, output 0, input 0)
- When chat message received → Value Proposition Generator (`main`, output 0, input 0)
- When chat message received → Customer Relationship Generator (`main`, output 0, input 0)
- When chat message received → Customer Segments Generator (`main`, output 0, input 0)
- When chat message received → Key Resources Generator (`main`, output 0, input 0)
- When chat message received → Channels Generator (`main`, output 0, input 0)
- When chat message received → Cost Structure Generator (`main`, output 0, input 0)
- When chat message received → Revenue Streams Generator (`main`, output 0, input 0)
- When chat message received → Title Generator (`main`, output 0, input 0)
- When chat message received → Key Activities Generator (`main`, output 0, input 0)
- Customer Segments Generator → Customer Segments HTML Transformer (`main`, output 0, input 0)
- Value Proposition Generator → Values proposition HTML Transformer (`main`, output 0, input 0)
- Key Partners HTML Transformer → Merge All Data (`main`, output 0, input 1)
- Key Resources HTML Transformer → Merge All Data (`main`, output 0, input 6)
- Cost Structure HTML Transformer → Merge All Data (`main`, output 0, input 8)
- Customer Relationship Generator → Customer Relationship HTML Transformer (`main`, output 0, input 0)
- Key Activities HTML Transformer → Merge All Data (`main`, output 0, input 2)
- Revenue streams HTML Transformer → Merge All Data (`main`, output 0, input 9)
- Customer Segments HTML Transformer → Merge All Data (`main`, output 0, input 5)
- Values proposition HTML Transformer → Merge All Data (`main`, output 0, input 3)
- Customer Relationship HTML Transformer → Merge All Data (`main`, output 0, input 4)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1907_Stickynote_Converttofile_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1907_Stickynote_Converttofile_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
