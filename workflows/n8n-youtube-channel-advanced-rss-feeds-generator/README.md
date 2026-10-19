# [n8n] YouTube Channel Advanced RSS Feeds Generator

This folder contains the **[n8n] YouTube Channel Advanced RSS Feeds Generator** workflow. Its executable nodes use `aggregate`, `code`, `formTrigger`, `httpRequest`, `merge`, `respondToWebhook`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-youtube-channel-advanced-rss-feeds-generator.json`](n8n-youtube-channel-advanced-rss-feeds-generator.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Get Channel ID | `httpRequest` | Inspect parameters |
| Set XML URL | `set` | Inspect parameters |
| Set Channel Username | `set` | Inspect parameters |
| Set XML Feed URL | `set` | Inspect parameters |
| Set Video ID | `set` | Inspect parameters |
| Get Video ID Channel ID | `httpRequest` | Inspect parameters |
| Set XML Feed | `set` | Inspect parameters |
| Get Temporary Token | `httpRequest` | Inspect parameters |
| GTT | `httpRequest` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Youtube Channel Videos RSS Formats | `set` | Inspect parameters |
| Youtube Channel Community RSS Formats | `set` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Validation Code | `code` | Inspect parameters |
| Format response as HTML Table | `code` | Inspect parameters |
| Merga Data of Youtube & Community RSS | `merge` | Inspect parameters |

## Connection map

- GTT → Set Video ID (`main`, output 0, input 0)
- Switch → Get Temporary Token (`main`, output 0, input 0)
- Switch → Set XML Feed URL (`main`, output 1, input 0)
- Switch → GTT (`main`, output 2, input 0)
- Aggregate → Youtube Channel Community RSS Formats (`main`, output 0, input 0)
- Aggregate → Youtube Channel Videos RSS Formats (`main`, output 0, input 0)
- Set XML URL → Aggregate (`main`, output 0, input 0)
- Set Video ID → Get Video ID Channel ID (`main`, output 0, input 0)
- Set XML Feed → Aggregate (`main`, output 0, input 0)
- Get Channel ID → Set XML URL (`main`, output 0, input 0)
- Validation Code → Switch (`main`, output 0, input 0)
- Set XML Feed URL → Aggregate (`main`, output 0, input 0)
- n8n Form Trigger → Validation Code (`main`, output 0, input 0)
- Get Temporary Token → Set Channel Username (`main`, output 0, input 0)
- Set Channel Username → Get Channel ID (`main`, output 0, input 0)
- Get Video ID Channel ID → Set XML Feed (`main`, output 0, input 0)
- Format response as HTML Table → Respond to Webhook (`main`, output 0, input 0)
- Youtube Channel Videos RSS Formats → Merga Data of Youtube & Community RSS (`main`, output 0, input 1)
- Merga Data of Youtube & Community RSS → Format response as HTML Table (`main`, output 0, input 0)
- Youtube Channel Community RSS Formats → Merga Data of Youtube & Community RSS (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0482_Code_Respondtowebhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0482_Code_Respondtowebhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
