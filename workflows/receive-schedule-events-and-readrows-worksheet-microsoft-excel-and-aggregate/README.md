# receive schedule events and readrows worksheet microsoft excel and aggregate

This folder contains the **receive schedule events and readrows worksheet microsoft excel and aggregate** workflow. Its executable nodes use `aggregate`, `chainLlm`, `html`, `httpRequest`, `if`, `lmChatOpenAi`, `merge`, `microsoftExcel`, `microsoftOutlook`, `noOp`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-readrows-worksheet-microsoft-excel-and-aggregate.json`](receive-schedule-events-and-readrows-worksheet-microsoft-excel-and-aggregate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftExcelOAuth2Api`, `microsoftOutlookOAuth2Api`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Subscribers | `microsoftExcel` | worksheet / readRows |
| Get Unique Categories | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Collect Fields | `set` | Inspect parameters |
| Categories to Items | `splitOut` | Inspect parameters |
| For Each Category | `splitInBatches` | Inspect parameters |
| Workflows to Items | `splitOut` | Inspect parameters |
| Workflow Summarizer | `chainLlm` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Fetch Latest 10 per Category | `httpRequest` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Get Relevant Workflows | `set` | Inspect parameters |
| Flatten Workflows | `set` | Inspect parameters |
| Remove Already Seen | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Workflow to Items | `splitOut` | Inspect parameters |
| Combine Workflows | `aggregate` | Inspect parameters |
| Has New Workflows? | `if` | Inspect parameters |
| With User Reference | `set` | Inspect parameters |
| Generate HTML Template | `html` | Inspect parameters |
| Parse Rows | `set` | Inspect parameters |
| Send Daily Digest | `microsoftOutlook` | Inspect parameters |
| Append Category | `set` | Inspect parameters |
| For Each Subscriber | `splitInBatches` | Inspect parameters |

## Connection map

- Merge → For Each Subscriber (`main`, output 0, input 0)
- Aggregate → For Each Category (`main`, output 0, input 0)
- Parse Rows → Get Unique Categories (`main`, output 0, input 0)
- Parse Rows → Merge (`main`, output 0, input 0)
- Collect Fields → Aggregate (`main`, output 0, input 0)
- Append Category → For Each Category (`main`, output 0, input 0)
- Get Subscribers → Parse Rows (`main`, output 0, input 0)
- Schedule Trigger → Get Subscribers (`main`, output 0, input 0)
- Combine Workflows → With User Reference (`main`, output 0, input 0)
- Flatten Workflows → Merge (`main`, output 0, input 1)
- For Each Category → Flatten Workflows (`main`, output 0, input 0)
- For Each Category → Workflows to Items (`main`, output 1, input 0)
- OpenAI Chat Model → Workflow Summarizer (`ai_languageModel`, output 0, input 0)
- Workflow to Items → Remove Already Seen (`main`, output 0, input 0)
- Has New Workflows? → Generate HTML Template (`main`, output 0, input 0)
- Has New Workflows? → No Operation, do nothing (`main`, output 1, input 0)
- Workflows to Items → Workflow Summarizer (`main`, output 0, input 0)
- Categories to Items → Fetch Latest 10 per Category (`main`, output 0, input 0)
- For Each Subscriber → Has New Workflows? (`main`, output 0, input 0)
- For Each Subscriber → Get Relevant Workflows (`main`, output 1, input 0)
- Remove Already Seen → Combine Workflows (`main`, output 0, input 0)
- With User Reference → For Each Subscriber (`main`, output 0, input 0)
- Workflow Summarizer → Collect Fields (`main`, output 0, input 0)
- Get Unique Categories → Categories to Items (`main`, output 0, input 0)
- Generate HTML Template → Send Daily Digest (`main`, output 0, input 0)
- Get Relevant Workflows → Workflow to Items (`main`, output 0, input 0)
- Fetch Latest 10 per Category → Append Category (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0833_Splitout_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0833_Splitout_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
