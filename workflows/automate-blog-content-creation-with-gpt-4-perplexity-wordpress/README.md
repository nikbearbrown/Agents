# 💥🛠️Automate Blog Content Creation with GPT-4, Perplexity & WordPress

This folder contains the **💥🛠️Automate Blog Content Creation with GPT-4, Perplexity & WordPress** workflow. Its executable nodes use `agent`, `chatTrigger`, `formTrigger`, `gmailTool`, `httpRequest`, `lmChatOpenAi`, `mcpClientTool`, `set`, `wordpressTool`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-blog-content-creation-with-gpt-4-perplexity-wordpress.json`](automate-blog-content-creation-with-gpt-4-perplexity-wordpress.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `httpHeaderAuth`, `mcpClientApi`, `openAiApi`, `wordpressApi`

**Entry nodes:** When chat message received, Start with Research Query Submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Perplexity Research | `httpRequest` | POST |
| When chat message received | `chatTrigger` | Inspect parameters |
| Slack-List | `mcpClientTool` | Inspect parameters |
| Copywriting AI Agent | `agent` | Inspect parameters |
| Format Research Output | `set` | Inspect parameters |
| Publish Article to WordPress | `wordpressTool` | Inspect parameters |
| Send Email Notification | `gmailTool` | Inspect parameters |
| Notify Slack Channel | `mcpClientTool` | executeTool |
| Generate SEO Blog Content (GPT-4o) | `lmChatOpenAi` | Inspect parameters |
| Start with Research Query Submission | `formTrigger` | Inspect parameters |
| Edit Workflow Variables | `set` | Inspect parameters |
| Notion-List | `mcpClientTool` | Inspect parameters |
| Insert Article in Notion | `mcpClientTool` | executeTool |

## Connection map

- Slack-List → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- Notion-List → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- Perplexity Research → Format Research Output (`main`, output 0, input 0)
- Notify Slack Channel → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- Format Research Output → Edit Workflow Variables (`main`, output 0, input 0)
- Edit Workflow Variables → Copywriting AI Agent (`main`, output 0, input 0)
- Send Email Notification → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- Insert Article in Notion → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → Copywriting AI Agent (`main`, output 0, input 0)
- Publish Article to WordPress → Copywriting AI Agent (`ai_tool`, output 0, input 0)
- Generate SEO Blog Content (GPT-4o) → Copywriting AI Agent (`ai_languageModel`, output 0, input 0)
- Start with Research Query Submission → Perplexity Research (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1535_HTTP_Form_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1535_HTTP_Form_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
