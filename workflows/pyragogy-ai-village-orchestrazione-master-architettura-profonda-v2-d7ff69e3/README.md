# Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)

This folder contains the **Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)** workflow. Its executable nodes use `emailSend`, `function`, `github`, `if`, `merge`, `openAi`, `postgres`, `respondToWebhook`, `slack`, `start`, `stopAndError`, `switch`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pyragogy-ai-village-orchestrazione-master-architettura-profonda-v2-d7ff69e3.json`](pyragogy-ai-village-orchestrazione-master-architettura-profonda-v2-d7ff69e3.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `emailSend`, `githubApi`, `openAiApi`, `postgres`

**Entry nodes:** Start, Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start | `start` | Inspect parameters |
| Webhook Trigger | `webhook` | Inspect parameters |
| Check DB Connection | `postgres` | executeQuery |
| Meta-Orchestrator | `openAi` | chat |
| Parse Orchestration Plan | `function` | Inspect parameters |
| More Agents to Run? | `if` | Inspect parameters |
| Prepare Agent Input | `function` | Inspect parameters |
| Route Agents with Switch | `switch` | Inspect parameters |
| Summarizer Agent | `openAi` | chat |
| Synthesizer Agent | `openAi` | chat |
| Peer Reviewer Agent | `openAi` | chat |
| Sensemaking Agent | `openAi` | chat |
| Prompt Engineer Agent | `openAi` | chat |
| Onboarding/Explainer Agent | `openAi` | chat |
| Add Handbook Metadata | `function` | Inspect parameters |
| Generate Content for Review | `function` | Inspect parameters |
| Generate Review ID | `function` | Inspect parameters |
| Send Review Request Email | `emailSend` | Inspect parameters |
| Wait for Human Approval | `wait` | Inspect parameters |
| Human Decision Split | `if` | Inspect parameters |
| Save to handbook_entries | `postgres` | insert |
| Prepare Approved Contribution Data | `function` | Inspect parameters |
| Save Agent Contribution (Approved) | `postgres` | insert |
| Generate GitHub File Path | `function` | Inspect parameters |
| GitHub Enabled? | `if` | Inspect parameters |
| Commit to GitHub (Approved) | `github` | file / createUpdate |
| Log Human Rejection | `function` | Inspect parameters |
| Merge Archivist Paths | `merge` | Inspect parameters |
| Evaluate Board Consensus | `function` | Inspect parameters |
| Check Redraft Needed | `if` | Inspect parameters |
| Handle Redraft | `function` | Inspect parameters |
| Process Agent Output | `function` | Inspect parameters |
| Slack Enabled? | `if` | Inspect parameters |
| Notify Slack | `slack` | Inspect parameters |
| Final Response | `respondToWebhook` | Inspect parameters |
| Error Handler | `stopAndError` | Inspect parameters |

## Connection map

No connections are declared; this may be a fragment or a disconnected example.

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"javascript_syntax": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/generate-collaborative-handbooks-with-gpt4o-multi-agent-orchestration-human-review.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/generate-collaborative-handbooks-with-gpt4o-multi-agent-orchestration-human-review.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
