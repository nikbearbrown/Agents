# Enrich new Discourse members then notify in Slack for high value leads

This folder contains the **Enrich new Discourse members then notify in Slack for high value leads** workflow. Its executable nodes use `clearbit`, `filter`, `noOp`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`enrich-new-discourse-members-then-notify-in-slack-for-high-value-leads.json`](enrich-new-discourse-members-then-notify-in-slack-for-high-value-leads.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clearbitApi`, `slackApi`

**Entry nodes:** On new Discourse user

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter out common personal emails | `filter` | Inspect parameters |
| No clearbit enrichment available | `noOp` | Inspect parameters |
| Enrich user with Clearbit | `clearbit` | person |
| Get company info | `clearbit` | Inspect parameters |
| Filter for high value leads | `filter` | Inspect parameters |
| On new Discourse user | `webhook` | Inspect parameters |
| Post message in Channel | `slack` | Inspect parameters |

## Connection map

- Get company info → Filter for high value leads (`main`, output 0, input 0)
- On new Discourse user → Filter out common personal emails (`main`, output 0, input 0)
- Enrich user with Clearbit → Get company info (`main`, output 0, input 0)
- Enrich user with Clearbit → No clearbit enrichment available (`main`, output 1, input 0)
- Filter for high value leads → Post message in Channel (`main`, output 0, input 0)
- Filter out common personal emails → Enrich user with Clearbit (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0414_Webhook_Filter_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0414_Webhook_Filter_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
