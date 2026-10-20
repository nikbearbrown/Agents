# Auto WordPress Blog Generator (GPT + Postgres + WP Media)

This folder contains the **Auto WordPress Blog Generator (GPT + Postgres + WP Media)** workflow. Its executable nodes use `agent`, `code`, `httpRequest`, `lmChatOpenAi`, `merge`, `noOp`, `postgres`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auto-wordpress-blog-generator-gpt-postgres-wp-media.json`](auto-wordpress-blog-generator-gpt-postgres-wp-media.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`, `wordpressApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| Prepare Post JSON | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Load Categories | `httpRequest` | Inspect parameters |
| Category Filter | `code` | Inspect parameters |
| Selecting recent | `postgres` | executeQuery |
| Picks Less Used | `code` | Inspect parameters |
| 10 latest headlines | `postgres` | executeQuery |
| New article title | `code` | Inspect parameters |
| AI Agent SEO Headings | `agent` | Inspect parameters |
| AI Agent SEO writer | `agent` | Inspect parameters |
| Merge heading | `merge` | Inspect parameters |
| Combines full post meta | `code` | Inspect parameters |
| Updating posts DB | `postgres` | upsert |
| Extracting output | `code` | Inspect parameters |
| Placeholder creator | `code` | Inspect parameters |
| Media Upload to WP | `httpRequest` | POST |
| Post to WP | `httpRequest` | POST |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Config | `set` | Inspect parameters |

## Connection map

- Merge → Prepare Post JSON (`main`, output 0, input 0)
- Config → Load Categories (`main`, output 0, input 0)
- Post to WP → No Operation, do nothing (`main`, output 0, input 0)
- Merge heading → Combines full post meta (`main`, output 0, input 0)
- Download Image → Media Upload to WP (`main`, output 0, input 0)
- Category Filter → Selecting recent (`main`, output 0, input 0)
- Load Categories → Category Filter (`main`, output 0, input 0)
- Picks Less Used → 10 latest headlines (`main`, output 0, input 0)
- Picks Less Used → Merge heading (`main`, output 0, input 0)
- Schedule Trigger → Config (`main`, output 0, input 0)
- Selecting recent → Picks Less Used (`main`, output 0, input 0)
- Extracting output → Merge (`main`, output 0, input 1)
- New article title → Merge heading (`main`, output 0, input 1)
- OpenAI Chat Model → AI Agent SEO writer (`ai_languageModel`, output 0, input 0)
- Prepare Post JSON → Post to WP (`main`, output 0, input 0)
- Updating posts DB → AI Agent SEO writer (`main`, output 0, input 0)
- Updating posts DB → Merge (`main`, output 0, input 0)
- Media Upload to WP → Merge (`main`, output 0, input 2)
- OpenAI Chat Model1 → AI Agent SEO Headings (`ai_languageModel`, output 0, input 0)
- 10 latest headlines → AI Agent SEO Headings (`main`, output 0, input 0)
- AI Agent SEO writer → Placeholder creator (`main`, output 0, input 0)
- AI Agent SEO writer → Extracting output (`main`, output 0, input 0)
- Placeholder creator → Download Image (`main`, output 0, input 0)
- AI Agent SEO Headings → New article title (`main`, output 0, input 0)
- Combines full post meta → Updating posts DB (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/0263_Postgres_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/0263_Postgres_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
