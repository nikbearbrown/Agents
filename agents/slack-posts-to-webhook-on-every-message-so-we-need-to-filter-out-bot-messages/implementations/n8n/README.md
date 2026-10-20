# Slack POSTs to Webhook on every message so we need to filter-out bot messages

This folder contains the **Slack POSTs to Webhook on every message so we need to filter-out bot messages** workflow. Its executable nodes use `agent`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `noOp`, `slack`, `toolSerpApi`, `toolWikipedia`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`slack-posts-to-webhook-on-every-message-so-we-need-to-filter-out-bot-messages.json`](slack-posts-to-webhook-on-every-message-so-we-need-to-filter-out-bot-messages.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `serpApi`, `slackApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Is user message? | `if` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| SerpAPI | `toolSerpApi` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- SerpAPI → AI Agent (`ai_tool`, output 0, input 0)
- Webhook → Is user message? (`main`, output 0, input 0)
- AI Agent → Slack (`main`, output 0, input 0)
- Wikipedia → AI Agent (`ai_tool`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Is user message? → AI Agent (`main`, output 0, input 0)
- Is user message? → No Operation, do nothing (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0327_Noop_Slack_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0327_Noop_Slack_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
