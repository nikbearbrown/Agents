# Mycroft - Financial Intelligence Hub

This folder contains the **Mycroft - Financial Intelligence Hub** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `extractFromFile`, `httpRequest`, `if`, `lmChatOllama`, `outputParserStructured`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-financial-intelligence-hub.json`](mycroft-financial-intelligence-hub.json): sanitized, inactive import copy with an overview sticky note.
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
| Initialize Hub | `set` | Inspect parameters |
| Initialize Logging | `code` | Inspect parameters |
| LLM Chain Router | `chainLlm` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| Call SEC? | `if` | Inspect parameters |
| Call Patent? | `if` | Inspect parameters |
| Call SEC Workflow | `httpRequest` | POST |
| Call Patent Workflow | `httpRequest` | POST |
| Log: SEC Called | `code` | Inspect parameters |
| Log: Patent Called | `code` | Inspect parameters |
| Aggregate Results | `code` | Inspect parameters |
| Log: Results Aggregated | `code` | Inspect parameters |
| LLM Chain Analyst | `chainLlm` | Inspect parameters |
| Ollama Analyst Model | `lmChatOllama` | Inspect parameters |
| Log: Analysis Complete | `code` | Inspect parameters |
| Format Chat Response | `code` | Inspect parameters |
| Log: Complete | `code` | Inspect parameters |
| No Tools Needed | `code` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Read/Write Files from Disk | `readWriteFile` | Inspect parameters |
| Extract from File | `extractFromFile` | fromJson |

## Connection map

- When chat message received → Initialize Hub (`main`, output 0, input 0)
- Initialize Hub → Initialize Logging (`main`, output 0, input 0)
- Initialize Logging → LLM Chain Router (`main`, output 0, input 0)
- LLM Chain Router → Call SEC? (`main`, output 0, input 0)
- LLM Chain Router → Call Patent? (`main`, output 0, input 0)
- Call SEC? → Call SEC Workflow (`main`, output 0, input 0)
- Call SEC? → No Tools Needed (`main`, output 1, input 0)
- Call Patent? → Call Patent Workflow (`main`, output 0, input 0)
- Call Patent? → No Tools Needed (`main`, output 1, input 0)
- Call SEC Workflow → Log: SEC Called (`main`, output 0, input 0)
- Call Patent Workflow → Log: Patent Called (`main`, output 0, input 0)
- Log: SEC Called → Aggregate Results (`main`, output 0, input 0)
- Log: Patent Called → Aggregate Results (`main`, output 0, input 0)
- No Tools Needed → Aggregate Results (`main`, output 0, input 0)
- Aggregate Results → Log: Results Aggregated (`main`, output 0, input 0)
- Aggregate Results → Read/Write Files from Disk (`main`, output 0, input 0)
- LLM Chain Analyst → Log: Analysis Complete (`main`, output 0, input 0)
- Log: Analysis Complete → Format Chat Response (`main`, output 0, input 0)
- Format Chat Response → Log: Complete (`main`, output 0, input 0)
- Ollama Chat Model → LLM Chain Router (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → LLM Chain Router (`ai_outputParser`, output 0, input 0)
- Ollama Analyst Model → LLM Chain Analyst (`ai_languageModel`, output 0, input 0)
- Read/Write Files from Disk → Extract from File (`main`, output 0, input 0)
- Extract from File → LLM Chain Analyst (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
