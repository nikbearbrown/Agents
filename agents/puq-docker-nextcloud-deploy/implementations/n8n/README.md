# PUQ Docker NextCloud deploy

This folder contains the **PUQ Docker NextCloud deploy** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `respondToWebhook`, `set`, `ssh`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`puq-docker-nextcloud-deploy.json`](puq-docker-nextcloud-deploy.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `sshPassword`

**Entry nodes:** API

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If | `if` | Inspect parameters |
| Parametrs | `set` | Inspect parameters |
| API | `webhook` | Inspect parameters |
| 422-Invalid server domain | `respondToWebhook` | Inspect parameters |
| Container Actions | `switch` | Inspect parameters |
| Container Stats | `switch` | Inspect parameters |
| Inspect | `set` | Inspect parameters |
| Stat | `set` | Inspect parameters |
| Start | `set` | Inspect parameters |
| Stop | `set` | Inspect parameters |
| Mount Disk | `set` | Inspect parameters |
| Unmount Disk | `set` | Inspect parameters |
| Log | `set` | Inspect parameters |
| Deploy-docker-compose | `set` | Inspect parameters |
| Version | `set` | Inspect parameters |
| Users | `set` | Inspect parameters |
| Change Password | `set` | Inspect parameters |
| NextCloud | `switch` | Inspect parameters |
| nginx | `set` | Inspect parameters |
| Test Connection | `set` | Inspect parameters |
| ChangePackage | `set` | Inspect parameters |
| Terminated | `set` | Inspect parameters |
| Unsuspend | `set` | Inspect parameters |
| Suspend | `set` | Inspect parameters |
| Deploy | `set` | Inspect parameters |
| Service Actions | `switch` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Dependent containers Stat | `set` | Inspect parameters |
| GET ACL | `set` | Inspect parameters |
| SET ACL | `set` | Inspect parameters |
| GET NET | `set` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| Split domain | `code` | Inspect parameters |
| DNS Service Actions | `switch` | Inspect parameters |
| DNS Parametrs | `set` | Inspect parameters |
| Add record | `httpRequest` | PATCH |
| Delete record | `httpRequest` | PATCH |
| API answer1 | `respondToWebhook` | Inspect parameters |
| REPLACE_WITH_CREDENTIAL | `ssh` | Inspect parameters |
| REPLACE_WITH_CREDENTIAL | `ssh` | Inspect parameters |
| Servers Switch | `switch` | Inspect parameters |
| Code | `code` | Inspect parameters |
| API answer2 | `respondToWebhook` | Inspect parameters |

## Connection map

- If → Container Stats (`main`, output 0, input 0)
- If → Container Actions (`main`, output 0, input 0)
- If → NextCloud (`main`, output 0, input 0)
- If → If1 (`main`, output 0, input 0)
- If → 422-Invalid server domain (`main`, output 1, input 0)
- API → Parametrs (`main`, output 0, input 0)
- If1 → nginx (`main`, output 0, input 0)
- If1 → Service Actions (`main`, output 1, input 0)
- If2 → DNS Service Actions (`main`, output 0, input 0)
- Log → Servers Switch (`main`, output 0, input 0)
- Code → API answer2 (`main`, output 0, input 0)
- Stat → Servers Switch (`main`, output 0, input 0)
- Stop → Servers Switch (`main`, output 0, input 0)
- Start → Servers Switch (`main`, output 0, input 0)
- Users → Servers Switch (`main`, output 0, input 0)
- nginx → Deploy-docker-compose (`main`, output 0, input 0)
- Deploy → Servers Switch (`main`, output 0, input 0)
- GET ACL → Servers Switch (`main`, output 0, input 0)
- GET NET → Servers Switch (`main`, output 0, input 0)
- Inspect → Servers Switch (`main`, output 0, input 0)
- SET ACL → Servers Switch (`main`, output 0, input 0)
- Suspend → Servers Switch (`main`, output 0, input 0)
- Version → Servers Switch (`main`, output 0, input 0)
- NextCloud → Version (`main`, output 0, input 0)
- NextCloud → Users (`main`, output 1, input 0)
- NextCloud → Change Password (`main`, output 2, input 0)
- Parametrs → If (`main`, output 0, input 0)
- Unsuspend → Servers Switch (`main`, output 0, input 0)
- Mount Disk → Servers Switch (`main`, output 0, input 0)
- Terminated → Servers Switch (`main`, output 0, input 0)
- Split domain → DNS Parametrs (`main`, output 0, input 0)
- Unmount Disk → Servers Switch (`main`, output 0, input 0)
- ChangePackage → Servers Switch (`main`, output 0, input 0)
- DNS Parametrs → If2 (`main`, output 0, input 0)
- Servers Switch → REPLACE_WITH_CREDENTIAL (`main`, output 0, input 0)
- Servers Switch → REPLACE_WITH_CREDENTIAL (`main`, output 1, input 0)
- Change Password → Servers Switch (`main`, output 0, input 0)
- Container Stats → Inspect (`main`, output 0, input 0)
- Container Stats → Stat (`main`, output 1, input 0)
- Container Stats → Log (`main`, output 2, input 0)
- Container Stats → Dependent containers Stat (`main`, output 3, input 0)
- Container Stats → Split domain (`main`, output 4, input 0)
- Service Actions → Test Connection (`main`, output 0, input 0)
- Service Actions → Deploy (`main`, output 1, input 0)
- Service Actions → Split domain (`main`, output 1, input 0)
- Service Actions → Suspend (`main`, output 2, input 0)
- Service Actions → Unsuspend (`main`, output 3, input 0)
- Service Actions → Terminated (`main`, output 4, input 0)
- Service Actions → Split domain (`main`, output 4, input 0)
- Service Actions → ChangePackage (`main`, output 5, input 0)
- Service Actions → Split domain (`main`, output 5, input 0)
- Test Connection → Servers Switch (`main`, output 0, input 0)
- d01-test.uuq.pl → Code (`main`, output 0, input 0)
- d01-test.uuq.pl → Code (`main`, output 1, input 0)
- d02-test.uuq.pl → Code (`main`, output 0, input 0)
- d02-test.uuq.pl → Code (`main`, output 1, input 0)
- Container Actions → Start (`main`, output 0, input 0)
- Container Actions → Stop (`main`, output 1, input 0)
- Container Actions → Mount Disk (`main`, output 2, input 0)
- Container Actions → Unmount Disk (`main`, output 3, input 0)
- Container Actions → GET ACL (`main`, output 4, input 0)
- Container Actions → SET ACL (`main`, output 5, input 0)
- Container Actions → GET NET (`main`, output 6, input 0)
- DNS Service Actions → Add record (`main`, output 0, input 0)
- DNS Service Actions → API answer1 (`main`, output 0, input 0)
- DNS Service Actions → Add record (`main`, output 1, input 0)
- DNS Service Actions → Delete record (`main`, output 2, input 0)
- DNS Service Actions → Add record (`main`, output 3, input 0)
- DNS Service Actions → Delete record (`main`, output 4, input 0)
- DNS Service Actions → Add record (`main`, output 5, input 0)
- Deploy-docker-compose → Service Actions (`main`, output 0, input 0)
- Dependent containers Stat → Servers Switch (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1832_Code_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1832_Code_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
