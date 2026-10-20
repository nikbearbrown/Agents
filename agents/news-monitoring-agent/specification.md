# News Monitoring Agent: shared specification

**Status: source-derived draft.** The source contains 74 executable nodes and 75 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

## Purpose

Adapt the published “News Monitoring Agent” workflow to other implementations while preserving its documented behavior.

The title is inherited from the source, not proof of intent. Confirm the actual user outcome before porting. Deterministic automations are included in this library; “agent” does not imply autonomous model judgment.

## Observed entry points

- Schedule Trigger
- When chat message received
- When clicking ‘Execute workflow’

## Terminal nodes

- Embeddings HuggingFace Inference
- Postgres Chat Memory
- Embeddings HuggingFace Inference4
- View daily KPIs
- Create Qdrant Collection
- Write metrics
- Create METRICS table
- Upsert row(s)
- Default Data Loader2
- Recursive Character Text Splitter2
- Google Gemini Chat Model3
- Google Gemini Chat Model4
- Google Gemini Chat Model
- Google Gemini Chat Model5
- Google Gemini Chat Model6
- Default Data Loader3
- Recursive Character Text Splitter3
- Embeddings Google Gemini1
- Postgres Chat Memory1
- Google Gemini Chat Model7
- Qdrant Vector Store A
- Qdrant Vector Store B
- News Articles RAG A
- News Articles RAG B
- Embeddings Google Gemini2
- Structured Output Parser test1
- Structured Output Parser2
- Convert to File1
- HTTP Request
- OpenRouter Chat Model3
- OpenRouter Chat Model4
- OpenRouter Chat Model5
- OpenRouter Chat Model6
- Google Gemini Chat Model8
- News Articles RAG A2
- Embeddings HuggingFace Inference6
- News Articles RAG A3
- Embeddings HuggingFace Inference7
- Qdrant Vector Store
- Embeddings HuggingFace Inference8
- OpenRouter Chat Model
- Metadata structured output
- Metaprompt structured output
- RAG Agent A
- RAG Agent B

## Inputs, outputs, decisions and state

Input and output schemas are not yet established. Read the exact parameters, expressions, prompts, code, branch ports, retries, disabled nodes, and execution settings in the n8n implementation. A terminal node is a graph endpoint, not necessarily a user-facing output. Model/tool links are dependencies, not necessarily sequential control flow.

## Required access

Declared credential types: `googlePalmApi`, `huggingFaceApi`, `openRouterApi`, `postgres`, `qdrantApi`. Use local credentials or environment variables, never public exports.

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
