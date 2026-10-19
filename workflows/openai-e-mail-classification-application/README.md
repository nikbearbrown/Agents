# OpenAI e-mail classification - application

This folder contains the **OpenAI e-mail classification - application** workflow. Its executable nodes use `emailReadImap`, `extractFromFile`, `informationExtractor`, `lmChatOpenAi`, `noOp`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`openai-e-mail-classification-application.json`](openai-e-mail-classification-application.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `imap`, `openAiApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email trigger | `emailReadImap` | Inspect parameters |
| Classify email | `textClassifier` | Inspect parameters |
| Extract variables - email & attachment | `informationExtractor` | Inspect parameters |
| Extract data from attachment | `extractFromFile` | pdf |
| OpenAI Chat Model 2 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Workflow 2 | `noOp` | Inspect parameters |
| Workflow 3 | `noOp` | Inspect parameters |
| workflow 4 | `noOp` | Inspect parameters |

## Connection map

- Email trigger → Extract data from attachment (`main`, output 0, input 0)
- Classify email → Extract variables - email & attachment (`main`, output 0, input 0)
- Classify email → Workflow 2 (`main`, output 1, input 0)
- Classify email → Workflow 3 (`main`, output 2, input 0)
- Classify email → workflow 4 (`main`, output 3, input 0)
- OpenAI Chat Model → Classify email (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model 2 → Extract variables - email & attachment (`ai_languageModel`, output 0, input 0)
- Extract data from attachment → Classify email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0929_Noop_Extractfromfile_Automation.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0929_Noop_Extractfromfile_Automation.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
