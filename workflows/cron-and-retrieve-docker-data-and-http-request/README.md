# Dashboard

This folder contains the **Dashboard** workflow. Its executable nodes use `cron`, `function`, `github`, `httpRequest`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`cron-and-retrieve-docker-data-and-http-request.json`](cron-and-retrieve-docker-data-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Cron | `cron` | Inspect parameters |
| Dashboard Configuration | `set` | Inspect parameters |
| Retrieve Docker Data | `httpRequest` | Inspect parameters |
| Docker Pulls | `httpRequest` | Inspect parameters |
| Docker Stars | `httpRequest` | Inspect parameters |
| Retrieve npm Data | `httpRequest` | Inspect parameters |
| GitHub Watchers | `httpRequest` | Inspect parameters |
| GitHub Forks | `httpRequest` | Inspect parameters |
| GitHub Open Issues  | `httpRequest` | Inspect parameters |
| GitHub Stars | `httpRequest` | Inspect parameters |
| npm Maintenance | `httpRequest` | Inspect parameters |
| npm Popularity | `httpRequest` | Inspect parameters |
| npm Quality | `httpRequest` | Inspect parameters |
| npm Final | `httpRequest` | Inspect parameters |
| Product Hunt Rating | `httpRequest` | Inspect parameters |
| Product Hunt Reviews | `httpRequest` | Inspect parameters |
| Product Hunt Votes | `httpRequest` | Inspect parameters |
| Product Hunt Comments | `httpRequest` | Inspect parameters |
| GitHub | `github` | repository / get |
| Retrieve Product Hunt Data | `httpRequest` | Inspect parameters |
| Massage npm Data | `function` | Inspect parameters |
| Massage Product Hunt Data | `function` | Inspect parameters |
| Massage Docker Data | `function` | Inspect parameters |
| Massage GitHub Data | `function` | Inspect parameters |

## Connection map

- Cron → Dashboard Configuration (`main`, output 0, input 0)
- GitHub → Massage GitHub Data (`main`, output 0, input 0)
- Massage npm Data → npm Maintenance (`main`, output 0, input 0)
- Massage npm Data → npm Quality (`main`, output 0, input 0)
- Massage npm Data → npm Popularity (`main`, output 0, input 0)
- Massage npm Data → npm Final (`main`, output 0, input 0)
- Retrieve npm Data → Massage npm Data (`main`, output 0, input 0)
- Massage Docker Data → Docker Stars (`main`, output 0, input 0)
- Massage Docker Data → Docker Pulls (`main`, output 0, input 0)
- Massage GitHub Data → GitHub Stars (`main`, output 0, input 0)
- Massage GitHub Data → GitHub Watchers (`main`, output 0, input 0)
- Massage GitHub Data → GitHub Forks (`main`, output 0, input 0)
- Massage GitHub Data → GitHub Open Issues  (`main`, output 0, input 0)
- Retrieve Docker Data → Massage Docker Data (`main`, output 0, input 0)
- Dashboard Configuration → Retrieve Product Hunt Data (`main`, output 0, input 0)
- Dashboard Configuration → Retrieve npm Data (`main`, output 0, input 0)
- Dashboard Configuration → Retrieve Docker Data (`main`, output 0, input 0)
- Dashboard Configuration → GitHub (`main`, output 0, input 0)
- Massage Product Hunt Data → Product Hunt Rating (`main`, output 0, input 0)
- Massage Product Hunt Data → Product Hunt Reviews (`main`, output 0, input 0)
- Massage Product Hunt Data → Product Hunt Votes (`main`, output 0, input 0)
- Massage Product Hunt Data → Product Hunt Comments (`main`, output 0, input 0)
- Retrieve Product Hunt Data → Massage Product Hunt Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1107_HTTP_GitHub_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1107_HTTP_GitHub_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
