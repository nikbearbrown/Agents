# fetch manifest digest and remove old tags and retrieve image tags

This folder contains the **fetch manifest digest and remove old tags and retrieve image tags** workflow. Its executable nodes use `code`, `emailSend`, `filter`, `httpRequest`, `scheduleTrigger`, `set`, `sort`, `splitOut`, `ssh`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-manifest-digest-and-remove-old-tags-and-retrieve-image-tags.json`](fetch-manifest-digest-and-remove-old-tags-and-retrieve-image-tags.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Scheduled Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Fetch Manifest Digest | `httpRequest` | Inspect parameters |
| Remove Old Tags | `httpRequest` | Inspect parameters |
| Retrieve Image Tags | `httpRequest` | Inspect parameters |
| List Images | `httpRequest` | Inspect parameters |
| Extract Image Names | `code` | Inspect parameters |
| Identify Tags to Remove | `code` | Inspect parameters |
| Scheduled Trigger | `scheduleTrigger` | Inspect parameters |
| Send Notification Email | `emailSend` | Inspect parameters |
| Split Tags | `splitOut` | Inspect parameters |
| Filter Valid Tags | `filter` | Inspect parameters |
| Fetch Manifest Digest for Blob | `httpRequest` | Inspect parameters |
| Update Fields | `set` | Inspect parameters |
| Group Tags by Image | `code` | Inspect parameters |
| Sort by Creation Date | `sort` | Inspect parameters |
| Send Failure Notification Email | `emailSend` | Inspect parameters |
| Execute Garbage Collection | `ssh` | Inspect parameters |

## Connection map

- Split Tags → Filter Valid Tags (`main`, output 0, input 0)
- List Images → Extract Image Names (`main`, output 0, input 0)
- Update Fields → Sort by Creation Date (`main`, output 0, input 0)
- Remove Old Tags → Execute Garbage Collection (`main`, output 0, input 0)
- Remove Old Tags → Send Failure Notification Email (`main`, output 1, input 0)
- Filter Valid Tags → Fetch Manifest Digest (`main`, output 0, input 0)
- Scheduled Trigger → List Images (`main`, output 0, input 0)
- Extract Image Names → Retrieve Image Tags (`main`, output 0, input 0)
- Group Tags by Image → Identify Tags to Remove (`main`, output 0, input 0)
- Retrieve Image Tags → Split Tags (`main`, output 0, input 0)
- Fetch Manifest Digest → Fetch Manifest Digest for Blob (`main`, output 0, input 0)
- Sort by Creation Date → Group Tags by Image (`main`, output 0, input 0)
- Identify Tags to Remove → Remove Old Tags (`main`, output 0, input 0)
- Identify Tags to Remove → Send Notification Email (`main`, output 0, input 0)
- Fetch Manifest Digest for Blob → Update Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0712_Splitout_Code_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0712_Splitout_Code_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
