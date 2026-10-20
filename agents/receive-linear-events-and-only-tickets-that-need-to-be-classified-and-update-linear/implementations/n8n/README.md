# receive linear events and only tickets that need to be classified and update linear

This folder contains the **receive linear events and only tickets that need to be classified and update linear** workflow. Its executable nodes use `filter`, `httpRequest`, `if`, `linear`, `linearTrigger`, `merge`, `openAi`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-linear-events-and-only-tickets-that-need-to-be-classified-and-update-linear.json`](receive-linear-events-and-only-tickets-that-need-to-be-classified-and-update-linear.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `linearApi`, `linearOAuth2Api`, `openAiApi`, `slackApi`

**Entry nodes:** Linear Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Linear Trigger | `linearTrigger` | Inspect parameters |
| Only tickets that need to be classified | `filter` | Inspect parameters |
| Update team | `linear` | update |
| Get all linear teams | `httpRequest` | POST |
| Set team ID | `set` | Inspect parameters |
| Set me up | `set` | Inspect parameters |
| Check if AI was able to find a team | `if` | Inspect parameters |
| Notify in Slack | `slack` | Inspect parameters |
| Merge data | `merge` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |

## Connection map

- OpenAI → Merge data (`main`, output 0, input 0)
- Set me up → Only tickets that need to be classified (`main`, output 0, input 0)
- Merge data → Check if AI was able to find a team (`main`, output 0, input 0)
- Set team ID → Update team (`main`, output 0, input 0)
- Linear Trigger → Set me up (`main`, output 0, input 0)
- Get all linear teams → Merge data (`main`, output 0, input 1)
- Check if AI was able to find a team → Set team ID (`main`, output 0, input 0)
- Check if AI was able to find a team → Notify in Slack (`main`, output 1, input 0)
- Only tickets that need to be classified → OpenAI (`main`, output 0, input 0)
- Only tickets that need to be classified → Get all linear teams (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0451_Filter_Slack_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0451_Filter_Slack_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
