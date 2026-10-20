# basic llm chain and hacker news and http request

This folder contains the **basic llm chain and hacker news and http request** workflow. Its executable nodes use `aggregate`, `chainLlm`, `emailSend`, `formTrigger`, `hackerNews`, `httpRequest`, `lmChatGoogleGemini`, `markdown`, `noOp`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`basic-llm-chain-and-hacker-news-and-http-request.json`](basic-llm-chain-and-hacker-news-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `smtp`

**Entry nodes:** GetTopicFromToLearn

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| SearchAskHN | `hackerNews` | all |
| FindHNComments | `httpRequest` | Inspect parameters |
| CombineIntoSingleText | `aggregate` | Inspect parameters |
| SplitOutChildrenIDs | `splitOut` | Inspect parameters |
| GetTopicFromToLearn | `formTrigger` | Inspect parameters |
| SendEmailWithTopResources | `emailSend` | Inspect parameters |
| Convert2HTML | `markdown` | Inspect parameters |
| Finished | `noOp` | Inspect parameters |

## Connection map

- SearchAskHN → SplitOutChildrenIDs (`main`, output 0, input 0)
- Convert2HTML → SendEmailWithTopResources (`main`, output 0, input 0)
- FindHNComments → CombineIntoSingleText (`main`, output 0, input 0)
- Basic LLM Chain → Convert2HTML (`main`, output 0, input 0)
- GetTopicFromToLearn → SearchAskHN (`main`, output 0, input 0)
- SplitOutChildrenIDs → FindHNComments (`main`, output 0, input 0)
- CombineIntoSingleText → Basic LLM Chain (`main`, output 0, input 0)
- Google Gemini Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- SendEmailWithTopResources → Finished (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0680_Splitout_HTTP_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0680_Splitout_HTTP_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
