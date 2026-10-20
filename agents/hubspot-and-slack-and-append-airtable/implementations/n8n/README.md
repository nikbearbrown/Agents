# hubspot and slack and append airtable

This folder contains the **hubspot and slack and append airtable** workflow. Its executable nodes use `airtable`, `googleSlides`, `hubspot`, `hubspotTrigger`, `if`, `set`, `slack`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hubspot-and-slack-and-append-airtable.json`](hubspot-and-slack-and-append-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `googleSlidesOAuth2Api`, `hubspotApi`, `slackApi`

**Entry nodes:** Hubspot Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| IF | `if` | Inspect parameters |
| high-priority | `hubspot` | ticket |
| low-priority | `hubspot` | ticket |
| #closedwon | `slack` | Inspect parameters |
| Airtable | `airtable` | append |
| Google Slides | `googleSlides` | Inspect parameters |
| Hubspot Trigger | `hubspotTrigger` | Inspect parameters |
| Hubspot | `hubspot` | get |

## Connection map

- IF → high-priority (`main`, output 0, input 0)
- IF → low-priority (`main`, output 1, input 0)
- Set → Switch (`main`, output 0, input 0)
- Set → IF (`main`, output 0, input 0)
- Switch → #closedwon (`main`, output 0, input 0)
- Switch → Google Slides (`main`, output 1, input 0)
- Switch → Airtable (`main`, output 2, input 0)
- Hubspot → Set (`main`, output 0, input 0)
- Hubspot Trigger → Hubspot (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/0095_Googleslides_Slack_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/0095_Googleslides_Slack_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
