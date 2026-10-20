# subscribe subscriber klicktipp and split out guest bookings and split out guest cancellations

This folder contains the **subscribe subscriber klicktipp and split out guest bookings and split out guest cancellations** workflow. Its executable nodes use `calendlyTrigger`, `if`, `klicktipp`, `noOp`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`subscribe-subscriber-klicktipp-and-split-out-guest-bookings-and-split-out-guest-cancellations.json`](subscribe-subscriber-klicktipp-and-split-out-guest-bookings-and-split-out-guest-cancellations.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `calendlyApi`, `klickTippApi`

**Entry nodes:** New Calendly event

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Subscribe invitee booking in KlickTipp | `klicktipp` | subscriber / subscribe |
| Subscribe guest booking in KlickTipp | `klicktipp` | subscriber / subscribe |
| Subscribe guest cancellation in KlickTipp | `klicktipp` | subscriber / subscribe |
| Subscribe invitee cancellation in KlickTipp | `klicktipp` | subscriber / subscribe |
| Split Out guest bookings | `splitOut` | Inspect parameters |
| Split Out guest cancellations | `splitOut` | Inspect parameters |
| Guests booking check | `if` | Inspect parameters |
| Subscribe invitee to empty guest addresses field | `klicktipp` | subscriber / subscribe |
| New Calendly event | `calendlyTrigger` | Inspect parameters |
| Convert data for KlickTipp | `set` | Inspect parameters |
| Check event - booking or cancellation? | `if` | Inspect parameters |
| List guests for booking | `set` | Inspect parameters |
| List guests for cancellation | `set` | Inspect parameters |
| Guests cancellation check | `if` | Inspect parameters |
| Rescheduling check | `if` | Inspect parameters |
| Invitee did not add guests to the booking | `noOp` | Inspect parameters |
| Event was rescheduled | `noOp` | Inspect parameters |
| No guest email addresses found | `noOp` | Inspect parameters |

## Connection map

- New Calendly event → Convert data for KlickTipp (`main`, output 0, input 0)
- Rescheduling check → Event was rescheduled (`main`, output 0, input 0)
- Rescheduling check → Subscribe invitee to empty guest addresses field (`main`, output 1, input 0)
- Guests booking check → List guests for booking (`main`, output 0, input 0)
- Guests booking check → Invitee did not add guests to the booking (`main`, output 1, input 0)
- List guests for booking → Split Out guest bookings (`main`, output 0, input 0)
- Split Out guest bookings → Subscribe guest booking in KlickTipp (`main`, output 0, input 0)
- Guests cancellation check → List guests for cancellation (`main`, output 0, input 0)
- Guests cancellation check → No guest email addresses found (`main`, output 1, input 0)
- Convert data for KlickTipp → Check event - booking or cancellation? (`main`, output 0, input 0)
- List guests for cancellation → Split Out guest cancellations (`main`, output 0, input 0)
- Split Out guest cancellations → Subscribe guest cancellation in KlickTipp (`main`, output 0, input 0)
- Check event - booking or cancellation? → Subscribe invitee booking in KlickTipp (`main`, output 0, input 0)
- Check event - booking or cancellation? → Subscribe invitee cancellation in KlickTipp (`main`, output 1, input 0)
- Subscribe invitee booking in KlickTipp → Guests booking check (`main`, output 0, input 0)
- Subscribe guest cancellation in KlickTipp → Rescheduling check (`main`, output 0, input 0)
- Subscribe invitee cancellation in KlickTipp → Guests cancellation check (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calendly/0660_Calendly_Noop_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Calendly/0660_Calendly_Noop_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
