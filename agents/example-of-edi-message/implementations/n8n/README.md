# Example of EDI Message

This folder contains the **Example of EDI Message** workflow. Its executable nodes use `code`, `gmail`, `gmailTrigger`, `googleSheets`, `if`, `merge`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`example-of-edi-message.json`](example-of-edi-message.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Email Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Order Information | `set` | Inspect parameters |
| Return Orders | `googleSheets` | append |
| Outbound Orders | `googleSheets` | append |
| Order Type | `if` | Inspect parameters |
| Email Trigger | `gmailTrigger` | Inspect parameters |
| Subject includes EDI | `if` | Inspect parameters |
| Extract Body | `set` | Inspect parameters |
| Get Email | `gmail` | get |
| Parse EDI Message | `code` | Inspect parameters |
| Order Info + Orderlines | `merge` | Inspect parameters |
| Flatten Data to Orderlines | `code` | Inspect parameters |
| Split Out by Line | `splitOut` | Inspect parameters |

## Connection map

- Get Email → Extract Body (`main`, output 0, input 0)
- Order Type → Return Orders (`main`, output 0, input 0)
- Order Type → Outbound Orders (`main`, output 1, input 0)
- Extract Body → Parse EDI Message (`main`, output 0, input 0)
- Email Trigger → Subject includes EDI (`main`, output 0, input 0)
- Order Information → Order Info + Orderlines (`main`, output 0, input 0)
- Parse EDI Message → Order Information (`main`, output 0, input 0)
- Parse EDI Message → Flatten Data to Orderlines (`main`, output 0, input 0)
- Split Out by Line → Order Info + Orderlines (`main`, output 0, input 1)
- Subject includes EDI → Get Email (`main`, output 0, input 0)
- Order Info + Orderlines → Order Type (`main`, output 0, input 0)
- Flatten Data to Orderlines → Split Out by Line (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0793_Splitout_Code_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0793_Splitout_Code_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
