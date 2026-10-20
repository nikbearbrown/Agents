# Email

This folder contains the **Email** workflow. Its executable nodes use `cortex`, `emailReadImap`, `if`, `theHive`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`email-read-imap-and-the-hive-and-promote-the-hive.json`](email-read-imap-and-the-hive-and-promote-the-hive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `cortexApi`, `imap`, `theHiveApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| IMAP Email | `emailReadImap` | Inspect parameters |
| TheHive | `theHive` | Inspect parameters |
| Create Case | `theHive` | promote |
| Case | `theHive` | case / get |
| Observable | `theHive` | observable |
| Analyzer Email | `theHive` | observable / executeAnalyzer |
| Cortex | `cortex` | job / report |
| IF | `if` | Inspect parameters |
| Update Case Domain | `theHive` | observable / create |
| Update Case Email | `theHive` | observable / create |
| Update Case Ip | `theHive` | observable / create |
| Wait | `wait` | Inspect parameters |
| Email Reputation | `theHive` | observable / executeAnalyzer |
| OTX IP | `theHive` | observable / executeAnalyzer |
| OTX DOMAIN | `theHive` | observable / executeAnalyzer |

## Connection map

- IF → Update Case Domain (`main`, output 0, input 0)
- IF → Update Case Email (`main`, output 0, input 0)
- IF → Update Case Ip (`main`, output 0, input 0)
- Case → Wait (`main`, output 0, input 0)
- Wait → Observable (`main`, output 0, input 0)
- Cortex → IF (`main`, output 0, input 0)
- TheHive → Create Case (`main`, output 0, input 0)
- IMAP Email → TheHive (`main`, output 0, input 0)
- Observable → Analyzer Email (`main`, output 0, input 0)
- Create Case → Case (`main`, output 0, input 0)
- Analyzer Email → Cortex (`main`, output 0, input 0)
- Update Case Ip → OTX IP (`main`, output 0, input 0)
- Update Case Email → Email Reputation (`main`, output 0, input 0)
- Update Case Domain → OTX DOMAIN (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Cortex/0972_Cortex_Emailreadimap_Send.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Cortex/0972_Cortex_Emailreadimap_Send.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
