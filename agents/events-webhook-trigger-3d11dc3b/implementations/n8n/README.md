# Events Webhook Trigger

This folder contains the **Events Webhook Trigger** workflow. Its executable nodes use `httpRequest`, `if`, `noOp`, `respondToWebhook`, `set`, `slack`, `switch`, `theHiveProject`, `theHiveProjectTrigger`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`events-webhook-trigger-3d11dc3b.json`](events-webhook-trigger-3d11dc3b.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`, `theHiveProjectApi`

**Entry nodes:** TheHive Trigger, Receive Button Press

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| TheHive Trigger | `theHiveProjectTrigger` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Task Modal | `httpRequest` | POST |
| HTTP Request | `httpRequest` | Inspect parameters |
| Formatting Dictionaries | `set` | Inspect parameters |
| Prep Fields For Slack | `set` | Inspect parameters |
| Update Message with new Assignee | `httpRequest` | POST |
| Check if Case Options | `if` | Inspect parameters |
| Case Slack Block Rebuild | `set` | Inspect parameters |
| Close Case Block Rebuild | `set` | Inspect parameters |
| Severity Case Block Rebuild1 | `set` | Inspect parameters |
| PAP Case Block Rebuild | `set` | Inspect parameters |
| Prep Fields For PAP Slack | `set` | Inspect parameters |
| Map Actions | `set` | Inspect parameters |
| Build Final Block | `set` | Inspect parameters |
| Prep Fields For TLP Slack | `set` | Inspect parameters |
| Prep Fields For Status Slack | `set` | Inspect parameters |
| Update Status in TheHive | `theHiveProject` | case / update |
| Close Case as False Positive | `theHiveProject` | case / update |
| Status Case Block Rebuild | `set` | Inspect parameters |
| TLP Case Block Rebuild | `set` | Inspect parameters |
| No Action Needed | `noOp` | Inspect parameters |
| Post New Case To Slack | `slack` | Inspect parameters |
| Prep Fields For Slack - Close | `set` | Inspect parameters |
| Prep Fields For Slack - Assign | `set` | Inspect parameters |
| Prep Fields For Slack - Severity | `set` | Inspect parameters |
| Update Case Severity | `theHiveProject` | case / update |
| Update Case PAP | `theHiveProject` | case / update |
| Update Case TLP | `theHiveProject` | case / update |
| Acknowledge Close Case to Slack | `respondToWebhook` | Inspect parameters |
| Acknowledge Severity Update to Slack | `respondToWebhook` | Inspect parameters |
| Acknowledge PAP Update to Slack | `respondToWebhook` | Inspect parameters |
| Acknowledge TLP Update to Slack | `respondToWebhook` | Inspect parameters |
| Acknowledge Status Update to Slack | `respondToWebhook` | Inspect parameters |
| Acknowledge Modal Request to Slack | `respondToWebhook` | Inspect parameters |
| Parse Message Type | `switch` | Inspect parameters |
| Respond positive to Slack when someone clicks a link | `respondToWebhook` | Inspect parameters |
| Respond 204 to Slack | `respondToWebhook` | Inspect parameters |
| Close Modal with 204 response | `respondToWebhook` | Inspect parameters |
| Get Slack User's Email From Slack | `slack` | user |
| Update TheHive Case with new Assignee | `theHiveProject` | case / update |
| Respond to Slack with 200 response | `respondToWebhook` | Inspect parameters |
| Get Email From Slack to assign the task to in TheHive | `slack` | user |
| Add a task to TheHive | `theHiveProject` | task |
| Receive Button Press | `webhook` | Inspect parameters |

## Connection map

- Edit Fields → Parse Message Type (`main`, output 0, input 0)
- Map Actions → Build Final Block (`main`, output 0, input 0)
- HTTP Request → Prep Fields For Slack (`main`, output 0, input 0)
- TheHive Trigger → Formatting Dictionaries (`main`, output 0, input 0)
- Update Case PAP → PAP Case Block Rebuild (`main`, output 0, input 0)
- Update Case TLP → TLP Case Block Rebuild (`main`, output 0, input 0)
- Build Final Block → Update Message with new Assignee (`main`, output 0, input 0)
- Parse Message Type → Respond to Slack with 200 response (`main`, output 0, input 0)
- Parse Message Type → Acknowledge Close Case to Slack (`main`, output 1, input 0)
- Parse Message Type → Acknowledge Severity Update to Slack (`main`, output 2, input 0)
- Parse Message Type → Acknowledge Modal Request to Slack (`main`, output 3, input 0)
- Parse Message Type → Check if Case Options (`main`, output 4, input 0)
- Parse Message Type → Acknowledge PAP Update to Slack (`main`, output 5, input 0)
- Parse Message Type → Acknowledge Status Update to Slack (`main`, output 6, input 0)
- Parse Message Type → Acknowledge TLP Update to Slack (`main`, output 7, input 0)
- Parse Message Type → Respond positive to Slack when someone clicks a link (`main`, output 8, input 0)
- Receive Button Press → Edit Fields (`main`, output 0, input 0)
- Update Case Severity → Severity Case Block Rebuild1 (`main`, output 0, input 0)
- Check if Case Options → Close Modal with 204 response (`main`, output 0, input 0)
- Check if Case Options → Respond 204 to Slack (`main`, output 1, input 0)
- Prep Fields For Slack → Post New Case To Slack (`main`, output 0, input 0)
- PAP Case Block Rebuild → Map Actions (`main`, output 0, input 0)
- TLP Case Block Rebuild → Map Actions (`main`, output 0, input 0)
- Formatting Dictionaries → HTTP Request (`main`, output 0, input 0)
- Case Slack Block Rebuild → Map Actions (`main`, output 0, input 0)
- Close Case Block Rebuild → Map Actions (`main`, output 0, input 0)
- Update Status in TheHive → Status Case Block Rebuild (`main`, output 0, input 0)
- Prep Fields For PAP Slack → Update Case PAP (`main`, output 0, input 0)
- Prep Fields For TLP Slack → Update Case TLP (`main`, output 0, input 0)
- Status Case Block Rebuild → Map Actions (`main`, output 0, input 0)
- Close Case as False Positive → Close Case Block Rebuild (`main`, output 0, input 0)
- Prep Fields For Status Slack → Update Status in TheHive (`main`, output 0, input 0)
- Severity Case Block Rebuild1 → Map Actions (`main`, output 0, input 0)
- Close Modal with 204 response → Get Email From Slack to assign the task to in TheHive (`main`, output 0, input 0)
- Prep Fields For Slack - Close → Close Case as False Positive (`main`, output 0, input 0)
- Prep Fields For Slack - Assign → Get Slack User's Email From Slack (`main`, output 0, input 0)
- Acknowledge Close Case to Slack → Prep Fields For Slack - Close (`main`, output 0, input 0)
- Acknowledge PAP Update to Slack → Prep Fields For PAP Slack (`main`, output 0, input 0)
- Acknowledge TLP Update to Slack → Prep Fields For TLP Slack (`main`, output 0, input 0)
- Prep Fields For Slack - Severity → Update Case Severity (`main`, output 0, input 0)
- Get Slack User's Email From Slack → Update TheHive Case with new Assignee (`main`, output 0, input 0)
- Acknowledge Modal Request to Slack → Task Modal (`main`, output 0, input 0)
- Acknowledge Status Update to Slack → Prep Fields For Status Slack (`main`, output 0, input 0)
- Respond to Slack with 200 response → Prep Fields For Slack - Assign (`main`, output 0, input 0)
- Acknowledge Severity Update to Slack → Prep Fields For Slack - Severity (`main`, output 0, input 0)
- Update TheHive Case with new Assignee → Case Slack Block Rebuild (`main`, output 0, input 0)
- Respond positive to Slack when someone clicks a link → No Action Needed (`main`, output 0, input 0)
- Get Email From Slack to assign the task to in TheHive → Add a task to TheHive (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0644_Webhook_Slack_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0644_Webhook_Slack_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
