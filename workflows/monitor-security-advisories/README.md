# Monitor_security_advisories

This folder contains the **Monitor_security_advisories** workflow. Its executable nodes use `filter`, `gmail`, `if`, `jira`, `manualTrigger`, `n8nTrainingCustomerDatastore`, `noOp`, `rssFeedRead`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`monitor-security-advisories.json`](monitor-security-advisories.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `jiraSoftwareCloudApi`

**Entry nodes:** When clicking "Execute Workflow", Run workflow every 24 hours at 1am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Get Palo Alto security advisories | `rssFeedRead` | Inspect parameters |
| GlobalProtect advisory? | `filter` | Inspect parameters |
| Traps advisory? | `filter` | Inspect parameters |
| Create Jira issue | `jira` | Inspect parameters |
| Get customers | `n8nTrainingCustomerDatastore` | getAllPeople |
| Email customers | `gmail` | Inspect parameters |
| Extract info | `set` | Inspect parameters |
| Check if posted in last 24 hours | `if` | Inspect parameters |
| Ignore, stale advisory | `noOp` | Inspect parameters |
| Run workflow every 24 hours at 1am | `scheduleTrigger` | Inspect parameters |

## Connection map

- Extract info → Check if posted in last 24 hours (`main`, output 0, input 0)
- Get customers → Email customers (`main`, output 0, input 0)
- Traps advisory? → Get customers (`main`, output 0, input 0)
- Create Jira issue → Get customers (`main`, output 0, input 0)
- GlobalProtect advisory? → Create Jira issue (`main`, output 0, input 0)
- Check if posted in last 24 hours → GlobalProtect advisory? (`main`, output 0, input 0)
- Check if posted in last 24 hours → Traps advisory? (`main`, output 0, input 0)
- Check if posted in last 24 hours → Ignore, stale advisory (`main`, output 1, input 0)
- When clicking "Execute Workflow" → Get Palo Alto security advisories (`main`, output 0, input 0)
- Get Palo Alto security advisories → Extract info (`main`, output 0, input 0)
- Run workflow every 24 hours at 1am → Get Palo Alto security advisories (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1772_Filter_Rssfeedread_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1772_Filter_Rssfeedread_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
