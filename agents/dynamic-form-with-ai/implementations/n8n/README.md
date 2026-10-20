# Dynamic Form with AI

This folder contains the **Dynamic Form with AI** workflow. Its executable nodes use `aggregate`, `chainLlm`, `filter`, `form`, `formTrigger`, `lmChatOpenAi`, `outputParserStructured`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dynamic-form-with-ai.json`](dynamic-form-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Get Basic Information

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Clarification Questions | `form` | Inspect parameters |
| Get Basic Information | `formTrigger` | Inspect parameters |
| Get Business Overview | `form` | Inspect parameters |
| End Form | `form` | completion |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Remove Already Answered Questions | `filter` | Inspect parameters |
| Analyse Response | `chainLlm` | Inspect parameters |
| Split Out Analysis | `splitOut` | Inspect parameters |
| Prepare For Form Generation | `set` | Inspect parameters |
| Aggregate For Form Generation | `aggregate` | Inspect parameters |

## Connection map

- Analyse Response → Split Out Analysis (`main`, output 0, input 0)
- OpenAI Chat Model → Analyse Response (`ai_languageModel`, output 0, input 0)
- Split Out Analysis → Remove Already Answered Questions (`main`, output 0, input 0)
- Get Basic Information → Get Business Overview (`main`, output 0, input 0)
- Get Business Overview → Analyse Response (`main`, output 0, input 0)
- Clarification Questions → End Form (`main`, output 0, input 0)
- Structured Output Parser → Analyse Response (`ai_outputParser`, output 0, input 0)
- Prepare For Form Generation → Aggregate For Form Generation (`main`, output 0, input 0)
- Aggregate For Form Generation → Clarification Questions (`main`, output 0, input 0)
- Remove Already Answered Questions → Prepare For Form Generation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1784_Splitout_Filter_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1784_Splitout_Filter_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
