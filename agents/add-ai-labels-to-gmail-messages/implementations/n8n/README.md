# Add AI labels to Gmail messages

This folder contains the **Add AI labels to Gmail messages** workflow. Its executable nodes use `aggregate`, `chainLlm`, `gmail`, `gmailTrigger`, `lmChatOpenAi`, `merge`, `outputParserStructured`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`add-ai-labels-to-gmail-messages.json`](add-ai-labels-to-gmail-messages.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Gmail trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail trigger | `gmailTrigger` | Inspect parameters |
| Get message content | `gmail` | get |
| Set label values | `set` | Inspect parameters |
| Get all labels | `gmail` | label |
| Split out assigned labels | `splitOut` | Inspect parameters |
| Merge corresponding labels | `merge` | Inspect parameters |
| Aggregate label IDs | `aggregate` | Inspect parameters |
| Add labels to message | `gmail` | addLabels |
| Assign labels for message | `chainLlm` | Inspect parameters |
| JSON Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat | `lmChatOpenAi` | Inspect parameters |

## Connection map

- JSON Parser → Assign labels for message (`ai_outputParser`, output 0, input 0)
- OpenAI Chat → Assign labels for message (`ai_languageModel`, output 0, input 0)
- Gmail trigger → Get message content (`main`, output 0, input 0)
- Get all labels → Merge corresponding labels (`main`, output 0, input 0)
- Set label values → Get all labels (`main`, output 0, input 0)
- Set label values → Split out assigned labels (`main`, output 0, input 0)
- Aggregate label IDs → Add labels to message (`main`, output 0, input 0)
- Get message content → Assign labels for message (`main`, output 0, input 0)
- Assign labels for message → Set label values (`main`, output 0, input 0)
- Split out assigned labels → Merge corresponding labels (`main`, output 0, input 1)
- Merge corresponding labels → Aggregate label IDs (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1324_Aggregate_Gmail_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1324_Aggregate_Gmail_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
