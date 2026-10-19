# My workflow 2

This folder contains the **My workflow 2** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `merge`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`authentication-set-up.json`](authentication-set-up.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Every 5 minutes start

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Token Request | `httpRequest` | POST |
| Assign Credentials | `set` | Inspect parameters |
| Dartagnan Project list | `httpRequest` | Inspect parameters |
| Create email template | `httpRequest` | POST |
| List Available Email Template Braze | `httpRequest` | Inspect parameters |
| Filtered Project Campaign | `httpRequest` | Inspect parameters |
| Filtering Dartagnan Campaigns | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Filtering Braze Email Template | `set` | Inspect parameters |
| Not existing In Braze | `merge` | Inspect parameters |
| Existing In Braze | `merge` | Inspect parameters |
| Dartagnan HTML & MEDIA To Update | `httpRequest` | Inspect parameters |
| Encode Content To Update | `set` | Inspect parameters |
| Dartagnan HTML & MEDIA Campagne to Create | `httpRequest` | Inspect parameters |
| Encode Content to Create | `set` | Inspect parameters |
| If campaign is modified recently | `if` | Inspect parameters |
| Filter Braze vs Dartagnan | `if` | Inspect parameters |
| Embed image in HTML | `code` | Inspect parameters |
| Embed image in HTML 1 | `code` | Inspect parameters |
| Every 5 minutes start | `scheduleTrigger` | Inspect parameters |
| Update existing email template in Braze | `httpRequest` | POST |

## Connection map

- Split Out → Filtering Braze Email Template (`main`, output 0, input 0)
- Token Request → Dartagnan Project list (`main`, output 0, input 0)
- Existing In Braze → If campaign is modified recently (`main`, output 0, input 0)
- Assign Credentials → List Available Email Template Braze (`main`, output 0, input 0)
- Assign Credentials → Token Request (`main`, output 0, input 0)
- Embed image in HTML → Encode Content To Update (`main`, output 0, input 0)
- Embed image in HTML 1 → Encode Content to Create (`main`, output 0, input 0)
- Every 5 minutes start → Assign Credentials (`main`, output 0, input 0)
- Not existing In Braze → Filter Braze vs Dartagnan (`main`, output 0, input 0)
- Dartagnan Project list → Filtered Project Campaign (`main`, output 0, input 0)
- Encode Content To Update → Update existing email template in Braze (`main`, output 0, input 0)
- Encode Content to Create → Create email template (`main`, output 0, input 0)
- Filter Braze vs Dartagnan → Dartagnan HTML & MEDIA Campagne to Create (`main`, output 0, input 0)
- Filtered Project Campaign → Filtering Dartagnan Campaigns (`main`, output 0, input 0)
- Filtering Dartagnan Campaigns → Existing In Braze (`main`, output 0, input 0)
- Filtering Dartagnan Campaigns → Not existing In Braze (`main`, output 0, input 0)
- Filtering Braze Email Template → Existing In Braze (`main`, output 0, input 1)
- Filtering Braze Email Template → Not existing In Braze (`main`, output 0, input 1)
- Dartagnan HTML & MEDIA To Update → Embed image in HTML (`main`, output 0, input 0)
- If campaign is modified recently → Dartagnan HTML & MEDIA To Update (`main`, output 0, input 0)
- List Available Email Template Braze → Split Out (`main`, output 0, input 0)
- Dartagnan HTML & MEDIA Campagne to Create → Embed image in HTML 1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0774_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0774_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
