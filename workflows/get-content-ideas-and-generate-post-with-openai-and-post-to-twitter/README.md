# get content ideas and generate post with openai and post to twitter

This folder contains the **get content ideas and generate post with openai and post to twitter** workflow. Its executable nodes use `googleSheets`, `if`, `openAi`, `twitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-content-ideas-and-generate-post-with-openai-and-post-to-twitter.json`](get-content-ideas-and-generate-post-with-openai-and-post-to-twitter.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAIApi`, `twitterOAuth1Api`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Content Ideas | `googleSheets` | Inspect parameters |
| Generate Post with OpenAI | `openAi` | Inspect parameters |
| Check Platform | `if` | Inspect parameters |
| Post to Twitter | `twitter` | Inspect parameters |
| Update Google Sheet | `googleSheets` | Inspect parameters |

## Connection map

- Check Platform → Post to Twitter (`main`, output 0, input 0)
- Post to Twitter → Update Google Sheet (`main`, output 0, input 0)
- Get Content Ideas → Generate Post with OpenAI (`main`, output 0, input 0)
- Generate Post with OpenAI → Check Platform (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/0785_Openai_Twitter_Create.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/0785_Openai_Twitter_Create.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
