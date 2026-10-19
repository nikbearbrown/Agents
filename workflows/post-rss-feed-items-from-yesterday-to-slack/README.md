# Post RSS feed items from yesterday to Slack

This folder contains the **Post RSS feed items from yesterday to Slack** workflow. Its executable nodes use `cron`, `dateTime`, `function`, `if`, `rssFeedRead`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`post-rss-feed-items-from-yesterday-to-slack.json`](post-rss-feed-items-from-yesterday-to-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`

**Entry nodes:** Every Morning

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Build our message | `function` | Inspect parameters |
| Every Morning | `cron` | Inspect parameters |
| Get Yesterdays Date | `dateTime` | subtract |
| Get the RSS Feed | `rssFeedRead` | Inspect parameters |
| If it was published after yesterday | `if` | Inspect parameters |
| Post to Slack | `slack` | Inspect parameters |

## Connection map

- Every Morning → Get Yesterdays Date (`main`, output 0, input 0)
- Get the RSS Feed → If it was published after yesterday (`main`, output 0, input 0)
- Build our message → Post to Slack (`main`, output 0, input 0)
- Get Yesterdays Date → Get the RSS Feed (`main`, output 0, input 0)
- If it was published after yesterday → Build our message (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1176_Rssfeedread_Slack_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1176_Rssfeedread_Slack_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
