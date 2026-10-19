# AI Talent Intelligence Agent

This folder contains the **AI Talent Intelligence Agent** workflow. Its executable nodes use `aggregate`, `chainLlm`, `chatTrigger`, `code`, `emailSend`, `httpRequest`, `if`, `lmChatGroq`, `manualTrigger`, `merge`, `postgres`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-talent-intelligence-agent.json`](ai-talent-intelligence-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`, `httpHeaderAuth`, `smtp`

**Entry nodes:** ▶️ START - Run Complete Analysis, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| ▶️ START - Run Complete Analysis | `manualTrigger` | Inspect parameters |
| 📚 SOURCE 1: ArXiv Papers | `httpRequest` | Inspect parameters |
| 📰 SOURCE 2: News Search | `httpRequest` | POST |
| 🔄 Parse ArXiv Data | `code` | Inspect parameters |
| 🔄 Parse News Data | `code` | Inspect parameters |
| 🔍 FILTER: High Significance Only | `if` | Inspect parameters |
| 📊 AGGREGATE Statistics | `aggregate` | Inspect parameters |
| 📋 Generate Intelligence Report | `code` | Inspect parameters |
| 💾 Save to Database | `postgres` | executeQuery |
| 📧 Format Email Report | `code` | Inspect parameters |
| 📬 Send Email Report | `emailSend` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |

## Connection map

- ▶️ START - Run Complete Analysis → 📚 SOURCE 1: ArXiv Papers (`main`, output 0, input 0)
- ▶️ START - Run Complete Analysis → 📰 SOURCE 2: News Search (`main`, output 0, input 0)
- ▶️ START - Run Complete Analysis → Code (`main`, output 0, input 0)
- 📚 SOURCE 1: ArXiv Papers → 🔄 Parse ArXiv Data (`main`, output 0, input 0)
- 📰 SOURCE 2: News Search → 🔄 Parse News Data (`main`, output 0, input 0)
- 🔄 Parse ArXiv Data → Merge (`main`, output 0, input 0)
- 🔄 Parse News Data → Merge (`main`, output 0, input 1)
- 🔍 FILTER: High Significance Only → 📊 AGGREGATE Statistics (`main`, output 0, input 0)
- 📊 AGGREGATE Statistics → 📋 Generate Intelligence Report (`main`, output 0, input 0)
- 📋 Generate Intelligence Report → 💾 Save to Database (`main`, output 0, input 0)
- 📋 Generate Intelligence Report → 📧 Format Email Report (`main`, output 0, input 0)
- 📧 Format Email Report → 📬 Send Email Report (`main`, output 0, input 0)
- Code → Merge (`main`, output 0, input 2)
- Merge → Basic LLM Chain (`main`, output 0, input 0)
- Groq Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- When chat message received → Basic LLM Chain (`main`, output 0, input 0)
- Basic LLM Chain → 🔍 FILTER: High Significance Only (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
