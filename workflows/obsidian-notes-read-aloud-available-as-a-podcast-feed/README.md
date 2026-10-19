# Obsidian Notes Read Aloud: Available as a Podcast Feed

This folder contains the **Obsidian Notes Read Aloud: Available as a Podcast Feed** workflow. Its executable nodes use `aggregate`, `code`, `googleSheets`, `httpRequest`, `merge`, `openAi`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`obsidian-notes-read-aloud-available-as-a-podcast-feed.json`](obsidian-notes-read-aloud-available-as-a-podcast-feed.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpCustomAuth`, `openAiApi`

**Entry nodes:** Webhook GET Note, Webhook GET Podcast Feed

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI1 | `openAi` | audio |
| Webhook GET Note | `webhook` | Inspect parameters |
| Webhook GET Podcast Feed | `webhook` | Inspect parameters |
| Upload Audio to Cloudinary | `httpRequest` | POST |
| OpenAI | `openAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Give Audio Unique Name | `set` | Inspect parameters |
| Send Audio to Obsidian | `respondToWebhook` | Inspect parameters |
| Rename Fields | `set` | Inspect parameters |
| Append Item to Google Sheet | `googleSheets` | append |
| Get Items from Google Sheets | `googleSheets` | Inspect parameters |
| Write RSS Feed | `code` | Inspect parameters |
| Return Podcast Feed to Webhook | `respondToWebhook` | Inspect parameters |
| Manually Enter Other Data for Podcast Feed | `set` | Inspect parameters |

## Connection map

- Merge → Aggregate (`main`, output 0, input 0)
- OpenAI → Merge (`main`, output 0, input 1)
- OpenAI1 → Give Audio Unique Name (`main`, output 0, input 0)
- Aggregate → Rename Fields (`main`, output 0, input 0)
- Rename Fields → Append Item to Google Sheet (`main`, output 0, input 0)
- Write RSS Feed → Return Podcast Feed to Webhook (`main`, output 0, input 0)
- Webhook GET Note → OpenAI1 (`main`, output 0, input 0)
- Webhook GET Note → OpenAI (`main`, output 0, input 0)
- Give Audio Unique Name → Upload Audio to Cloudinary (`main`, output 0, input 0)
- Give Audio Unique Name → Send Audio to Obsidian (`main`, output 0, input 0)
- Webhook GET Podcast Feed → Get Items from Google Sheets (`main`, output 0, input 0)
- Upload Audio to Cloudinary → Merge (`main`, output 0, input 0)
- Get Items from Google Sheets → Manually Enter Other Data for Podcast Feed (`main`, output 0, input 0)
- Manually Enter Other Data for Podcast Feed → Write RSS Feed (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1578_Webhook_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1578_Webhook_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
