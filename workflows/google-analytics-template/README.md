# Google analytics template

This folder contains the **Google analytics template** workflow. Its executable nodes use `baserow`, `code`, `googleAnalytics`, `httpRequest`, `manualTrigger`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-analytics-template.json`](google-analytics-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleAnalyticsOAuth2`

**Entry nodes:** Schedule Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Page Engagement Stats for this week | `googleAnalytics` | Inspect parameters |
| Get Page Engagement Stats for prior week | `googleAnalytics` | Inspect parameters |
| Parse data from Google Analytics | `code` | Inspect parameters |
| Parse GA data | `code` | Inspect parameters |
| Get Google Search Results for this week | `googleAnalytics` | Inspect parameters |
| Get Google Search Results for last week | `googleAnalytics` | Inspect parameters |
| Parse Google Analytics Data | `code` | Inspect parameters |
| Parse Google Analytics Data1 | `code` | Inspect parameters |
| Get Country views data for this week | `googleAnalytics` | Inspect parameters |
| Get Country views data for last week | `googleAnalytics` | Inspect parameters |
| Parse Google analytics data | `code` | Inspect parameters |
| Parse Google analytics data1 | `code` | Inspect parameters |
| Send page data to A.I. | `httpRequest` | POST |
| Send page Search data to A.I. | `httpRequest` | POST |
| Send country view data to A.I. | `httpRequest` | POST |
| Save A.I. output to Baserow | `baserow` | create |

## Connection map

- Parse GA data → Get Google Search Results for this week (`main`, output 0, input 0)
- Schedule Trigger → Get Page Engagement Stats for this week (`main`, output 0, input 0)
- Send page data to A.I. → Send page Search data to A.I. (`main`, output 0, input 0)
- Parse Google Analytics Data → Get Google Search Results for last week (`main`, output 0, input 0)
- Parse Google analytics data → Get Country views data for last week (`main`, output 0, input 0)
- Parse Google Analytics Data1 → Get Country views data for this week (`main`, output 0, input 0)
- Parse Google analytics data1 → Send page data to A.I. (`main`, output 0, input 0)
- Send page Search data to A.I. → Send country view data to A.I. (`main`, output 0, input 0)
- Send country view data to A.I. → Save A.I. output to Baserow (`main`, output 0, input 0)
- Parse data from Google Analytics → Get Page Engagement Stats for prior week (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Page Engagement Stats for this week (`main`, output 0, input 0)
- Get Country views data for last week → Parse Google analytics data1 (`main`, output 0, input 0)
- Get Country views data for this week → Parse Google analytics data (`main`, output 0, input 0)
- Get Google Search Results for last week → Parse Google Analytics Data1 (`main`, output 0, input 0)
- Get Google Search Results for this week → Parse Google Analytics Data (`main`, output 0, input 0)
- Get Page Engagement Stats for this week → Parse data from Google Analytics (`main`, output 0, input 0)
- Get Page Engagement Stats for prior week → Parse GA data (`main`, output 0, input 0)

## Verification and provenance

Selected from 10 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleanalytics/1652_Googleanalytics_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleanalytics/1652_Googleanalytics_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
