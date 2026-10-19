# Suspicious_login_detection

This folder contains the **Suspicious_login_detection** workflow. Its executable nodes use `code`, `gmail`, `html`, `httpRequest`, `if`, `manualTrigger`, `merge`, `noOp`, `postgres`, `set`, `slack`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`suspicious-login-detection.json`](suspicious-login-detection.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `httpHeaderAuth`, `httpQueryAuth`, `postgres`, `slackApi`

**Entry nodes:** New /login event, When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract relevant data | `set` | Inspect parameters |
| New /login event | `webhook` | Inspect parameters |
| Unknown threat? | `if` | Inspect parameters |
| Get last 10 logins from the same user | `postgres` | executeQuery |
| Query IP API1 | `httpRequest` | Inspect parameters |
| New location? | `if` | Inspect parameters |
| Parse User Agent | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| New Device/Browser? | `if` | Inspect parameters |
| Complete login info | `merge` | Inspect parameters |
| Query user by ID | `postgres` | executeQuery |
| New Location | `noOp` | Inspect parameters |
| New Device/Browser | `noOp` | Inspect parameters |
| User has email? | `if` | Inspect parameters |
| HTML | `html` | Inspect parameters |
| Inform user | `gmail` | Inspect parameters |
| noise? | `if` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Check trust level | `switch` | Inspect parameters |
| Check classification | `switch` | Inspect parameters |
| riot? | `if` | Inspect parameters |
| 🔴 Priority: HIGH | `set` | Inspect parameters |
| 🟡 Priority: MEDIUM | `set` | Inspect parameters |
| 🟢 Priority: LOW | `set` | Inspect parameters |
| GreyNoise | `httpRequest` | Inspect parameters |
| IP API | `httpRequest` | Inspect parameters |
| UserParser | `httpRequest` | Inspect parameters |
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Example event | `code` | Inspect parameters |
| Known, Do Nothing | `noOp` | Inspect parameters |
| Known Location | `noOp` | Inspect parameters |
| Old Device/Browser | `noOp` | Inspect parameters |
| Not Riot | `noOp` | Inspect parameters |

## Connection map

- HTML → Inform user (`main`, output 0, input 0)
- Merge → Complete login info (`main`, output 0, input 1)
- riot? → Check trust level (`main`, output 0, input 0)
- riot? → Not Riot (`main`, output 1, input 0)
- IP API → Merge (`main`, output 0, input 0)
- noise? → Check classification (`main`, output 0, input 0)
- noise? → riot? (`main`, output 1, input 0)
- GreyNoise → Complete login info (`main`, output 0, input 0)
- GreyNoise → noise? (`main`, output 0, input 0)
- UserParser → Merge (`main`, output 0, input 1)
- New Location → Query user by ID (`main`, output 0, input 0)
- Example event → Extract relevant data (`main`, output 0, input 0)
- New location? → New Location (`main`, output 0, input 0)
- New location? → Known Location (`main`, output 1, input 0)
- Query IP API1 → New location? (`main`, output 0, input 0)
- Unknown threat? → Get last 10 logins from the same user (`main`, output 0, input 0)
- Unknown threat? → Known, Do Nothing (`main`, output 1, input 0)
- User has email? → HTML (`main`, output 0, input 0)
- New /login event → Extract relevant data (`main`, output 0, input 0)
- Parse User Agent → New Device/Browser? (`main`, output 0, input 0)
- Query user by ID → User has email? (`main`, output 0, input 0)
- Check trust level → 🔴 Priority: HIGH (`main`, output 1, input 0)
- Check trust level → 🟡 Priority: MEDIUM (`main`, output 2, input 0)
- Check trust level → 🟢 Priority: LOW (`main`, output 3, input 0)
- New Device/Browser → Query user by ID (`main`, output 0, input 0)
- 🟢 Priority: LOW → Slack (`main`, output 0, input 0)
- Complete login info → Unknown threat? (`main`, output 0, input 0)
- New Device/Browser? → New Device/Browser (`main`, output 0, input 0)
- New Device/Browser? → Old Device/Browser (`main`, output 1, input 0)
- 🔴 Priority: HIGH → Slack (`main`, output 0, input 0)
- Check classification → 🔴 Priority: HIGH (`main`, output 0, input 0)
- Check classification → 🟡 Priority: MEDIUM (`main`, output 1, input 0)
- Check classification → 🟢 Priority: LOW (`main`, output 2, input 0)
- Extract relevant data → GreyNoise (`main`, output 0, input 0)
- Extract relevant data → UserParser (`main`, output 0, input 0)
- Extract relevant data → IP API (`main`, output 0, input 0)
- 🟡 Priority: MEDIUM → Slack (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Example event (`main`, output 0, input 0)
- Get last 10 logins from the same user → Query IP API1 (`main`, output 0, input 0)
- Get last 10 logins from the same user → Parse User Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/2014_Postgres_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/2014_Postgres_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
