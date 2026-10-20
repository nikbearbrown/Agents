# Receive an alert when new breaches are added to haveibeenpwned.com

This folder contains the **Receive an alert when new breaches are added to haveibeenpwned.com** workflow. Its executable nodes use `convertToFile`, `extractFromFile`, `httpRequest`, `if`, `manualTrigger`, `merge`, `noOp`, `readWriteFile`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-an-alert-when-new-breaches-are-added-to-haveibeenpwned-com.json`](receive-an-alert-when-new-breaches-are-added-to-haveibeenpwned-com.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Convert to File | `convertToFile` | toJson |
| Split Out | `splitOut` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Request breaches | `httpRequest` | Inspect parameters |
| Read last breach | `readWriteFile` | Inspect parameters |
| Get JSON from file | `extractFromFile` | fromJson |
| Check for content | `if` | Inspect parameters |
| Set to none | `set` | Inspect parameters |
| If - check for new | `if` | Inspect parameters |
| Set breach name | `set` | Inspect parameters |
| Write breach name to file | `readWriteFile` | write |
| New breach | `noOp` | Inspect parameters |
| Old breach | `noOp` | Inspect parameters |
| Set empty json | `set` | Inspect parameters |
| Write cache.json | `readWriteFile` | write |
| Convert json to file | `convertToFile` | toJson |
| Add information about the last breach we alerted | `merge` | Inspect parameters |

## Connection map

- Split Out → Check for content (`main`, output 0, input 0)
- Set to none → Add information about the last breach we alerted (`main`, output 0, input 1)
- Set empty json → Convert json to file (`main`, output 0, input 0)
- Convert to File → Write breach name to file (`main`, output 0, input 0)
- Set breach name → Convert to File (`main`, output 0, input 0)
- Read last breach → Get JSON from file (`main`, output 0, input 0)
- Request breaches → Read last breach (`main`, output 0, input 0)
- Request breaches → Add information about the last breach we alerted (`main`, output 0, input 0)
- Schedule Trigger → Request breaches (`main`, output 0, input 0)
- Check for content → Add information about the last breach we alerted (`main`, output 0, input 1)
- Check for content → Set to none (`main`, output 1, input 0)
- Get JSON from file → Split Out (`main`, output 0, input 0)
- If - check for new → Set breach name (`main`, output 0, input 0)
- If - check for new → New breach (`main`, output 0, input 0)
- If - check for new → Old breach (`main`, output 1, input 0)
- Convert json to file → Write cache.json (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set empty json (`main`, output 0, input 0)
- Add information about the last breach we alerted → If - check for new (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0790_Splitout_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0790_Splitout_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
