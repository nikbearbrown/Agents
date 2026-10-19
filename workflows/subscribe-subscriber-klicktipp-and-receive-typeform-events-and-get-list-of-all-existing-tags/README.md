# subscribe subscriber klicktipp and receive typeform events and get list of all existing tags

This folder contains the **subscribe subscriber klicktipp and receive typeform events and get list of all existing tags** workflow. Its executable nodes use `aggregate`, `if`, `klicktipp`, `merge`, `set`, `splitOut`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`subscribe-subscriber-klicktipp-and-receive-typeform-events-and-get-list-of-all-existing-tags.json`](subscribe-subscriber-klicktipp-and-receive-typeform-events-and-get-list-of-all-existing-tags.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `klickTippApi`, `typeformApi`

**Entry nodes:** New quiz sumbmission via Typeform

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Convert and set quiz data | `set` | Inspect parameters |
| Subscribe contact in KlickTipp | `klicktipp` | subscriber / subscribe |
| New quiz sumbmission via Typeform | `typeformTrigger` | Inspect parameters |
| Get list of all existing tags | `klicktipp` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Define Array of tags from Typeform | `set` | Inspect parameters |
| Split Out Typeform tags | `splitOut` | Inspect parameters |
| Tag creation check | `if` | Inspect parameters |
| Create the tag in KlickTipp | `klicktipp` | create |
| Aggregate tags to add to contact | `aggregate` | Inspect parameters |
| Tag contact directly in KlickTipp | `klicktipp` | contact-tagging |
| Aggregate array of created tags | `aggregate` | Inspect parameters |
| Tag contact KlickTipp after trag creation | `klicktipp` | contact-tagging |

## Connection map

- Merge → Tag creation check (`main`, output 0, input 0)
- Tag creation check → Aggregate tags to add to contact (`main`, output 0, input 0)
- Tag creation check → Create the tag in KlickTipp (`main`, output 1, input 0)
- Split Out Typeform tags → Merge (`main`, output 0, input 0)
- Convert and set quiz data → Subscribe contact in KlickTipp (`main`, output 0, input 0)
- Create the tag in KlickTipp → Aggregate array of created tags (`main`, output 0, input 0)
- Get list of all existing tags → Merge (`main`, output 0, input 1)
- Subscribe contact in KlickTipp → Define Array of tags from Typeform (`main`, output 0, input 0)
- Subscribe contact in KlickTipp → Get list of all existing tags (`main`, output 0, input 0)
- Aggregate array of created tags → Tag contact KlickTipp after trag creation (`main`, output 0, input 0)
- Aggregate tags to add to contact → Tag contact directly in KlickTipp (`main`, output 0, input 0)
- New quiz sumbmission via Typeform → Convert and set quiz data (`main`, output 0, input 0)
- Define Array of tags from Typeform → Split Out Typeform tags (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/0697_Aggregate_Typeform_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/0697_Aggregate_Typeform_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
