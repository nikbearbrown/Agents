# push redis and receive twilio events and get redis 43bd0430

This folder contains the **push redis and receive twilio events and get redis 43bd0430** workflow. Its executable nodes use `agent`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `memoryManager`, `noOp`, `redis`, `set`, `twilio`, `twilioTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`push-redis-and-receive-twilio-events-and-get-redis-43bd0430.json`](push-redis-and-receive-twilio-events-and-get-redis-43bd0430.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `redis`, `twilioApi`

**Entry nodes:** Twilio Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Add to Messages Stack | `redis` | push |
| Should Continue? | `if` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Twilio Trigger | `twilioTrigger` | Inspect parameters |
| Get Latest Message Stack | `redis` | get |
| Send Reply | `twilio` | Inspect parameters |
| Wait 5 seconds | `wait` | Inspect parameters |
| Get Chat History | `memoryManager` | Inspect parameters |
| Window Buffer Memory1 | `memoryBufferWindow` | Inspect parameters |
| Get Messages Buffer | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- AI Agent → Send Reply (`main`, output 0, input 0)
- Twilio Trigger → Add to Messages Stack (`main`, output 0, input 0)
- Twilio Trigger → Wait 5 seconds (`main`, output 0, input 0)
- Wait 5 seconds → Get Latest Message Stack (`main`, output 0, input 0)
- Get Chat History → Get Messages Buffer (`main`, output 0, input 0)
- Should Continue? → Get Chat History (`main`, output 0, input 0)
- Should Continue? → No Operation, do nothing (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Get Messages Buffer → AI Agent (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Window Buffer Memory1 → Get Chat History (`ai_memory`, output 0, input 0)
- Get Latest Message Stack → Should Continue? (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1431_Wait_Redis_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1431_Wait_Redis_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
