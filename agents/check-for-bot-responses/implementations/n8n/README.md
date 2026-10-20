# Check for Bot Responses

This folder contains the **Check for Bot Responses** workflow. Its executable nodes use `agent`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `noOp`, `respondToWebhook`, `slack`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`check-for-bot-responses.json`](check-for-bot-responses.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `slackApi`

**Entry nodes:** Receive DMs

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Verify Webhook | `respondToWebhook` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Check if Bot | `if` | Inspect parameters |
| Send Initial Message | `slack` | Inspect parameters |
| Delete Initial Message | `slack` | delete |
| Send Message | `slack` | Inspect parameters |
| Receive DMs | `webhook` | Inspect parameters |
| Call Confluence Workflow Tool | `toolWorkflow` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- AI Agent → Delete Initial Message (`main`, output 0, input 0)
- Receive DMs → Verify Webhook (`main`, output 0, input 0)
- Check if Bot → No Operation, do nothing (`main`, output 0, input 0)
- Check if Bot → Send Initial Message (`main`, output 1, input 0)
- Verify Webhook → Check if Bot (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Send Initial Message → AI Agent (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Delete Initial Message → Send Message (`main`, output 0, input 0)
- Call Confluence Workflow Tool → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1502_Webhook_Slack_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1502_Webhook_Slack_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
