# Namesilo Bulk Domain Availability [Template]

This folder contains the **Namesilo Bulk Domain Availability [Template]** workflow. Its executable nodes use `code`, `convertToFile`, `httpRequest`, `manualTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`namesilo-bulk-domain-availability-template.json`](namesilo-bulk-domain-availability-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Start

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set Data | `set` | Inspect parameters |
| Convert & Split Domains | `code` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Merge Results | `code` | Inspect parameters |
| Loop Over Domains | `splitInBatches` | Inspect parameters |
| Namesilo Requests | `httpRequest` | Inspect parameters |
| Parse Data | `code` | Inspect parameters |
| Convert to Excel | `convertToFile` | xlsx |
| Start | `manualTrigger` | Inspect parameters |

## Connection map

- Wait → Loop Over Domains (`main`, output 0, input 0)
- Start → Set Data (`main`, output 0, input 0)
- Set Data → Convert & Split Domains (`main`, output 0, input 0)
- Parse Data → Wait (`main`, output 0, input 0)
- Merge Results → Convert to Excel (`main`, output 0, input 0)
- Loop Over Domains → Merge Results (`main`, output 0, input 0)
- Loop Over Domains → Namesilo Requests (`main`, output 1, input 0)
- Namesilo Requests → Parse Data (`main`, output 0, input 0)
- Convert & Split Domains → Loop Over Domains (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1954_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1954_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
