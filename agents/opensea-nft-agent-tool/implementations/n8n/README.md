# OpenSea NFT Agent Tool

This folder contains the **OpenSea NFT Agent Tool** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`opensea-nft-agent-tool.json`](opensea-nft-agent-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`

**Entry nodes:** Workflow Input Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| NFT Agent Brain | `lmChatOpenAi` | Inspect parameters |
| NFT Agent Memory | `memoryBufferWindow` | Inspect parameters |
| OpenSea NFT Agent | `agent` | Inspect parameters |
| Workflow Input Trigger | `executeWorkflowTrigger` | Inspect parameters |
| OpenSea Get Account | `toolHttpRequest` | Inspect parameters |
| OpenSea Get Collection | `toolHttpRequest` | Inspect parameters |
| OpenSea Get Collections | `toolHttpRequest` | Inspect parameters |
| OpenSea Get Contract | `toolHttpRequest` | Inspect parameters |
| OpenSea Get NFT | `toolHttpRequest` | Inspect parameters |
| OpenSea Get NFTs by Account | `toolHttpRequest` | Inspect parameters |
| OpenSea Get NFTs by Collection | `toolHttpRequest` | Inspect parameters |
| OpenSea Get NFTs by Contract | `toolHttpRequest` | Inspect parameters |
| OpenSea Get Payment Token | `toolHttpRequest` | Inspect parameters |
| OpenSea Get Traits | `toolHttpRequest` | Inspect parameters |

## Connection map

- NFT Agent Brain → OpenSea NFT Agent (`ai_languageModel`, output 0, input 0)
- OpenSea Get NFT → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- NFT Agent Memory → OpenSea NFT Agent (`ai_memory`, output 0, input 0)
- OpenSea Get Traits → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get Account → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get Contract → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get Collection → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- Workflow Input Trigger → OpenSea NFT Agent (`main`, output 0, input 0)
- OpenSea Get Collections → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get Payment Token → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get NFTs by Account → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get NFTs by Contract → OpenSea NFT Agent (`ai_tool`, output 0, input 0)
- OpenSea Get NFTs by Collection → OpenSea NFT Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1779_Stickynote_Executeworkflow_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1779_Stickynote_Executeworkflow_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
