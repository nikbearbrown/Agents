# issues to list and sentiment over issue comments and search airtable 517a1983

This folder contains the **issues to list and sentiment over issue comments and search airtable 517a1983** workflow. Its executable nodes use `airtable`, `airtableTrigger`, `graphql`, `informationExtractor`, `lmChatOpenAi`, `removeDuplicates`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `splitOut`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`issues-to-list-and-sentiment-over-issue-comments-and-search-airtable-517a1983.json`](issues-to-list-and-sentiment-over-issue-comments-and-search-airtable-517a1983.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`, `openAiApi`, `slackApi`

**Entry nodes:** Airtable Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Issues to List | `splitOut` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Combine Sentiment Analysis | `set` | Inspect parameters |
| Sentiment over Issue Comments | `informationExtractor` | Inspect parameters |
| Copy of Issue | `set` | Inspect parameters |
| For Each Issue... | `splitInBatches` | Inspect parameters |
| Get Existing Sentiment | `airtable` | search |
| Update Row | `airtable` | upsert |
| Airtable Trigger | `airtableTrigger` | Inspect parameters |
| Sentiment Transition | `switch` | Inspect parameters |
| Fetch Active Linear Issues | `graphql` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Deduplicate Notifications | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Report Issue Negative Transition | `slack` | Inspect parameters |

## Connection map

- Update Row → For Each Issue... (`main`, output 0, input 0)
- Copy of Issue → Get Existing Sentiment (`main`, output 0, input 0)
- Issues to List → Sentiment over Issue Comments (`main`, output 0, input 0)
- Airtable Trigger → Sentiment Transition (`main`, output 0, input 0)
- Schedule Trigger → Fetch Active Linear Issues (`main`, output 0, input 0)
- For Each Issue... → Copy of Issue (`main`, output 1, input 0)
- OpenAI Chat Model → Sentiment over Issue Comments (`ai_languageModel`, output 0, input 0)
- Sentiment Transition → Deduplicate Notifications (`main`, output 0, input 0)
- Get Existing Sentiment → Update Row (`main`, output 0, input 0)
- Deduplicate Notifications → Report Issue Negative Transition (`main`, output 0, input 0)
- Combine Sentiment Analysis → For Each Issue... (`main`, output 0, input 0)
- Fetch Active Linear Issues → Issues to List (`main`, output 0, input 0)
- Sentiment over Issue Comments → Combine Sentiment Analysis (`main`, output 0, input 0)

## Verification and provenance

Selected from 6 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1657_Splitout_Schedule_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1657_Splitout_Schedule_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
