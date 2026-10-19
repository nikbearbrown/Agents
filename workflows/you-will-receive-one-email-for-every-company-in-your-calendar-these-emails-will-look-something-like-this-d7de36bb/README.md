# 📬 You will receive one email for every company in your calendar. These emails will look something like this:

This folder contains the **📬 You will receive one email for every company in your calendar. These emails will look something like this:** workflow. Its executable nodes use `clearbit`, `filter`, `gmail`, `googleCalendar`, `html`, `httpRequest`, `merge`, `openAi`, `scheduleTrigger`, `set`, `splitOut`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`you-will-receive-one-email-for-every-company-in-your-calendar-these-emails-will-look-something-like-this-d7de36bb.json`](you-will-receive-one-email-for-every-company-in-your-calendar-these-emails-will-look-something-like-this-d7de36bb.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clearbitApi`, `gmailOAuth2`, `googleCalendarOAuth2Api`, `openAiApi`

**Entry nodes:** Every morning @ 7

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Setup | `set` | Inspect parameters |
| Every morning @ 7 | `scheduleTrigger` | Inspect parameters |
| Get meetings for today | `googleCalendar` | getAll |
| Get attendees email domains | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Get recent LinkedIn posts | `httpRequest` | Inspect parameters |
| Enrich attendee company | `clearbit` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Combine all activity for a company | `merge` | Inspect parameters |
| Extract data for email | `set` | Inspect parameters |
| Prepare email template | `html` | Inspect parameters |
| Keep only ones with the domain | `filter` | Inspect parameters |
| Extract important data | `set` | Inspect parameters |
| Extract important data again | `set` | Inspect parameters |
| Ask AI to summerize | `openAi` | chat |
| Switch | `switch` | Inspect parameters |
| Wrap everything together | `merge` | Inspect parameters |
| Get latest tweets | `httpRequest` | Inspect parameters |

## Connection map

- Setup → Get meetings for today (`main`, output 0, input 0)
- Switch → Get recent LinkedIn posts (`main`, output 0, input 0)
- Switch → Get latest tweets (`main`, output 1, input 0)
- Split Out → Keep only ones with the domain (`main`, output 0, input 0)
- Every morning @ 7 → Setup (`main`, output 0, input 0)
- Get latest tweets → Extract important data again (`main`, output 0, input 0)
- Ask AI to summerize → Wrap everything together (`main`, output 0, input 0)
- Extract data for email → Wrap everything together (`main`, output 0, input 1)
- Extract important data → Combine all activity for a company (`main`, output 0, input 0)
- Get meetings for today → Get attendees email domains (`main`, output 0, input 0)
- Prepare email template → Gmail (`main`, output 0, input 0)
- Enrich attendee company → Switch (`main`, output 0, input 0)
- Wrap everything together → Prepare email template (`main`, output 0, input 0)
- Get recent LinkedIn posts → Extract important data (`main`, output 0, input 0)
- Get attendees email domains → Split Out (`main`, output 0, input 0)
- Extract important data again → Combine all activity for a company (`main`, output 0, input 1)
- Keep only ones with the domain → Enrich attendee company (`main`, output 0, input 0)
- Combine all activity for a company → Ask AI to summerize (`main`, output 0, input 0)
- Combine all activity for a company → Extract data for email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0429_Splitout_GoogleCalendar_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0429_Splitout_GoogleCalendar_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
