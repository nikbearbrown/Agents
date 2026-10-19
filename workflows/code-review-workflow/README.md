# Code Review workflow

This folder contains the **Code Review workflow** workflow. Its executable nodes use `agent`, `code`, `github`, `githubTrigger`, `googleSheetsTool`, `httpRequest`, `lmChatOpenAi`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`code-review-workflow.json`](code-review-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `githubOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** PR Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| PR Trigger | `githubTrigger` | Inspect parameters |
| Get file's Diffs from PR | `httpRequest` | Inspect parameters |
| Create target Prompt from PR Diffs | `code` | Inspect parameters |
| GitHub Robot | `github` | review |
| Add Label to PR | `github` | edit |
| Code Best Practices | `googleSheetsTool` | Inspect parameters |
| Code Review Agent | `agent` | Inspect parameters |

## Connection map

- PR Trigger → Get file's Diffs from PR (`main`, output 0, input 0)
- GitHub Robot → Add Label to PR (`main`, output 0, input 0)
- Code Review Agent → GitHub Robot (`main`, output 0, input 0)
- OpenAI Chat Model → Code Review Agent (`ai_languageModel`, output 0, input 0)
- Code Best Practices → Code Review Agent (`ai_tool`, output 0, input 0)
- Get file's Diffs from PR → Create target Prompt from PR Diffs (`main`, output 0, input 0)
- Create target Prompt from PR Diffs → Code Review Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1292_Code_GitHub_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1292_Code_GitHub_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
