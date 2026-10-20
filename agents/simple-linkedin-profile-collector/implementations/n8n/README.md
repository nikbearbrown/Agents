# Simple LinkedIn profile collector

This folder contains the **Simple LinkedIn profile collector** workflow. Its executable nodes use `convertToFile`, `httpRequest`, `manualTrigger`, `merge`, `nocoDb`, `openAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`simple-linkedin-profile-collector.json`](simple-linkedin-profile-collector.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `nocoDbApiToken`, `openAiApi`, `serpApi`

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Google search w/ SerpAPI | `httpRequest` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Discard meta data | `set` | Inspect parameters |
| LinkedIn profiles in Excel for download | `convertToFile` | xlsx |
| Search parameter | `set` | Inspect parameters |
| Turn search results into individual items | `splitOut` | Inspect parameters |
| Company name & followers | `openAi` | Inspect parameters |
| Generate final data via merge | `merge` | Inspect parameters |
| Store data in a NocoDB table | `nocoDb` | create |

## Connection map

- Edit Fields → Company name & followers (`main`, output 0, input 0)
- Edit Fields → Generate final data via merge (`main`, output 0, input 1)
- Manual Trigger → Search parameter (`main`, output 0, input 0)
- Search parameter → Google search w/ SerpAPI (`main`, output 0, input 0)
- Discard meta data → Generate final data via merge (`main`, output 0, input 0)
- Company name & followers → Discard meta data (`main`, output 0, input 0)
- Google search w/ SerpAPI → Turn search results into individual items (`main`, output 0, input 0)
- Generate final data via merge → LinkedIn profiles in Excel for download (`main`, output 0, input 0)
- Generate final data via merge → Store data in a NocoDB table (`main`, output 0, input 0)
- Turn search results into individual items → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1742_Splitout_Nocodb_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1742_Splitout_Nocodb_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
