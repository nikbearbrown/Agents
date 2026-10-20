# ⚙️ Turn blocks into rich text

This folder contains the **⚙️ Turn blocks into rich text** workflow. Its executable nodes use `code`, `compareDatasets`, `filter`, `merge`, `noOp`, `notion`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `webflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`turn-blocks-into-rich-text.json`](turn-blocks-into-rich-text.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `slackOAuth2Api`, `webflowOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get simple page data | `notion` | databasePage / get |
| Get all page data | `notion` | databasePage / get |
| Take cover url | `set` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Data transporter1 | `noOp` | Inspect parameters |
| Get all blog posts1 | `notion` | databasePage / getAll |
| Is sync checked?1 | `filter` | Inspect parameters |
| For each blog post1 | `splitInBatches` | Inspect parameters |
| Create post1 | `webflow` | create |
| Update slug on posts1 | `notion` | databasePage / update |
| Slug uniqueness checker and differentiator1 | `code` | Inspect parameters |
| Success message1 | `slack` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Compare by slug1 | `compareDatasets` | Inspect parameters |
| Add slug to posts1 | `notion` | databasePage / update |
| Get all collection posts1 | `webflow` | getAll |
| Data transporter, Notion posts to sync1 | `noOp` | Inspect parameters |
| Craft the rich text element1 | `code` | Inspect parameters |
| Turn blocks into HTML1 | `code` | Inspect parameters |
| Get blocks1 | `notion` | block / getAll |
| Update in "Blog Posts" | `webflow` | update |
| Add Webflow item id to Notion data | `code` | Inspect parameters |
| Final Notion post data | `merge` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Merge1 → Final Notion post data (`main`, output 0, input 0)
- Merge1 → Get blocks1 (`main`, output 0, input 0)
- Merge2 → Add slug to posts1 (`main`, output 0, input 0)
- Get blocks1 → Turn blocks into HTML1 (`main`, output 0, input 0)
- Create post1 → Merge2 (`main`, output 0, input 0)
- Take cover url → Merge1 (`main`, output 0, input 1)
- Compare by slug1 → Create post1 (`main`, output 0, input 0)
- Compare by slug1 → Merge2 (`main`, output 0, input 1)
- Compare by slug1 → Add Webflow item id to Notion data (`main`, output 2, input 0)
- Schedule Trigger → Get all blog posts1 (`main`, output 0, input 0)
- Data transporter1 → For each blog post1 (`main`, output 0, input 0)
- Get all page data → Take cover url (`main`, output 0, input 0)
- Is sync checked?1 → Slug uniqueness checker and differentiator1 (`main`, output 0, input 0)
- Add slug to posts1 → Data transporter1 (`main`, output 0, input 0)
- For each blog post1 → Success message1 (`main`, output 0, input 0)
- For each blog post1 → Get simple page data (`main`, output 1, input 0)
- For each blog post1 → Get all page data (`main`, output 1, input 0)
- Get all blog posts1 → Is sync checked?1 (`main`, output 0, input 0)
- Get simple page data → Merge1 (`main`, output 0, input 0)
- Update slug on posts1 → Data transporter1 (`main`, output 0, input 0)
- Final Notion post data → Data transporter, Notion posts to sync1 (`main`, output 0, input 0)
- Final Notion post data → Get all collection posts1 (`main`, output 0, input 0)
- Turn blocks into HTML1 → Craft the rich text element1 (`main`, output 0, input 0)
- Update in "Blog Posts" → Update slug on posts1 (`main`, output 0, input 0)
- Get all collection posts1 → Compare by slug1 (`main`, output 0, input 1)
- Craft the rich text element1 → Final Notion post data (`main`, output 0, input 1)
- Add Webflow item id to Notion data → Update in "Blog Posts" (`main`, output 0, input 0)
- Data transporter, Notion posts to sync1 → Compare by slug1 (`main`, output 0, input 0)
- Slug uniqueness checker and differentiator1 → For each blog post1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0506_Code_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0506_Code_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
