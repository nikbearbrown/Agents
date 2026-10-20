# If time available Respond

This folder contains the **If time available Respond** workflow. Its executable nodes use `airtable`, `code`, `googleCalendar`, `if`, `itemLists`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`if-time-available-respond.json`](if-time-available-respond.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Getslot_tool, bookslots_tool, Updateslots_tool, CancelSlots_tool, call_results

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Input Arguments | `set` | Inspect parameters |
| Format response | `itemLists` | concatenateItems |
| Sort | `itemLists` | sort |
| Available Start Times & Ranges | `code` | Inspect parameters |
| Flatten Slots | `code` | Inspect parameters |
| Enrich Date | `code` | Inspect parameters |
| Build Response Payload | `set` | Inspect parameters |
| Booking Payload | `set` | Inspect parameters |
| Success Response | `set` | Inspect parameters |
| Add Friendly Error | `code` | Inspect parameters |
| Error Response | `set` | Inspect parameters |
| Escape Json | `code` | Inspect parameters |
| Has all information | `if` | Inspect parameters |
| Respond with Error | `respondToWebhook` | Inspect parameters |
| Build Error Response Payload | `set` | Inspect parameters |
| Build Error Response Payload2 | `set` | Inspect parameters |
| Getslot_tool | `webhook` | Inspect parameters |
| Check Availability | `googleCalendar` | calendar |
| Response | `respondToWebhook` | Inspect parameters |
| Check if time is available or not | `if` | Inspect parameters |
| Time available (true) & Call_id | `set` | Inspect parameters |
| Get All Calendar Events | `googleCalendar` | getAll |
| Extract start, end and name | `set` | Inspect parameters |
| Convert into Json format for Vapi | `code` | Inspect parameters |
| Response to Vapi | `respondToWebhook` | Inspect parameters |
| bookslots_tool | `webhook` | Inspect parameters |
| Input Arguments from booking tools | `set` | Inspect parameters |
| Convert time to CST America / Chicago | `code` | Inspect parameters |
| Create Event | `googleCalendar` | Inspect parameters |
| Respond to Vapi | `respondToWebhook` | Inspect parameters |
| If the booking is confirmed then true | `if` | Inspect parameters |
| Information to be Saved in Airtable | `set` | Inspect parameters |
| Logs the confirmed booking details | `airtable` | create |
| Updateslots_tool | `webhook` | Inspect parameters |
| Input Arguments from updateslot tool | `set` | Inspect parameters |
| Checks if required info is provided. | `if` | Inspect parameters |
| Finds original appointment | `airtable` | search |
| Response with Error | `respondToWebhook` | Inspect parameters |
| Update Event | `googleCalendar` | update |
| Updates Airtable record | `airtable` | update |
| Response & call_id | `set` | Inspect parameters |
| Respond to Vapi about Updating slots | `respondToWebhook` | Inspect parameters |
| CancelSlots_tool | `webhook` | Inspect parameters |
| Input Arguments from cancelslot tool | `set` | Inspect parameters |
| Checks if required info is provided for cancelation | `if` | Inspect parameters |
| Finds the appointment record | `airtable` | search |
| Build Error Response | `set` | Inspect parameters |
| Respond with Error to Vapi | `respondToWebhook` | Inspect parameters |
| Delete Event | `googleCalendar` | delete |
| Update Airtable record | `airtable` | update |
| Call_id & Response | `set` | Inspect parameters |
| Respond to Vapi about cancelation | `respondToWebhook` | Inspect parameters |
| call_results | `webhook` | Inspect parameters |
| All Input Arguments | `set` | Inspect parameters |
| Save all information | `airtable` | upsert |

## Connection map

- Sort → Format response (`main`, output 0, input 0)
- Enrich Date → Build Response Payload (`main`, output 0, input 0)
- Escape Json → Convert time to CST America / Chicago (`main`, output 0, input 0)
- Create Event → Booking Payload (`main`, output 0, input 0)
- Create Event → Add Friendly Error (`main`, output 1, input 0)
- Delete Event → Update Airtable record (`main`, output 0, input 0)
- Delete Event → Call_id & Response (`main`, output 1, input 0)
- Getslot_tool → Input Arguments (`main`, output 0, input 0)
- Update Event → Updates Airtable record (`main`, output 0, input 0)
- Update Event → Response & call_id (`main`, output 1, input 0)
- call_results → All Input Arguments (`main`, output 0, input 0)
- Flatten Slots → Enrich Date (`main`, output 0, input 0)
- Error Response → Respond to Vapi (`main`, output 0, input 0)
- bookslots_tool → Input Arguments from booking tools (`main`, output 0, input 0)
- Booking Payload → Success Response (`main`, output 0, input 0)
- Format response → Available Start Times & Ranges (`main`, output 0, input 0)
- Input Arguments → Check Availability (`main`, output 0, input 0)
- Respond to Vapi → If the booking is confirmed then true (`main`, output 0, input 0)
- CancelSlots_tool → Input Arguments from cancelslot tool (`main`, output 0, input 0)
- Success Response → Respond to Vapi (`main`, output 0, input 0)
- Updateslots_tool → Input Arguments from updateslot tool (`main`, output 0, input 0)
- Add Friendly Error → Error Response (`main`, output 0, input 0)
- Call_id & Response → Respond to Vapi about cancelation (`main`, output 0, input 0)
- Check Availability → Check if time is available or not (`main`, output 0, input 0)
- Response & call_id → Respond to Vapi about Updating slots (`main`, output 0, input 0)
- All Input Arguments → Save all information (`main`, output 0, input 0)
- Has all information → Escape Json (`main`, output 0, input 0)
- Has all information → Build Error Response Payload (`main`, output 1, input 0)
- Build Error Response → Respond with Error to Vapi (`main`, output 0, input 0)
- Build Response Payload → Convert into Json format for Vapi (`main`, output 0, input 0)
- Update Airtable record → Call_id & Response (`main`, output 0, input 0)
- Get All Calendar Events → Extract start, end and name (`main`, output 0, input 0)
- Updates Airtable record → Response & call_id (`main`, output 0, input 0)
- Finds original appointment → Update Event (`main`, output 0, input 0)
- Extract start, end and name → Sort (`main`, output 0, input 0)
- Build Error Response Payload → Respond with Error (`main`, output 0, input 0)
- Finds the appointment record → Delete Event (`main`, output 0, input 0)
- Build Error Response Payload2 → Response with Error (`main`, output 0, input 0)
- Available Start Times & Ranges → Flatten Slots (`main`, output 0, input 0)
- Time available (true) & Call_id → Response (`main`, output 0, input 0)
- Check if time is available or not → Time available (true) & Call_id (`main`, output 0, input 0)
- Check if time is available or not → Get All Calendar Events (`main`, output 1, input 0)
- Convert into Json format for Vapi → Response to Vapi (`main`, output 0, input 0)
- Input Arguments from booking tools → Has all information (`main`, output 0, input 0)
- Information to be Saved in Airtable → Logs the confirmed booking details (`main`, output 0, input 0)
- Checks if required info is provided. → Finds original appointment (`main`, output 0, input 0)
- Checks if required info is provided. → Build Error Response Payload2 (`main`, output 1, input 0)
- Input Arguments from cancelslot tool → Checks if required info is provided for cancelation (`main`, output 0, input 0)
- Input Arguments from updateslot tool → Checks if required info is provided. (`main`, output 0, input 0)
- Convert time to CST America / Chicago → Create Event (`main`, output 0, input 0)
- If the booking is confirmed then true → Information to be Saved in Airtable (`main`, output 0, input 0)
- Checks if required info is provided for cancelation → Finds the appointment record (`main`, output 0, input 0)
- Checks if required info is provided for cancelation → Build Error Response (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0829_Webhook_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0829_Webhook_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
