# ⚡AI-Powered YouTube Playlist &amp; Video Summarization and Analysis v2: shared specification

**Status: source-derived draft.** The source contains 60 executable nodes and 64 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

## Purpose

Adapt the published “⚡AI-Powered YouTube Playlist &amp; Video Summarization and Analysis v2” workflow to other implementations while preserving its documented behavior.

The title is inherited from the source, not proof of intent. Confirm the actual user outcome before porting. Deterministic automations are included in this library; “agent” does not imply autonomous model judgment.

## Observed entry points

- Chat

## Terminal nodes

- Google Gemini Chat Model1
- Handle Queries
- Recursive Character Text Splitter
- Embeddings Google Gemini
- Google Gemini Chat Model2
- Embeddings Google Gemini1
- AI Agent
- Google Gemini Chat Model4
- Default Data Loader
- Chat Buffer Memory
- Chat Buffer Memory1
- Structured Output Parser1
- Simple Memory
- Simple Memory3
- Google Gemini Chat Model6
- Numb of Videos
- Google Gemini Chat Model8
- Embeddings Google Gemini2
- Qdrant Vector Store3
- Answer questions with a vector store
- Qdrant Vector Store4
- Answer questions with a vector store1
- Google Gemini Chat Model
- Google Gemini Chat Model3
- Embeddings Google Gemini4

## Inputs, outputs, decisions and state

Input and output schemas are not yet established. Read the exact parameters, expressions, prompts, code, branch ports, retries, disabled nodes, and execution settings in the n8n implementation. A terminal node is a graph endpoint, not necessarily a user-facing output. Model/tool links are dependencies, not necessarily sequential control flow.

## Required access

Declared credential types: `googlePalmApi`, `qdrantApi`, `redis`. Use local credentials or environment variables, never public exports.

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
