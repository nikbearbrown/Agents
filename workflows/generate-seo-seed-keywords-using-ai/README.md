# Generate SEO Seed Keywords Using AI

This folder contains the **Generate SEO Seed Keywords Using AI** workflow. Its executable nodes use `agent`, `aggregate`, `lmChatAnthropic`, `manualTrigger`, `noOp`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-seo-seed-keywords-using-ai.json`](generate-seo-seed-keywords-using-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Set Ideal Customer Profile (ICP) | `set` | Inspect parameters |
| Aggregate for AI node | `aggregate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Connect to your own database | `noOp` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |

## Connection map

- AI Agent → Split Out (`main`, output 0, input 0)
- Split Out → Connect to your own database (`main`, output 0, input 0)
- Anthropic Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Aggregate for AI node → AI Agent (`main`, output 0, input 0)
- Set Ideal Customer Profile (ICP) → Aggregate for AI node (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Ideal Customer Profile (ICP) (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1471_Splitout_Aggregate_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1471_Splitout_Aggregate_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
