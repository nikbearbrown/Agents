# ⏳ Inactivity & Threshold Check

This folder contains the **⏳ Inactivity & Threshold Check** workflow. Its executable nodes use `chatTrigger`, `code`, `executeWorkflowTrigger`, `if`, `informationExtractor`, `lmChatOpenAi`, `manualTrigger`, `noOp`, `redis`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`inactivity-threshold-check.json`](inactivity-threshold-check.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `redis`

**Entry nodes:** When clicking ‘Test workflow’, When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| No Operation, do nothing1 | `noOp` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| get wait seconds | `code` | Inspect parameters |
| Set last_seen | `redis` | set |
| Get waiting_reply | `redis` | get |
| Mod input | `set` | Inspect parameters |
| waiting_reply? | `if` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Set waiting_reply | `redis` | set |
| Get buffer | `redis` | get |
| Delete buffer_in | `redis` | delete |
| Delete waiting_reply | `redis` | delete |
| WaitSeconds | `wait` | Inspect parameters |
| Buffer messages | `redis` | push |
| Set buffer_count increment | `redis` | incr |
| Get last_seen | `redis` | get |
| Get buffer_count | `redis` | get |
| Map ouput | `set` | Inspect parameters |
| Check Inactivity + Count | `if` | Inspect parameters |
| Delete waiting_reply1 | `redis` | delete |
| No Operation, do nothing2 | `noOp` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Mock input data | `set` | Inspect parameters |
| No Operation, do nothing3 | `noOp` | Inspect parameters |

## Connection map

- Wait → Check Inactivity + Count (`main`, output 0, input 0)
- Mod input → waiting_reply? (`main`, output 0, input 0)
- Get buffer → Information Extractor (`main`, output 0, input 0)
- WaitSeconds → Get last_seen (`main`, output 0, input 0)
- Get last_seen → Get buffer_count (`main`, output 0, input 0)
- Set last_seen → No Operation, do nothing2 (`main`, output 0, input 0)
- waiting_reply? → No Operation, do nothing2 (`main`, output 0, input 0)
- waiting_reply? → Set waiting_reply (`main`, output 1, input 0)
- Buffer messages → Set buffer_count increment (`main`, output 0, input 0)
- Buffer messages → Set last_seen (`main`, output 0, input 0)
- Buffer messages → Get waiting_reply (`main`, output 0, input 0)
- Mock input data → get wait seconds (`main`, output 0, input 0)
- Delete buffer_in → No Operation, do nothing3 (`main`, output 0, input 0)
- Get buffer_count → Check Inactivity + Count (`main`, output 0, input 0)
- get wait seconds → Buffer messages (`main`, output 0, input 0)
- Get waiting_reply → Mod input (`main`, output 0, input 0)
- OpenAI Chat Model → Information Extractor (`ai_languageModel`, output 0, input 0)
- Set waiting_reply → WaitSeconds (`main`, output 0, input 0)
- Delete waiting_reply → No Operation, do nothing3 (`main`, output 0, input 0)
- Delete waiting_reply1 → No Operation, do nothing3 (`main`, output 0, input 0)
- Information Extractor → Map ouput (`main`, output 0, input 0)
- Information Extractor → Delete buffer_in (`main`, output 0, input 0)
- Information Extractor → Delete waiting_reply (`main`, output 0, input 0)
- Information Extractor → Delete waiting_reply1 (`main`, output 0, input 0)
- Check Inactivity + Count → Get buffer (`main`, output 0, input 0)
- Check Inactivity + Count → No Operation, do nothing1 (`main`, output 1, input 0)
- No Operation, do nothing1 → Wait (`main`, output 0, input 0)
- Set buffer_count increment → No Operation, do nothing2 (`main`, output 0, input 0)
- When chat message received → Mock input data (`main`, output 0, input 0)
- When Executed by Another Workflow → get wait seconds (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Mock input data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0903_Wait_Redis_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0903_Wait_Redis_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
