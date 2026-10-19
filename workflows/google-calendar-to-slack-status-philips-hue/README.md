# Google Calendar to Slack Status & Philips Hue

This folder contains the **Google Calendar to Slack Status & Philips Hue** workflow. Its executable nodes use `function`, `googleCalendar`, `googleCalendarTrigger`, `httpRequest`, `manualTrigger`, `slack`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-calendar-to-slack-status-philips-hue.json`](google-calendar-to-slack-status-philips-hue.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `slackApi`

**Entry nodes:** On clicking 'execute', Event Started

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Google Calendar | `googleCalendar` | get |
| Light - Busy | `httpRequest` | Inspect parameters |
| Light - Available | `httpRequest` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Light - Personal | `httpRequest` | Inspect parameters |
| Event Started | `googleCalendarTrigger` | Inspect parameters |
| Slack - Status | `slack` | userProfile / update |
| Set CalColor | `function` | Inspect parameters |

## Connection map

- Switch → Light - Busy (`main`, output 0, input 0)
- Switch → Light - Personal (`main`, output 1, input 0)
- Switch → Light - Available (`main`, output 3, input 0)
- Set CalColor → Slack - Status (`main`, output 0, input 0)
- Set CalColor → Switch (`main`, output 0, input 0)
- Event Started → Google Calendar (`main`, output 0, input 0)
- Google Calendar → Set CalColor (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0078_Manual_Slack_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0078_Manual_Slack_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
