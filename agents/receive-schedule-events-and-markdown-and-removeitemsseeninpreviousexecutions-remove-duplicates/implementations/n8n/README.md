# receive schedule events and markdown and removeitemsseeninpreviousexecutions remove duplicates

This folder contains the **receive schedule events and markdown and removeitemsseeninpreviousexecutions remove duplicates** workflow. Its executable nodes use `chainLlm`, `gmail`, `linear`, `lmChatOpenAi`, `markdown`, `outputParserStructured`, `removeDuplicates`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-markdown-and-removeitemsseeninpreviousexecutions-remove-duplicates.json`](receive-schedule-events-and-markdown-and-removeitemsseeninpreviousexecutions-remove-duplicates.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `linearApi`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Mark as Seen | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Generate Issue From Support Request | `chainLlm` | Inspect parameters |
| Get Recent Messages | `gmail` | getAll |
| Create Issue in Linear.App | `linear` | Inspect parameters |

## Connection map

- Markdown → Generate Issue From Support Request (`main`, output 0, input 0)
- Mark as Seen → Markdown (`main`, output 0, input 0)
- Schedule Trigger → Get Recent Messages (`main`, output 0, input 0)
- OpenAI Chat Model → Generate Issue From Support Request (`ai_languageModel`, output 0, input 0)
- Get Recent Messages → Mark as Seen (`main`, output 0, input 0)
- Structured Output Parser → Generate Issue From Support Request (`ai_outputParser`, output 0, input 0)
- Generate Issue From Support Request → Create Issue in Linear.App (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0912_Schedule_Removeduplicates_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0912_Schedule_Removeduplicates_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
