# Auto Categorise Outlook Emails with AI

This folder contains the **Auto Categorise Outlook Emails with AI** workflow. Its executable nodes use `agent`, `filter`, `if`, `lmChatOllama`, `manualTrigger`, `markdown`, `merge`, `microsoftOutlook`, `set`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auto-categorise-outlook-emails-with-ai.json`](auto-categorise-outlook-emails-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Ollama Chat Model1 | `lmChatOllama` | Inspect parameters |
| Microsoft Outlook10 | `microsoftOutlook` | move |
| Microsoft Outlook12 | `microsoftOutlook` | update |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Microsoft Outlook13 | `microsoftOutlook` | update |
| Microsoft Outlook15 | `microsoftOutlook` | move |
| Microsoft Outlook16 | `microsoftOutlook` | update |
| Microsoft Outlook17 | `microsoftOutlook` | move |
| Microsoft Outlook18 | `microsoftOutlook` | update |
| Microsoft Outlook19 | `microsoftOutlook` | move |
| Markdown1 | `markdown` | Inspect parameters |
| varEmal1 | `set` | Inspect parameters |
| Microsoft Outlook20 | `microsoftOutlook` | update |
| Microsoft Outlook21 | `microsoftOutlook` | update |
| Filter1 | `filter` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Microsoft Outlook22 | `microsoftOutlook` | update |
| Catch Errors1 | `set` | Inspect parameters |
| varJSON1 | `set` | Inspect parameters |
| Microsoft Outlook23 | `microsoftOutlook` | getAll |
| varID & Category1 | `set` | Inspect parameters |
| Microsoft Outlook Move Message1 | `microsoftOutlook` | move |
| AI Agent1 | `agent` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Switch1 | `switch` | Inspect parameters |

## Connection map

- If1 → Microsoft Outlook Move Message1 (`main`, output 0, input 0)
- If1 → Merge1 (`main`, output 1, input 5)
- Merge1 → Loop Over Items1 (`main`, output 0, input 0)
- Filter1 → Loop Over Items1 (`main`, output 0, input 0)
- Switch1 → Microsoft Outlook12 (`main`, output 0, input 0)
- Switch1 → Microsoft Outlook13 (`main`, output 1, input 0)
- Switch1 → Microsoft Outlook18 (`main`, output 2, input 0)
- Switch1 → Microsoft Outlook16 (`main`, output 3, input 0)
- Switch1 → Microsoft Outlook20 (`main`, output 4, input 0)
- Switch1 → Microsoft Outlook22 (`main`, output 5, input 0)
- Switch1 → Microsoft Outlook21 (`main`, output 6, input 0)
- varEmal1 → varID & Category1 (`main`, output 0, input 0)
- varJSON1 → Switch1 (`main`, output 0, input 0)
- varJSON1 → Catch Errors1 (`main`, output 1, input 0)
- AI Agent1 → varJSON1 (`main`, output 0, input 0)
- Markdown1 → varEmal1 (`main`, output 0, input 0)
- Catch Errors1 → Loop Over Items1 (`main`, output 0, input 0)
- Loop Over Items1 → Markdown1 (`main`, output 1, input 0)
- varID & Category1 → AI Agent1 (`main`, output 0, input 0)
- Ollama Chat Model1 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- Microsoft Outlook10 → Merge1 (`main`, output 0, input 0)
- Microsoft Outlook12 → Microsoft Outlook10 (`main`, output 0, input 0)
- Microsoft Outlook13 → Microsoft Outlook15 (`main`, output 0, input 0)
- Microsoft Outlook15 → Merge1 (`main`, output 0, input 1)
- Microsoft Outlook16 → Microsoft Outlook17 (`main`, output 0, input 0)
- Microsoft Outlook17 → Merge1 (`main`, output 0, input 3)
- Microsoft Outlook18 → Microsoft Outlook19 (`main`, output 0, input 0)
- Microsoft Outlook19 → Merge1 (`main`, output 0, input 2)
- Microsoft Outlook20 → If1 (`main`, output 0, input 0)
- Microsoft Outlook21 → Merge1 (`main`, output 0, input 6)
- Microsoft Outlook22 → If1 (`main`, output 0, input 0)
- Microsoft Outlook23 → Filter1 (`main`, output 0, input 0)
- Microsoft Outlook Move Message1 → Merge1 (`main`, output 0, input 4)
- When clicking ‘Test workflow’ → Microsoft Outlook23 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0595_Filter_Manual_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0595_Filter_Manual_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
