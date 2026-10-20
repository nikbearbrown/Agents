# Tech_Stack_Directional_Signal_Agent

This folder contains the **Tech_Stack_Directional_Signal_Agent** workflow. Its executable nodes use `code`, `formTrigger`, `httpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`tech-stack-directional-signal-agent.json`](tech-stack-directional-signal-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Form Trigger | `formTrigger` | Inspect parameters |
| Company Input | `code` | Inspect parameters |
| GitHub GraphQL | `httpRequest` | POST |
| Process Repos + Language Analysis | `code` | Inspect parameters |
| Fetch Commit Activity | `code` | Inspect parameters |
| Velocity Analysis | `code` | Inspect parameters |
| Build Groq Prompt | `code` | Inspect parameters |
| Groq AI Analysis | `httpRequest` | POST |
| Score + Claims Schema | `code` | Inspect parameters |
| Generate Dashboard | `code` | Inspect parameters |
| Export HTML File | `code` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- Company Input → GitHub GraphQL (`main`, output 0, input 0)
- GitHub GraphQL → Process Repos + Language Analysis (`main`, output 0, input 0)
- Process Repos + Language Analysis → Fetch Commit Activity (`main`, output 0, input 0)
- Fetch Commit Activity → Velocity Analysis (`main`, output 0, input 0)
- Velocity Analysis → Build Groq Prompt (`main`, output 0, input 0)
- Build Groq Prompt → Groq AI Analysis (`main`, output 0, input 0)
- Groq AI Analysis → Score + Claims Schema (`main`, output 0, input 0)
- Score + Claims Schema → Generate Dashboard (`main`, output 0, input 0)
- Generate Dashboard → Export HTML File (`main`, output 0, input 0)
- Form Trigger → Company Input (`main`, output 0, input 0)
- Export HTML File → Code (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
