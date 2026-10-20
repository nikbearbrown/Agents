# rag grader

This folder contains the **rag grader** workflow. Its executable nodes use `agent`, `code`, `executeWorkflowTrigger`, `lmChatOpenRouter`, `merge`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rag-answer-evaluation.json`](rag-answer-evaluation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openRouterApi`

**Entry nodes:** Start

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenRouter Chat Model2 | `lmChatOpenRouter` | Inspect parameters |
| Merge7 | `merge` | Inspect parameters |
| Correctness grader | `agent` | Inspect parameters |
| Relevance grader | `agent` | Inspect parameters |
| Groundedness grader | `agent` | Inspect parameters |
| Groundedness output parser | `outputParserStructured` | Inspect parameters |
| Relevance output parser | `outputParserStructured` | Inspect parameters |
| Correctness output parser | `outputParserStructured` | Inspect parameters |
| Dummy node | `code` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| OpenRouter Chat Model1 | `lmChatOpenRouter` | Inspect parameters |
| Start | `executeWorkflowTrigger` | Inspect parameters |

## Connection map

- OpenRouter Chat Model2 → Correctness grader (`ai_languageModel`, output 0, input 0)
- Correctness grader → Merge7 (`main`, output 0, input 0)
- Relevance grader → Merge7 (`main`, output 0, input 1)
- Groundedness grader → Merge7 (`main`, output 0, input 2)
- Groundedness output parser → Groundedness grader (`ai_outputParser`, output 0, input 0)
- Relevance output parser → Relevance grader (`ai_outputParser`, output 0, input 0)
- Correctness output parser → Correctness grader (`ai_outputParser`, output 0, input 0)
- Dummy node → Correctness grader (`main`, output 0, input 0)
- Dummy node → Relevance grader (`main`, output 0, input 0)
- Dummy node → Groundedness grader (`main`, output 0, input 0)
- OpenRouter Chat Model1 → Groundedness grader (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model → Relevance grader (`ai_languageModel`, output 0, input 0)
- Start → Dummy node (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
