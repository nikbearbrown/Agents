# AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack

This folder contains the **AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack** workflow. Its executable nodes use `dateTime`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `noOp`, `openAi`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `textClassifier`, `webhook`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-generated-summary-block-for-wordpress-posts-with-openai-wordpress-google-sheets-slack.json`](ai-generated-summary-block-for-wordpress-posts-with-openai-wordpress-google-sheets-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpHeaderAuth`, `openAiApi`, `slackOAuth2Api`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’, Webhook, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| If | `if` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Wordpress - Update Post | `httpRequest` | POST |
| Google Sheets - Get rows | `googleSheets` | Inspect parameters |
| HTML to Markdown | `markdown` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Google Sheets - Add Row | `googleSheets` | append |
| Slack - Notify Channel | `slack` | Inspect parameters |
| Set fields - From Webhook input | `set` | Inspect parameters |
| Date & Time - Substract | `dateTime` | subtractFromDate |
| Set fields - Prepare data for Gsheets & Slack | `set` | Inspect parameters |
| WordPress - Get Post2 | `wordpress` | get |
| No Operation, do nothing | `noOp` | Inspect parameters |
| WordPress - Get Last Posts | `wordpress` | getAll |
| WordPress - Get Post1 | `wordpress` | get |
| WordPress - Get All Posts | `wordpress` | getAll |

## Connection map

- If → Loop Over Items (`main`, output 0, input 0)
- If → WordPress - Get Post2 (`main`, output 1, input 0)
- OpenAI → Wordpress - Update Post (`main`, output 0, input 0)
- Webhook → Set fields - From Webhook input (`main`, output 0, input 0)
- Loop Over Items → No Operation, do nothing (`main`, output 0, input 0)
- Loop Over Items → Google Sheets - Get rows (`main`, output 1, input 0)
- Text Classifier → OpenAI (`main`, output 0, input 0)
- Text Classifier → Loop Over Items (`main`, output 1, input 0)
- HTML to Markdown → Text Classifier (`main`, output 0, input 0)
- Schedule Trigger → Date & Time - Substract (`main`, output 0, input 0)
- OpenAI Chat Model → Text Classifier (`ai_languageModel`, output 0, input 0)
- WordPress - Get Post2 → HTML to Markdown (`main`, output 0, input 0)
- Slack - Notify Channel → Loop Over Items (`main`, output 0, input 0)
- Date & Time - Substract → WordPress - Get Last Posts (`main`, output 0, input 0)
- Google Sheets - Add Row → Slack - Notify Channel (`main`, output 0, input 0)
- Wordpress - Update Post → Set fields - Prepare data for Gsheets & Slack (`main`, output 0, input 0)
- Google Sheets - Get rows → If (`main`, output 0, input 0)
- WordPress - Get All Posts → Loop Over Items (`main`, output 0, input 0)
- Set fields - From Webhook input → WordPress - Get Post1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → WordPress - Get All Posts (`main`, output 0, input 0)
- Set fields - Prepare data for Gsheets & Slack → Google Sheets - Add Row (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1272_Datetime_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1272_Datetime_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
