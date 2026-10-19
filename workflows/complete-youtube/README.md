# Complete Youtube

This folder contains the **Complete Youtube** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `splitInBatches`, `toolWorkflow`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`complete-youtube.json`](complete-youtube.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `youTubeOAuth2Api`

**Entry nodes:** chat_message_received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| chat_message_received | `chatTrigger` | Inspect parameters |
| youtube_search | `toolWorkflow` | Inspect parameters |
| openai_llm | `lmChatOpenAi` | Inspect parameters |
| window_buffer_memory | `memoryBufferWindow` | Inspect parameters |
| find_video_data1 | `httpRequest` | Inspect parameters |
| get_videos1 | `youTube` | video |
| response1 | `set` | Inspect parameters |
| group_data1 | `set` | Inspect parameters |
| save_data_to_memory1 | `code` | Inspect parameters |
| retrieve_data_from_memory1 | `code` | Inspect parameters |
| loop_over_items1 | `splitInBatches` | Inspect parameters |
| if_longer_than_3_ | `if` | Inspect parameters |

## Connection map

- openai_llm → AI Agent (`ai_languageModel`, output 0, input 0)
- get_videos1 → loop_over_items1 (`main`, output 0, input 0)
- group_data1 → save_data_to_memory1 (`main`, output 0, input 0)
- youtube_search → AI Agent (`ai_tool`, output 0, input 0)
- find_video_data1 → if_longer_than_3_ (`main`, output 0, input 0)
- loop_over_items1 → retrieve_data_from_memory1 (`main`, output 0, input 0)
- loop_over_items1 → find_video_data1 (`main`, output 1, input 0)
- if_longer_than_3_ → group_data1 (`main`, output 0, input 0)
- if_longer_than_3_ → loop_over_items1 (`main`, output 1, input 0)
- save_data_to_memory1 → loop_over_items1 (`main`, output 0, input 0)
- window_buffer_memory → AI Agent (`ai_memory`, output 0, input 0)
- chat_message_received → AI Agent (`main`, output 0, input 0)
- retrieve_data_from_memory1 → response1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1758_Code_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1758_Code_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
