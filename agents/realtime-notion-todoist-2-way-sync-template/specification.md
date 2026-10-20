# Realtime Notion Todoist 2-way Sync Template: shared specification

**Status: source-derived draft.** The source contains 174 executable nodes and 197 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

## Purpose

Adapt the published “Realtime Notion Todoist 2-way Sync Template” workflow to other implementations while preserving its documented behavior.

The title is inherited from the source, not proof of intent. Confirm the actual user outcome before porting. Deterministic automations are included in this library; “agent” does not imply autonomous model judgment.

## Observed entry points

- OAuth redirect
- Notion-Todoist Sync Setup Helper
- Todoist Webhook Setup Helper
- Schedule Trigger
- Execute Workflow Trigger
- Notion Webhook
- Todoist Webhook
- Webhook

## Terminal nodes

- Redirect to Auth Page
- Respond with success
- Respond with error
- Return config JSON
- Lock Todoist ID
- Lock Todoist ID1
- Lock Todoist ID2
- Gmail
- Globals
- Execute Workflow Trigger
- Lock Notion ID
- Update Description in Todoist
- Update Description in Todoist1
- Update section (Sync API)1
- Globals1
- Store Todoist ID1
- Globals2
- Lock Todoist ID4
- Execute Workflow
- Execute Workflow1
- End here
- Retry limit reached
- Retry limit reached1
- Retry limit reached2

## Inputs, outputs, decisions and state

Input and output schemas are not yet established. Read the exact parameters, expressions, prompts, code, branch ports, retries, disabled nodes, and execution settings in the n8n implementation. A terminal node is a graph endpoint, not necessarily a user-facing output. Model/tool links are dependencies, not necessarily sequential control flow.

## Required access

Declared credential types: `gmailOAuth2`, `notionApi`, `redis`, `todoistApi`. Use local credentials or environment variables, never public exports.

## Port acceptance criteria

- Write a reviewed purpose and concrete input/output schema.
- Preserve identifiers, ordering, routing ports, expressions, state semantics, retries, and disabled behavior unless a documented change is intended.
- Add representative success, empty-input, malformed-input, authentication failure, unavailable dependency, and duplicate/retry fixtures where relevant.
- Start with fixtures and dry-run adapters. No messages, writes, purchases, or scheduled work from a build prompt.
- Compare deterministic translations on identical fixtures. Measure model judgments against human-labeled examples separately from agreement with the old implementation.
- Record code revision, fixture hash, command, observed output and limitations. Never infer a passing test from a diagram or a generated explanation.

## Unresolved questions

- Define input/output schemas and expected outputs.
- Review source expressions, external actions, and failure behavior.
- Determine whether model judgment is required or deterministic rules suffice.
