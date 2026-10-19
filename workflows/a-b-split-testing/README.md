# A/B Split Testing

This folder contains the **A/B Split Testing** workflow. Its executable nodes use `agent`, `chatTrigger`, `if`, `lmChatOpenAi`, `memoryPostgresChat`, `set`, `supabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`a-b-split-testing.json`](a-b-split-testing.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`, `supabaseApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Check If Session Exists | `supabase` | get |
| If Session Does Exist | `if` | Inspect parameters |
| Assign Path To Session | `supabase` | Inspect parameters |
| Define Path Values | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Get Correct Prompt | `set` | Inspect parameters |

## Connection map

- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Define Path Values → Check If Session Exists (`main`, output 0, input 0)
- Get Correct Prompt → AI Agent (`main`, output 0, input 0)
- Postgres Chat Memory → AI Agent (`ai_memory`, output 0, input 0)
- If Session Does Exist → Get Correct Prompt (`main`, output 0, input 0)
- If Session Does Exist → Assign Path To Session (`main`, output 1, input 0)
- Assign Path To Session → Get Correct Prompt (`main`, output 0, input 0)
- Check If Session Exists → If Session Does Exist (`main`, output 0, input 0)
- When chat message received → Define Path Values (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Supabase/1680_Supabase_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Supabase/1680_Supabase_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
