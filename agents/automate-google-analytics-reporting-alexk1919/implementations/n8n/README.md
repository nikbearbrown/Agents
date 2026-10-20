# Automate Google Analytics Reporting - AlexK1919

This folder contains the **Automate Google Analytics Reporting - AlexK1919** workflow. Its executable nodes use `code`, `gmail`, `googleAnalytics`, `manualTrigger`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-google-analytics-reporting-alexk1919.json`](automate-google-analytics-reporting-alexk1919.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleAnalyticsOAuth2`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Page Engagement Stats for this week | `googleAnalytics` | Inspect parameters |
| Get Page Engagement Stats for prior week | `googleAnalytics` | Inspect parameters |
| Get Google Search Results for this week | `googleAnalytics` | Inspect parameters |
| Get Country views data for this week | `googleAnalytics` | Inspect parameters |
| Aggregate Data | `code` | Inspect parameters |
| Get Google Search Results for prior week | `googleAnalytics` | Inspect parameters |
| Get Country views data for prior week | `googleAnalytics` | Inspect parameters |
| Parse - Get Page Engagement This Week | `code` | Inspect parameters |
| Parse - Get Page Engagement Prior Week | `code` | Inspect parameters |
| Parse - Get Google Search This Week | `code` | Inspect parameters |
| Parse - Get Google Search Prior Week | `code` | Inspect parameters |
| Parse - Country Views This Week | `code` | Inspect parameters |
| Parse - Country Views Prior Week | `code` | Inspect parameters |
| Set urlStrings | `set` | Inspect parameters |
| Format Data | `code` | Inspect parameters |
| Input All | `code` | Inspect parameters |
| Email the Report | `gmail` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Input All → Format Data (`main`, output 0, input 0)
- Format Data → Email the Report (`main`, output 0, input 0)
- Aggregate Data → Input All (`main`, output 0, input 0)
- Set urlStrings → Aggregate Data (`main`, output 0, input 0)
- Parse - Country Views This Week → Get Country views data for prior week (`main`, output 0, input 0)
- Parse - Country Views Prior Week → Set urlStrings (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Page Engagement Stats for this week (`main`, output 0, input 0)
- Parse - Get Google Search This Week → Get Google Search Results for prior week (`main`, output 0, input 0)
- Get Country views data for this week → Parse - Country Views This Week (`main`, output 0, input 0)
- Parse - Get Google Search Prior Week → Get Country views data for this week (`main`, output 0, input 0)
- Get Country views data for prior week → Parse - Country Views Prior Week (`main`, output 0, input 0)
- Parse - Get Page Engagement This Week → Get Page Engagement Stats for prior week (`main`, output 0, input 0)
- Parse - Get Page Engagement Prior Week → Get Google Search Results for this week (`main`, output 0, input 0)
- Get Google Search Results for this week → Parse - Get Google Search This Week (`main`, output 0, input 0)
- Get Page Engagement Stats for this week → Parse - Get Page Engagement This Week (`main`, output 0, input 0)
- Get Google Search Results for prior week → Parse - Get Google Search Prior Week (`main`, output 0, input 0)
- Get Page Engagement Stats for prior week → Parse - Get Page Engagement Prior Week (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleanalytics/0475_Googleanalytics_Code_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleanalytics/0475_Googleanalytics_Code_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
