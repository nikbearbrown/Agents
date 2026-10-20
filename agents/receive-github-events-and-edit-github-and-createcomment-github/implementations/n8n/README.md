# Githubtrigger Workflow

This folder contains the **Githubtrigger Workflow** workflow. Its executable nodes use `github`, `githubTrigger`, `if`, `noOp`, `stopAndError`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-github-events-and-edit-github-and-createcomment-github.json`](receive-github-events-and-edit-github-and-createcomment-github.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubOAuth2Api`

**Entry nodes:** Github Trigger, Githubtrigger 1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Github Trigger | `githubTrigger` | Inspect parameters |
| Githubtrigger 1 | `githubTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| IF no assignee? | `if` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |
| IF wants to work? | `if` | Inspect parameters |
| IF not assigned? | `if` | Inspect parameters |
| Assign Issue Creator | `github` | edit |
| Add Comment | `github` | createComment |
| NoOp1 | `noOp` | Inspect parameters |
| Assign Commenter | `github` | edit |
| Error Handler | `stopAndError` | Inspect parameters |

## Connection map

No connections are declared; this may be a fragment or a disconnected example.

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0108_Noop_GitHub_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0108_Noop_GitHub_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
