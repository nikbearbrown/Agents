# Write a WordPress post with AI (starting from a few keywords)

This folder contains the **Write a WordPress post with AI (starting from a few keywords)** workflow. Its executable nodes use `code`, `formTrigger`, `httpRequest`, `if`, `merge`, `openAi`, `respondToWebhook`, `set`, `splitOut`, `toolWikipedia`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`write-a-wordpress-post-with-ai-starting-from-a-few-keywords.json`](write-a-wordpress-post-with-ai-starting-from-a-few-keywords.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `wordpressApi`

**Entry nodes:** Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Form | `formTrigger` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Check data consistency | `if` | Inspect parameters |
| Split out chapters | `splitOut` | Inspect parameters |
| Merge chapters title and text | `merge` | Inspect parameters |
| Final article text | `code` | Inspect parameters |
| Post on Wordpress | `wordpress` | Inspect parameters |
| Upload media | `httpRequest` | POST |
| Set image ID for the post | `httpRequest` | POST |
| Respond: Success | `respondToWebhook` | Inspect parameters |
| Respond: Error | `respondToWebhook` | Inspect parameters |
| Generate featured image | `openAi` | image |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Create post title and structure | `openAi` | Inspect parameters |
| Create chapters text | `openAi` | Inspect parameters |

## Connection map

- Form → Settings (`main`, output 0, input 0)
- Settings → Create post title and structure (`main`, output 0, input 0)
- Wikipedia → Create post title and structure (`ai_tool`, output 0, input 0)
- Upload media → Set image ID for the post (`main`, output 0, input 0)
- Post on Wordpress → Generate featured image (`main`, output 0, input 0)
- Final article text → Post on Wordpress (`main`, output 0, input 0)
- Split out chapters → Merge chapters title and text (`main`, output 0, input 1)
- Split out chapters → Create chapters text (`main`, output 0, input 0)
- Create chapters text → Merge chapters title and text (`main`, output 0, input 0)
- Check data consistency → Split out chapters (`main`, output 0, input 0)
- Check data consistency → Respond: Error (`main`, output 1, input 0)
- Generate featured image → Upload media (`main`, output 0, input 0)
- Set image ID for the post → Respond: Success (`main`, output 0, input 0)
- Merge chapters title and text → Final article text (`main`, output 0, input 0)
- Create post title and structure → Check data consistency (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1753_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1753_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
