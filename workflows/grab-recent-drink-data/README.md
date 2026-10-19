# Grab recent drink data

This folder contains the **Grab recent drink data** workflow. Its executable nodes use `googleSheets`, `if`, `limit`, `merge`, `openAi`, `scheduleTrigger`, `set`, `slack`, `summarize`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`grab-recent-drink-data.json`](grab-recent-drink-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `slackOAuth2Api`

**Entry nodes:** Schedule Trigger, slack drink webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| slack_action_payload | `set` | Inspect parameters |
| slack_action_drink_data | `set` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Google Sheets - Get Target | `googleSheets` | Inspect parameters |
| Summarize | `summarize` | Inspect parameters |
| combine data | `merge` | Inspect parameters |
| If | `if` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| slack drink webhook | `webhook` | Inspect parameters |
| Slack send drink notification | `slack` | Inspect parameters |
| Send to Slack with confirm | `slack` | Inspect parameters |
| Edit Fields-Set progress | `set` | Inspect parameters |
| Google Sheets - log water value to sheet | `googleSheets` | append |
| Google Sheets - Get Today Water Log | `googleSheets` | Inspect parameters |

## Connection map

- If → Wait (`main`, output 0, input 0)
- If → OpenAI (`main`, output 1, input 0)
- Wait → OpenAI (`main`, output 0, input 0)
- Limit → combine data (`main`, output 0, input 1)
- OpenAI → Slack send drink notification (`main`, output 0, input 0)
- Summarize → combine data (`main`, output 0, input 2)
- combine data → Edit Fields-Set progress (`main`, output 0, input 0)
- Schedule Trigger → Google Sheets - Get Target (`main`, output 0, input 0)
- Schedule Trigger → Google Sheets - Get Today Water Log (`main`, output 0, input 0)
- slack drink webhook → slack_action_payload (`main`, output 0, input 0)
- slack_action_payload → slack_action_drink_data (`main`, output 0, input 0)
- slack_action_drink_data → Google Sheets - log water value to sheet (`main`, output 0, input 0)
- slack_action_drink_data → Send to Slack with confirm (`main`, output 0, input 0)
- Edit Fields-Set progress → If (`main`, output 0, input 0)
- Google Sheets - Get Target → combine data (`main`, output 0, input 0)
- Google Sheets - Get Today Water Log → Limit (`main`, output 0, input 0)
- Google Sheets - Get Today Water Log → Summarize (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0766_Wait_Limit_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0766_Wait_Limit_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
