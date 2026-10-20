# Figure out issue assignee and title (shortening if necessary)

This folder contains the **Figure out issue assignee and title (shortening if necessary)** workflow. Its executable nodes use `aggregate`, `code`, `filter`, `formTrigger`, `graphql`, `httpRequest`, `if`, `linear`, `notion`, `openAi`, `respondToWebhook`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`figure-out-issue-assignee-and-title-shortening-if-necessary.json`](figure-out-issue-assignee-and-title-shortening-if-necessary.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `linearApi`, `notionApi`, `openAiApi`

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Fetch Linear team details | `graphql` | Inspect parameters |
| Get issue contents | `notion` | block / getAll |
| Aggregate | `aggregate` | Inspect parameters |
| Prepare issue data | `set` | Inspect parameters |
| Create linear issue | `linear` | Inspect parameters |
| Set assignee and title | `code` | Inspect parameters |
| Team missing? | `if` | Inspect parameters |
| Set page URL | `set` | Inspect parameters |
| Set team ID | `set` | Inspect parameters |
| Add link to Notion block | `httpRequest` | PATCH |
| Get issue URL | `graphql` | Inspect parameters |
| Shorten title | `openAi` | Inspect parameters |
| Unimported, unchecked to_do blocks only | `filter` | Inspect parameters |
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Get issues | `notion` | block / getAll |
| Convert contents to Markdown | `code` | Inspect parameters |
| Respond with error | `respondToWebhook` | Inspect parameters |
| Respond with error1 | `respondToWebhook` | Inspect parameters |

## Connection map

- Aggregate → Prepare issue data (`main`, output 0, input 0)
- Get issues → Unimported, unchecked to_do blocks only (`main`, output 0, input 0)
- Get issues → Respond with error (`main`, output 1, input 0)
- Set team ID → Get issues (`main`, output 0, input 0)
- Set page URL → Convert contents to Markdown (`main`, output 0, input 0)
- Get issue URL → Add link to Notion block (`main`, output 0, input 0)
- Shorten title → Get issue contents (`main`, output 0, input 0)
- Team missing? → Respond with error1 (`main`, output 0, input 0)
- Team missing? → Set team ID (`main`, output 1, input 0)
- Loop Over Items → Set assignee and title (`main`, output 1, input 0)
- n8n Form Trigger → Fetch Linear team details (`main`, output 0, input 0)
- Get issue contents → Set page URL (`main`, output 0, input 0)
- Prepare issue data → Create linear issue (`main`, output 0, input 0)
- Create linear issue → Get issue URL (`main`, output 0, input 0)
- Set assignee and title → Shorten title (`main`, output 0, input 0)
- Add link to Notion block → Loop Over Items (`main`, output 0, input 0)
- Fetch Linear team details → Team missing? (`main`, output 0, input 0)
- Convert contents to Markdown → Aggregate (`main`, output 0, input 0)
- Unimported, unchecked to_do blocks only → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0438_Code_Filter_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0438_Code_Filter_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
