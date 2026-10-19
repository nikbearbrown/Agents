# Gmail labelling agent

This folder contains the **Gmail labelling agent** workflow. Its executable nodes use `agent`, `gmailTool`, `gmailTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`gmail-labelling-agent.json`](gmail-labelling-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Gmail - read labels | `gmailTool` | label |
| Gmail - get message | `gmailTool` | get |
| Gmail - add label to message | `gmailTool` | addLabels |
| Gmail - create label | `gmailTool` | label / create |
| Gmail labelling agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Wait | `wait` | Inspect parameters |

## Connection map

- Wait → Gmail labelling agent (`main`, output 0, input 0)
- Gmail Trigger → Wait (`main`, output 0, input 0)
- OpenAI Chat Model1 → Gmail labelling agent (`ai_languageModel`, output 0, input 0)
- Gmail - get message → Gmail labelling agent (`ai_tool`, output 0, input 0)
- Gmail - read labels → Gmail labelling agent (`ai_tool`, output 0, input 0)
- Gmail - create label → Gmail labelling agent (`ai_tool`, output 0, input 0)
- Window Buffer Memory → Gmail labelling agent (`ai_memory`, output 0, input 0)
- Gmail - add label to message → Gmail labelling agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1353_Stickynote_Gmail_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1353_Stickynote_Gmail_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
