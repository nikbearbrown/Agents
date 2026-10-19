# Configure influencer profile

This folder contains the **Configure influencer profile** workflow. Its executable nodes use `if`, `manualTrigger`, `openAi`, `scheduleTrigger`, `set`, `twitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`configure-influencer-profile.json`](configure-influencer-profile.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `twitterOAuth2Api`

**Entry nodes:** Schedule posting every 6 hours, Trigger posting manually

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Post tweet | `twitter` | Inspect parameters |
| Schedule posting every 6 hours | `scheduleTrigger` | Inspect parameters |
| Trigger posting manually | `manualTrigger` | Inspect parameters |
| Verify tweet constraints | `if` | Inspect parameters |
| Generate tweet content | `openAi` | Inspect parameters |
| Configure your influencer profile | `set` | Inspect parameters |

## Connection map

- Generate tweet content → Verify tweet constraints (`main`, output 0, input 0)
- Trigger posting manually → Configure your influencer profile (`main`, output 0, input 0)
- Verify tweet constraints → Configure your influencer profile (`main`, output 0, input 0)
- Verify tweet constraints → Post tweet (`main`, output 1, input 0)
- Schedule posting every 6 hours → Configure your influencer profile (`main`, output 0, input 0)
- Configure your influencer profile → Generate tweet content (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0439_Manual_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0439_Manual_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
