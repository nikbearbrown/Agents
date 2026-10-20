# address validation

This folder contains the **address validation** workflow. Its executable nodes use `filter`, `httpRequest`, `if`, `set`, `splitOut`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`address-validation.json`](address-validation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| get order data | `httpRequest` | Inspect parameters |
| Split Out Order Data | `splitOut` | Inspect parameters |
| Set Address Fields | `set` | Inspect parameters |
| Check Address endereco api | `httpRequest` | POST |
| Split Out Corrected Address | `splitOut` | Inspect parameters |
| set new delivery address to billbee | `httpRequest` | PATCH |
| Wait | `wait` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| check if new address is not empty | `if` | Inspect parameters |
| set billbee tag | `httpRequest` | POST |
| check if housenumer is not empty | `if` | Inspect parameters |
| check if addressline 2 contains number | `if` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| set value of addressline2 as housenumber | `set` | Inspect parameters |
| Filter Out PickUpShops | `filter` | Inspect parameters |
| check if addressline 2 contains number and letter | `if` | Inspect parameters |
| set billbee tag manual check | `httpRequest` | POST |
| set value of addressline2 as housenumber number+letter | `set` | Inspect parameters |
| set billbee success | `httpRequest` | POST |
| ConfigNode | `set` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Wait → get order data (`main`, output 0, input 0)
- Wait1 → set new delivery address to billbee (`main`, output 0, input 0)
- Webhook → ConfigNode (`main`, output 0, input 0)
- ConfigNode → Wait (`main`, output 0, input 0)
- get order data → Split Out Order Data (`main`, output 0, input 0)
- Set Address Fields → Filter Out PickUpShops (`main`, output 0, input 0)
- Split Out Order Data → Set Address Fields (`main`, output 0, input 0)
- Filter Out PickUpShops → check if housenumer is not empty (`main`, output 0, input 0)
- Check Address endereco api → check if new address is not empty (`main`, output 0, input 0)
- Split Out Corrected Address → Wait1 (`main`, output 0, input 0)
- check if housenumer is not empty → Check Address endereco api (`main`, output 0, input 0)
- check if housenumer is not empty → check if addressline 2 contains number (`main`, output 1, input 0)
- check if new address is not empty → Split Out Corrected Address (`main`, output 0, input 0)
- check if new address is not empty → set billbee tag (`main`, output 1, input 0)
- set new delivery address to billbee → set billbee success (`main`, output 0, input 0)
- check if addressline 2 contains number → set value of addressline2 as housenumber (`main`, output 0, input 0)
- check if addressline 2 contains number → check if addressline 2 contains number and letter (`main`, output 1, input 0)
- set value of addressline2 as housenumber → Check Address endereco api (`main`, output 0, input 0)
- check if addressline 2 contains number and letter → set value of addressline2 as housenumber number+letter (`main`, output 0, input 0)
- check if addressline 2 contains number and letter → set billbee tag manual check (`main`, output 1, input 0)
- set value of addressline2 as housenumber number+letter → Check Address endereco api (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1727_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1727_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
