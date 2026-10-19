# Auto-Tag Blog Posts in WordPress with AI

This folder contains the **Auto-Tag Blog Posts in WordPress with AI** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `httpRequest`, `if`, `lmChatOpenAi`, `outputParserAutofixing`, `outputParserStructured`, `rssFeedReadTrigger`, `set`, `splitInBatches`, `splitOut`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auto-tag-blog-posts-in-wordpress-with-ai.json`](auto-tag-blog-posts-in-wordpress-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `wordpressApi`

**Entry nodes:** RSS Feed Trigger, Demo Usage in Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| RSS Feed Trigger | `rssFeedReadTrigger` | Inspect parameters |
| Return article details | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Loop over articles | `splitInBatches` | Inspect parameters |
| SET initial record | `set` | Inspect parameters |
| GET WP tags | `httpRequest` | Inspect parameters |
| POST WP tags | `httpRequest` | POST |
| GET updated WP tags | `httpRequest` | Inspect parameters |
| Keep matches | `filter` | Inspect parameters |
| Combine tag_ids | `aggregate` | Inspect parameters |
| Combine slugs | `aggregate` | Inspect parameters |
| If | `if` | Inspect parameters |
| MOCK article | `set` | Inspect parameters |
| Return missing tags | `code` | Inspect parameters |
| Wordpress | `wordpress` | Inspect parameters |
| Demo Usage in Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Auto-Tag Posts in WordPress | `executeWorkflow` | Inspect parameters |
| Generate tags for article | `chainLlm` | Inspect parameters |

## Connection map

- If → GET updated WP tags (`main`, output 0, input 0)
- If → Split Out (`main`, output 1, input 0)
- Split Out → POST WP tags (`main`, output 0, input 0)
- GET WP tags → Combine slugs (`main`, output 0, input 0)
- Keep matches → Combine tag_ids (`main`, output 0, input 0)
- MOCK article → Auto-Tag Posts in WordPress (`main`, output 0, input 0)
- POST WP tags → GET updated WP tags (`main`, output 0, input 0)
- Combine slugs → Return missing tags (`main`, output 0, input 0)
- Combine tag_ids → Loop over articles (`main`, output 0, input 0)
- RSS Feed Trigger → Generate tags for article (`main`, output 0, input 0)
- OpenAI Chat Model → Generate tags for article (`ai_languageModel`, output 0, input 0)
- Loop over articles → SET initial record (`main`, output 1, input 0)
- OpenAI Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- SET initial record → GET WP tags (`main`, output 0, input 0)
- GET updated WP tags → Keep matches (`main`, output 0, input 0)
- Return missing tags → If (`main`, output 0, input 0)
- Return article details → Wordpress (`main`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Generate tags for article (`ai_outputParser`, output 0, input 0)
- Generate tags for article → MOCK article (`main`, output 0, input 0)
- Auto-Tag Posts in WordPress → Return article details (`main`, output 0, input 0)
- Demo Usage in Another Workflow → Loop over articles (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1323_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1323_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
