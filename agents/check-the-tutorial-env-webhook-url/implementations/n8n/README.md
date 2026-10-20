# [Check the Tutorial]({{ $env.WEBHOOK_URL }}

This folder contains the **[Check the Tutorial]({{ $env.WEBHOOK_URL }}** workflow. Its executable nodes use `agent`, `code`, `gmail`, `googleSheets`, `html`, `httpRequest`, `if`, `lmChatOpenAi`, `merge`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`check-the-tutorial-env-webhook-url.json`](check-the-tutorial-env-webhook-url.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Trigger at 08:30 am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If | `if` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Agent Classification | `agent` | Inspect parameters |
| Get Sustainability News | `googleSheets` | Inspect parameters |
| Send to your mailing list | `gmail` | Inspect parameters |
| Generate Email HTML | `code` | Inspect parameters |
| Parse Article Blocks | `html` | extractHtmlContent |
| Extract Articles Blocks | `html` | extractHtmlContent |
| Trigger at 08:30 am | `scheduleTrigger` | Inspect parameters |
| Query EU News Website | `httpRequest` | Inspect parameters |
| Split Out by Article Block | `splitOut` | Inspect parameters |
| Loop Over Articles | `splitInBatches` | Inspect parameters |
| Sustainability Flag | `set` | Inspect parameters |
| Merge Article + Flag | `merge` | Inspect parameters |
| Record Results | `googleSheets` | append |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |

## Connection map

- If → Loop Over Articles (`main`, output 0, input 0)
- Record Results → Loop Over Articles (`main`, output 0, input 0)
- Loop Over Articles → Agent Classification (`main`, output 1, input 0)
- Loop Over Articles → Merge Article + Flag (`main`, output 1, input 1)
- OpenAI Chat Model3 → Agent Classification (`ai_languageModel`, output 0, input 0)
- Generate Email HTML → Send to your mailing list (`main`, output 0, input 0)
- Sustainability Flag → Merge Article + Flag (`main`, output 0, input 0)
- Trigger at 08:30 am → Query EU News Website (`main`, output 0, input 0)
- Trigger at 08:30 am → Get Sustainability News (`main`, output 0, input 0)
- Agent Classification → Sustainability Flag (`main`, output 0, input 0)
- Merge Article + Flag → Record Results (`main`, output 0, input 0)
- Parse Article Blocks → If (`main`, output 0, input 0)
- Query EU News Website → Extract Articles Blocks (`main`, output 0, input 0)
- Extract Articles Blocks → Split Out by Article Block (`main`, output 0, input 0)
- Get Sustainability News → Generate Email HTML (`main`, output 0, input 0)
- Structured Output Parser → Agent Classification (`ai_outputParser`, output 0, input 0)
- Split Out by Article Block → Parse Article Blocks (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0883_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0883_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
