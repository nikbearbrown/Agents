# http request and get urls to scrape and chain llm

This folder contains the **http request and get urls to scrape and chain llm** workflow. Its executable nodes use `chainLlm`, `code`, `googleSheets`, `httpRequest`, `lmChatOpenRouter`, `manualTrigger`, `outputParserStructured`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-get-urls-to-scrape-and-chain-llm.json`](http-request-and-get-urls-to-scrape-and-chain-llm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| scrap url | `httpRequest` | POST |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| url | `splitInBatches` | Inspect parameters |
| get urls to scrape | `googleSheets` | Inspect parameters |
| clean html | `code` | Inspect parameters |
| extract data | `chainLlm` | Inspect parameters |
| add results | `googleSheets` | append |
| Split items | `splitOut` | Inspect parameters |

## Connection map

- url → scrap url (`main`, output 1, input 0)
- scrap url → clean html (`main`, output 0, input 0)
- clean html → extract data (`main`, output 0, input 0)
- Split items → add results (`main`, output 0, input 0)
- add results → url (`main`, output 0, input 0)
- extract data → Split items (`main`, output 0, input 0)
- get urls to scrape → url (`main`, output 0, input 0)
- OpenRouter Chat Model → extract data (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → extract data (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → get urls to scrape (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0913_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0913_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
