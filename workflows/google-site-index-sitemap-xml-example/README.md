# Google Site Index - sitemap.xml example

This folder contains the **Google Site Index - sitemap.xml example** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `sort`, `splitInBatches`, `splitOut`, `wait`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-site-index-sitemap-xml-example.json`](google-site-index-sitemap-xml-example.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleOAuth2Api`

**Entry nodes:** When clicking "Test workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Check status | `httpRequest` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| URL Updated | `httpRequest` | POST |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| is new? | `if` | Inspect parameters |
| Get content-specific sitemaps | `splitOut` | Inspect parameters |
| Convert sitemap to JSON | `xml` | Inspect parameters |
| Force urlset.url to array | `set` | Inspect parameters |
| Assign mandatiry sitemap fields | `set` | Inspect parameters |
| convert page data to JSON | `xml` | Inspect parameters |
| Get sitemap.xml | `httpRequest` | Inspect parameters |
| Get content of each sitemap | `httpRequest` | Inspect parameters |
| Sort | `sort` | Inspect parameters |

## Connection map

- Sort → Assign mandatiry sitemap fields (`main`, output 0, input 0)
- Wait → Loop Over Items (`main`, output 0, input 0)
- is new? → URL Updated (`main`, output 0, input 0)
- is new? → Wait (`main`, output 1, input 0)
- Split Out → Sort (`main`, output 0, input 0)
- URL Updated → Wait (`main`, output 0, input 0)
- Check status → is new? (`main`, output 0, input 0)
- Check status → URL Updated (`main`, output 1, input 0)
- Get sitemap.xml → Convert sitemap to JSON (`main`, output 0, input 0)
- Loop Over Items → Check status (`main`, output 1, input 0)
- Schedule Trigger → Get sitemap.xml (`main`, output 0, input 0)
- Convert sitemap to JSON → Get content-specific sitemaps (`main`, output 0, input 0)
- Force urlset.url to array → Split Out (`main`, output 0, input 0)
- convert page data to JSON → Force urlset.url to array (`main`, output 0, input 0)
- Get content of each sitemap → convert page data to JSON (`main`, output 0, input 0)
- Get content-specific sitemaps → Get content of each sitemap (`main`, output 0, input 0)
- When clicking "Test workflow" → Get sitemap.xml (`main`, output 0, input 0)
- Assign mandatiry sitemap fields → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1145_Wait_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1145_Wait_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
