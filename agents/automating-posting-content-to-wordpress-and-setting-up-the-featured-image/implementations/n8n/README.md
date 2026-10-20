# Automating Posting content to WordPress and setting up the featured Image

This folder contains the **Automating Posting content to WordPress and setting up the featured Image** workflow. Its executable nodes use `airtable`, `filter`, `httpRequest`, `markdown`, `scheduleTrigger`, `set`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automating-posting-content-to-wordpress-and-setting-up-the-featured-image.json`](automating-posting-content-to-wordpress-and-setting-up-the-featured-image.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Post on Wordpress | `wordpress` | Inspect parameters |
| Upload Media | `httpRequest` | POST |
| Set Featured Image | `httpRequest` | POST |
| Edit Fields | `set` | Inspect parameters |
| Get content to post | `airtable` | search |
| Filter by existing Blogs | `filter` | Inspect parameters |
| Markdown to HTML | `markdown` | Inspect parameters |
| Get Image | `httpRequest` | Inspect parameters |
| Download the image | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Update POST on Airtable | `airtable` | update |

## Connection map

- Get Image → Download the image (`main`, output 0, input 0)
- Edit Fields → Markdown to HTML (`main`, output 0, input 0)
- Upload Media → Set Featured Image (`main`, output 0, input 0)
- Markdown to HTML → Post on Wordpress (`main`, output 0, input 0)
- Schedule Trigger → Get content to post (`main`, output 0, input 0)
- Post on Wordpress → Get Image (`main`, output 0, input 0)
- Download the image → Upload Media (`main`, output 0, input 0)
- Set Featured Image → Update POST on Airtable (`main`, output 0, input 0)
- Get content to post → Filter by existing Blogs (`main`, output 0, input 0)
- Filter by existing Blogs → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/0502_Wordpress_Filter_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wordpress/0502_Wordpress_Filter_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
