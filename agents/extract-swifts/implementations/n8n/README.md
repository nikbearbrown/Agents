# extract_swifts

This folder contains the **extract_swifts** workflow. Its executable nodes use `executeCommand`, `function`, `functionItem`, `htmlExtract`, `httpRequest`, `if`, `manualTrigger`, `mongoDb`, `readBinaryFile`, `set`, `splitInBatches`, `uproc`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-swifts.json`](extract-swifts.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mongoDb`, `uprocApi`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| HTML Extract | `htmlExtract` | Inspect parameters |
| SplitInBatches | `splitInBatches` | Inspect parameters |
| HTTP Request1 | `httpRequest` | Inspect parameters |
| HTML Extract1 | `htmlExtract` | Inspect parameters |
| MongoDB1 | `mongoDb` | insert |
| uProc | `uproc` | Inspect parameters |
| Prepare Documents | `function` | Inspect parameters |
| More Countries | `if` | Inspect parameters |
| Set Page to Scrape | `functionItem` | Inspect parameters |
| More Pages | `if` | Inspect parameters |
| Set More Pages | `function` | Inspect parameters |
| Set | `set` | Inspect parameters |
| Generate filename | `functionItem` | Inspect parameters |
| Read Binary File | `readBinaryFile` | Inspect parameters |
| File exists? | `if` | Inspect parameters |
| Write Binary File | `writeBinaryFile` | Inspect parameters |
| Read Binary File1 | `readBinaryFile` | Inspect parameters |
| Wait | `function` | Inspect parameters |
| Prepare countries | `function` | Inspect parameters |
| Create Directory | `executeCommand` | Inspect parameters |
| MongoDB | `mongoDb` | Inspect parameters |

## Connection map

- Set → Generate filename (`main`, output 0, input 0)
- Wait → HTTP Request1 (`main`, output 0, input 0)
- uProc → Set Page to Scrape (`main`, output 0, input 0)
- MongoDB1 → Set More Pages (`main`, output 0, input 0)
- More Pages → Set Page to Scrape (`main`, output 0, input 0)
- More Pages → More Countries (`main`, output 1, input 0)
- File exists? → Read Binary File1 (`main`, output 0, input 0)
- File exists? → Wait (`main`, output 1, input 0)
- HTML Extract → Prepare countries (`main`, output 0, input 0)
- HTTP Request → HTML Extract (`main`, output 0, input 0)
- HTML Extract1 → Prepare Documents (`main`, output 0, input 0)
- HTTP Request1 → Write Binary File (`main`, output 0, input 0)
- More Countries → SplitInBatches (`main`, output 1, input 0)
- Set More Pages → More Pages (`main`, output 0, input 0)
- SplitInBatches → uProc (`main`, output 0, input 0)
- Create Directory → HTTP Request (`main`, output 0, input 0)
- Read Binary File → File exists? (`main`, output 0, input 0)
- Generate filename → Read Binary File (`main`, output 0, input 0)
- Prepare Documents → MongoDB1 (`main`, output 0, input 0)
- Prepare countries → SplitInBatches (`main`, output 0, input 0)
- Read Binary File1 → HTML Extract1 (`main`, output 0, input 0)
- Write Binary File → Read Binary File1 (`main`, output 0, input 0)
- Set Page to Scrape → Set (`main`, output 0, input 0)
- On clicking 'execute' → Create Directory (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0178_Functionitem_Executecommand_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0178_Functionitem_Executecommand_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
