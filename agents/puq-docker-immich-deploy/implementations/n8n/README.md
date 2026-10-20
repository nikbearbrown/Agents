# puq-docker-immich-deploy

This folder contains the **puq-docker-immich-deploy** workflow. Its executable nodes use `code`, `if`, `respondToWebhook`, `set`, `ssh`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`puq-docker-immich-deploy.json`](puq-docker-immich-deploy.json): sanitized, inactive import copy with an overview sticky note.
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
| Code1 | `code` | Inspect parameters |
| SSH | `ssh` | Inspect parameters |
| Container Actions | `switch` | Inspect parameters |
| Service Actions | `switch` | Inspect parameters |
| API answer | `respondToWebhook` | Inspect parameters |
| Inspect | `set` | Inspect parameters |
| Stat | `set` | Inspect parameters |
| Start | `set` | Inspect parameters |
| Stop | `set` | Inspect parameters |
| Test Connection1 | `set` | Inspect parameters |
| Deploy | `set` | Inspect parameters |
| Suspend | `set` | Inspect parameters |
| Terminated | `set` | Inspect parameters |
| Unsuspend | `set` | Inspect parameters |
| Mount Disk | `set` | Inspect parameters |
| Unmount Disk | `set` | Inspect parameters |
| Log | `set` | Inspect parameters |
| ChangePackage | `set` | Inspect parameters |
| Deploy-docker-compose | `set` | Inspect parameters |
| Version | `set` | Inspect parameters |
| Users | `set` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| nginx | `set` | Inspect parameters |
| Container Stat | `switch` | Inspect parameters |
| GET ACL | `set` | Inspect parameters |
| SET ACL | `set` | Inspect parameters |
| GET NET | `set` | Inspect parameters |
| Dependent containers Stat | `set` | Inspect parameters |
| Change Password | `set` | Inspect parameters |
| Immich | `switch` | Inspect parameters |

## Connection map

- If → Container Stat (`main`, output 0, input 0)
- If → Container Actions (`main`, output 0, input 0)
- If → Immich (`main`, output 0, input 0)
- If → If1 (`main`, output 0, input 0)
- If → 422-Invalid server domain (`main`, output 1, input 0)
- API → Parametrs (`main`, output 0, input 0)
- If1 → nginx (`main`, output 0, input 0)
- If1 → Service Actions (`main`, output 1, input 0)
- Log → SSH (`main`, output 0, input 0)
- SSH → Code1 (`main`, output 0, input 0)
- SSH → Code1 (`main`, output 1, input 0)
- Stat → SSH (`main`, output 0, input 0)
- Stop → SSH (`main`, output 0, input 0)
- Code1 → API answer (`main`, output 0, input 0)
- Start → SSH (`main`, output 0, input 0)
- Users → SSH (`main`, output 0, input 0)
- nginx → Deploy-docker-compose (`main`, output 0, input 0)
- Deploy → SSH (`main`, output 0, input 0)
- Immich → Version (`main`, output 0, input 0)
- Immich → Users (`main`, output 1, input 0)
- Immich → Change Password (`main`, output 2, input 0)
- GET ACL → SSH (`main`, output 0, input 0)
- GET NET → SSH (`main`, output 0, input 0)
- Inspect → SSH (`main`, output 0, input 0)
- SET ACL → SSH (`main`, output 0, input 0)
- Suspend → SSH (`main`, output 0, input 0)
- Version → SSH (`main`, output 0, input 0)
- Parametrs → If (`main`, output 0, input 0)
- Unsuspend → SSH (`main`, output 0, input 0)
- Mount Disk → SSH (`main`, output 0, input 0)
- Terminated → SSH (`main`, output 0, input 0)
- Unmount Disk → SSH (`main`, output 0, input 0)
- ChangePackage → SSH (`main`, output 0, input 0)
- Container Stat → Inspect (`main`, output 0, input 0)
- Container Stat → Stat (`main`, output 1, input 0)
- Container Stat → Log (`main`, output 2, input 0)
- Container Stat → Dependent containers Stat (`main`, output 3, input 0)
- Change Password → SSH (`main`, output 0, input 0)
- Service Actions → Test Connection1 (`main`, output 0, input 0)
- Service Actions → Deploy (`main`, output 1, input 0)
- Service Actions → Suspend (`main`, output 2, input 0)
- Service Actions → Unsuspend (`main`, output 3, input 0)
- Service Actions → Terminated (`main`, output 4, input 0)
- Service Actions → ChangePackage (`main`, output 5, input 0)
- Test Connection1 → SSH (`main`, output 0, input 0)
- Container Actions → Start (`main`, output 0, input 0)
- Container Actions → Stop (`main`, output 1, input 0)
- Container Actions → Mount Disk (`main`, output 2, input 0)
- Container Actions → Unmount Disk (`main`, output 3, input 0)
- Container Actions → GET ACL (`main`, output 4, input 0)
- Container Actions → SET ACL (`main`, output 5, input 0)
- Container Actions → GET NET (`main`, output 6, input 0)
- Deploy-docker-compose → Service Actions (`main`, output 0, input 0)
- Dependent containers Stat → SSH (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1966_Code_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1966_Code_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
