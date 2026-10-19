# create strapi and every 30 minutes and search twitter

This folder contains the **create strapi and every 30 minutes and search twitter** workflow. Its executable nodes use `googleCloudNaturalLanguage`, `if`, `interval`, `merge`, `set`, `strapi`, `twitter`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-strapi-and-every-30-minutes-and-search-twitter.json`](create-strapi-and-every-30-minutes-and-search-twitter.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCloudNaturalLanguageOAuth2Api`, `strapiApi`, `twitterOAuth1Api`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Simplify Result | `set` | Inspect parameters |
| Store in Strapi | `strapi` | create |
| Every 30 Minutes | `interval` | Inspect parameters |
| Is Retweet or Old? | `if` | Inspect parameters |
| Search Tweets | `twitter` | search |
| Webhook | `webhook` | Inspect parameters |
| Simplify Webhook Result | `set` | Inspect parameters |
| Analyze Form Submission | `googleCloudNaturalLanguage` | Inspect parameters |
| Analyze Tweet | `googleCloudNaturalLanguage` | Inspect parameters |
| Merge Form Sentiment with Source | `merge` | Inspect parameters |
| Merge Tweet Sentiment with Source | `merge` | Inspect parameters |
| Positive Form Sentiment? | `if` | Inspect parameters |
| Store Form Submission in Strapi | `strapi` | create |
| Positive Tweet Sentiment? | `if` | Inspect parameters |

## Connection map

- Webhook → Simplify Webhook Result (`main`, output 0, input 0)
- Analyze Tweet → Merge Tweet Sentiment with Source (`main`, output 0, input 1)
- Search Tweets → Simplify Result (`main`, output 0, input 0)
- Simplify Result → Is Retweet or Old? (`main`, output 0, input 0)
- Every 30 Minutes → Search Tweets (`main`, output 0, input 0)
- Is Retweet or Old? → Analyze Tweet (`main`, output 1, input 0)
- Is Retweet or Old? → Merge Tweet Sentiment with Source (`main`, output 1, input 0)
- Analyze Form Submission → Merge Form Sentiment with Source (`main`, output 0, input 0)
- Simplify Webhook Result → Analyze Form Submission (`main`, output 0, input 0)
- Simplify Webhook Result → Merge Form Sentiment with Source (`main`, output 0, input 1)
- Positive Form Sentiment? → Store Form Submission in Strapi (`main`, output 0, input 0)
- Positive Tweet Sentiment? → Store in Strapi (`main`, output 0, input 0)
- Merge Form Sentiment with Source → Positive Form Sentiment? (`main`, output 0, input 0)
- Merge Tweet Sentiment with Source → Positive Tweet Sentiment? (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Strapi/1336_Strapi_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Strapi/1336_Strapi_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
