# clearbit and hubspot and update company hubspot

This folder contains the **clearbit and hubspot and update company hubspot** workflow. Its executable nodes use `calendlyTrigger`, `clearbit`, `filter`, `hubspot`, `if`, `noOp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clearbit-and-hubspot-and-update-company-hubspot.json`](clearbit-and-hubspot-and-update-company-hubspot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `calendlyApi`, `clearbitApi`, `hubspotOAuth2Api`

**Entry nodes:** Calendly Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| if company does not exist on CRM | `if` | Inspect parameters |
| Enrich company | `clearbit` | Inspect parameters |
| Create company | `hubspot` | company |
| Upsert contact | `hubspot` | Inspect parameters |
| Update company | `hubspot` | company / update |
| Contact not found, do nothing | `noOp` | Inspect parameters |
| Enrich email | `clearbit` | person |
| Filter out personal emails | `filter` | Inspect parameters |
| Search company | `hubspot` | company / searchByDomain |
| Upsert lead | `hubspot` | Inspect parameters |
| If person has a company | `if` | Inspect parameters |
| Calendly Trigger | `calendlyTrigger` | Inspect parameters |

## Connection map

- Enrich email → If person has a company (`main`, output 0, input 0)
- Enrich email → Contact not found, do nothing (`main`, output 1, input 0)
- Create company → Upsert contact (`main`, output 0, input 0)
- Enrich company → Search company (`main`, output 0, input 0)
- Search company → if company does not exist on CRM (`main`, output 0, input 0)
- Calendly Trigger → Filter out personal emails (`main`, output 0, input 0)
- If person has a company → Enrich company (`main`, output 0, input 0)
- If person has a company → Upsert lead (`main`, output 1, input 0)
- Filter out personal emails → Enrich email (`main`, output 0, input 0)
- if company does not exist on CRM → Create company (`main`, output 0, input 0)
- if company does not exist on CRM → Update company (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calendly/0430_Calendly_Filter_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calendly/0430_Calendly_Filter_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
