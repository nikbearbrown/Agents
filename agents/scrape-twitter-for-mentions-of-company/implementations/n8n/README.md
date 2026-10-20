# Scrape Twitter for mentions of company

This folder contains the **Scrape Twitter for mentions of company** workflow. Its executable nodes use `cron`, `dateTime`, `if`, `set`, `slack`, `twitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-twitter-for-mentions-of-company.json`](scrape-twitter-for-mentions-of-company.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`, `twitterOAuth1Api`

**Entry nodes:** Run Every 10 Minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter Tweet Data | `set` | Inspect parameters |
| Run Every 10 Minutes | `cron` | Inspect parameters |
| Now - 10 minutes | `dateTime` | subtract |
| Get last 50 mentions | `twitter` | search |
| Created since last run? | `if` | Inspect parameters |
| Setup | `set` | Inspect parameters |
| Post to Slack | `slack` | Inspect parameters |

## Connection map

- Setup → Now - 10 minutes (`main`, output 0, input 0)
- Now - 10 minutes → Get last 50 mentions (`main`, output 0, input 0)
- Filter Tweet Data → Post to Slack (`main`, output 0, input 0)
- Get last 50 mentions → Created since last run? (`main`, output 0, input 0)
- Run Every 10 Minutes → Setup (`main`, output 0, input 0)
- Created since last run? → Filter Tweet Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Twitter/1212_Twitter_Slack_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Twitter/1212_Twitter_Slack_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
