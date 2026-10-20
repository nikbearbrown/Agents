# Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack

This folder contains the **Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack** workflow. Its executable nodes use `httpRequest`, `itemLists`, `jira`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`analyze-crowdstrike-detections-search-for-iocs-in-virustotal-create-a-ticket-in-jira-and-post-a-message-in-sla.json`](analyze-crowdstrike-detections-search-for-iocs-in-virustotal-create-a-ticket-in-jira-and-post-a-message-in-sla.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `crowdStrikeOAuth2Api`, `jiraSoftwareCloudApi`, `slackOAuth2Api`, `virusTotalApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Split out detections | `itemLists` | Inspect parameters |
| Get recent detections from Crowdstrike | `httpRequest` | Inspect parameters |
| Get detection details | `httpRequest` | POST |
| Split out behaviours | `itemLists` | Inspect parameters |
| Look up SHA in Virustotal | `httpRequest` | Inspect parameters |
| Look up IOC in Virustotal | `httpRequest` | Inspect parameters |
| Split In Batches | `splitInBatches` | Inspect parameters |
| Merge behaviour descriptions | `itemLists` | summarize |
| Set behaviour descriptions | `set` | Inspect parameters |
| Create Jira issue | `jira` | Inspect parameters |
| Post notification on Slack | `slack` | Inspect parameters |
| Pause 1 second | `wait` | Inspect parameters |

## Connection map

- Pause 1 second → Look up SHA in Virustotal (`main`, output 0, input 0)
- Schedule Trigger → Get recent detections from Crowdstrike (`main`, output 0, input 0)
- Split In Batches → Split out behaviours (`main`, output 0, input 0)
- Create Jira issue → Post notification on Slack (`main`, output 0, input 0)
- Split out behaviours → Pause 1 second (`main`, output 0, input 0)
- Split out detections → Get detection details (`main`, output 0, input 0)
- Get detection details → Split In Batches (`main`, output 0, input 0)
- Look up IOC in Virustotal → Set behaviour descriptions (`main`, output 0, input 0)
- Look up SHA in Virustotal → Look up IOC in Virustotal (`main`, output 0, input 0)
- Post notification on Slack → Split In Batches (`main`, output 0, input 0)
- Set behaviour descriptions → Merge behaviour descriptions (`main`, output 0, input 0)
- Merge behaviour descriptions → Create Jira issue (`main`, output 0, input 0)
- Get recent detections from Crowdstrike → Split out detections (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1312_Wait_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1312_Wait_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
