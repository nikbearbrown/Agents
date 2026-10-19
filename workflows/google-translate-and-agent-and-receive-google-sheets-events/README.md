# google translate and agent and receive google sheets events

This folder contains the **google translate and agent and receive google sheets events** workflow. Its executable nodes use `agent`, `googleDrive`, `googleSheets`, `googleSheetsTrigger`, `googleTranslate`, `httpRequest`, `if`, `lmChatOpenAi`, `merge`, `noOp`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-translate-and-agent-and-receive-google-sheets-events.json`](google-translate-and-agent-and-receive-google-sheets-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Trigger Added Row

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Translate | `googleTranslate` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Trigger Added Row | `googleSheetsTrigger` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Upload Picture | `googleDrive` | Inspect parameters |
| Get Picture | `httpRequest` | Inspect parameters |
| Call API Pexels | `httpRequest` | Inspect parameters |
| Take initialText | `set` | Inspect parameters |
| Extract Image Link | `set` | Inspect parameters |
| Final Merge | `merge` | Inspect parameters |
| Extract Pinyin and Example | `set` | Inspect parameters |
| Extract Fields | `set` | Inspect parameters |
| initialText is empty? | `if` | Inspect parameters |
| Add Results in Sheet | `googleSheets` | update |

## Connection map

- Merge → Final Merge (`main`, output 0, input 0)
- AI Agent → Extract Pinyin and Example (`main`, output 0, input 0)
- Final Merge → Add Results in Sheet (`main`, output 0, input 0)
- Get Picture → Upload Picture (`main`, output 0, input 0)
- Extract Fields → Merge (`main`, output 0, input 0)
- Upload Picture → Extract Image Link (`main`, output 0, input 0)
- Call API Pexels → Get Picture (`main`, output 0, input 0)
- Google Translate → Extract Fields (`main`, output 0, input 0)
- Google Translate → AI Agent (`main`, output 0, input 0)
- Take initialText → Call API Pexels (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Trigger Added Row → initialText is empty? (`main`, output 0, input 0)
- Trigger Added Row → Take initialText (`main`, output 0, input 0)
- Extract Image Link → Final Merge (`main`, output 0, input 1)
- initialText is empty? → Google Translate (`main`, output 0, input 0)
- initialText is empty? → No Operation, do nothing (`main`, output 1, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Extract Pinyin and Example → Merge (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletranslate/0788_Googletranslate_Noop_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletranslate/0788_Googletranslate_Noop_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
