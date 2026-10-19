# Parse DMARC reports

This folder contains the **Parse DMARC reports** workflow. Its executable nodes use `compression`, `dateTime`, `emailReadImap`, `emailSend`, `extractFromFile`, `if`, `mySql`, `renameKeys`, `set`, `slack`, `splitOut`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`parse-dmarc-reports.json`](parse-dmarc-reports.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `imap`, `mySql`, `slackOAuth2Api`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| End date format | `dateTime` | formatDate |
| If multiple records to parse | `if` | Inspect parameters |
| Map fields for DB input and parse | `set` | Inspect parameters |
| Begin format date | `dateTime` | formatDate |
| Input into database | `mySql` | Inspect parameters |
| If issue with DKIM or SPF | `if` | Inspect parameters |
| Rename Keys | `renameKeys` | Inspect parameters |
| Rename column for consistency | `set` | Inspect parameters |
| Unzip File | `compression` | Inspect parameters |
| Extract XML data | `extractFromFile` | xml |
| Parse XML data to JSON | `xml` | Inspect parameters |
| Split Out For Separate Entries | `splitOut` | Inspect parameters |
| Slack Post Message On Channel | `slack` | Inspect parameters |
| Send Error Notification Email | `emailSend` | Inspect parameters |

## Connection map

- Unzip File → Extract XML data (`main`, output 0, input 0)
- Rename Keys → Map fields for DB input and parse (`main`, output 0, input 0)
- End date format → Input into database (`main`, output 0, input 0)
- End date format → If issue with DKIM or SPF (`main`, output 0, input 0)
- Extract XML data → Parse XML data to JSON (`main`, output 0, input 0)
- Begin format date → End date format (`main`, output 0, input 0)
- Email Trigger (IMAP) → Unzip File (`main`, output 0, input 0)
- Parse XML data to JSON → If multiple records to parse (`main`, output 0, input 0)
- If issue with DKIM or SPF → Slack Post Message On Channel (`main`, output 0, input 0)
- If issue with DKIM or SPF → Send Error Notification Email (`main`, output 0, input 0)
- If multiple records to parse → Split Out For Separate Entries (`main`, output 0, input 0)
- If multiple records to parse → Rename column for consistency (`main`, output 1, input 0)
- Rename column for consistency → Map fields for DB input and parse (`main`, output 0, input 0)
- Split Out For Separate Entries → Rename Keys (`main`, output 0, input 0)
- Map fields for DB input and parse → Begin format date (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1296_Datetime_Splitout_Process.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1296_Datetime_Splitout_Process.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
