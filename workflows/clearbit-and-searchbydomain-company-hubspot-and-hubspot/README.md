# clearbit and searchbydomain company hubspot and hubspot

This folder contains the **clearbit and searchbydomain company hubspot and hubspot** workflow. Its executable nodes use `clearbit`, `convertKitTrigger`, `filter`, `hubspot`, `if`, `noOp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clearbit-and-searchbydomain-company-hubspot-and-hubspot.json`](clearbit-and-searchbydomain-company-hubspot-and-hubspot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** ConvertKit Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| if company does not exist on CRM | `if` | Inspect parameters |
| Enrich company | `clearbit` | Inspect parameters |
| Search company | `hubspot` | company / searchByDomain |
| Upsert lead | `hubspot` | Inspect parameters |
| Create company | `hubspot` | company |
| Upsert contact | `hubspot` | Inspect parameters |
| Update company | `hubspot` | company / update |
| ConvertKit Trigger | `convertKitTrigger` | Inspect parameters |
| Filter out personal emails1 | `filter` | Inspect parameters |
| Contact not found, do nothing1 | `noOp` | Inspect parameters |
| Enrich email | `clearbit` | person |
| If person has company | `if` | Inspect parameters |

## Connection map

- Enrich email → If person has company (`main`, output 0, input 0)
- Enrich email → Contact not found, do nothing1 (`main`, output 1, input 0)
- Create company → Upsert contact (`main`, output 0, input 0)
- Enrich company → Search company (`main`, output 0, input 0)
- Search company → if company does not exist on CRM (`main`, output 0, input 0)
- ConvertKit Trigger → Filter out personal emails1 (`main`, output 0, input 0)
- If person has company → Enrich company (`main`, output 0, input 0)
- If person has company → Upsert lead (`main`, output 1, input 0)
- Filter out personal emails1 → Enrich email (`main`, output 0, input 0)
- if company does not exist on CRM → Create company (`main`, output 0, input 0)
- if company does not exist on CRM → Update company (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0431_Filter_Convertkit_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0431_Filter_Convertkit_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
