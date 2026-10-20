# Agents migration — 20 October 2026

This is the first structural migration, not a claim that every alternative implementation is finished.

## Scope

- 1,877 agent packages: 1,876 collected workflow families and the existing Lectern job-search package.
- All 1,876 collected n8n JSON files retain their exact SHA-256 hashes. Lectern's five JSON files also retain their hashes.
- Each agent has a shared specification, a Mermaid file, provenance-aware n8n setup, five alternative implementation plans, and five assistant prompt files with separate build/operate sections.
- Source-derived specifications are drafts. The plans contain no executable Python, Pydantic AI, CrewAI Flow, CrewAI Crew or LangGraph port. The prompts have not been execution-tested.
- Historical Lectern fixture reports are preserved, with their original scope; they were not rerun for this migration.

## Verification performed

| Check | Result | What it establishes |
|---|---|---|
| `python3 scripts/validate.py` | 1,876 passed | Existing publication checks, including required metadata and sanitized workflow structure |
| `python3 scripts/validate_agents.py` | 1,877 passed | Package structure, labels, prompt sections, local links, graph counts, and unchanged JSON hashes |
| Mermaid 12.2.0 parser | 1,877 parsed, 0 failures | Diagram syntax; not workflow correctness or runtime execution |
| Gitleaks scan of public collection | 0 detected secrets | Pattern-based scan only; no guarantee against every possible sensitive value |
| Website production build | Passed | Isolated release built from the existing website commit plus only Agents changes |

Website type checking still reports pre-existing errors in blog, sitemap, Substack and tools pages; no errors were reported in the new Agents files. The site retains its existing build configuration. Browser review covered search ranking, implementation labels, small and large Mermaid diagrams, and the retained n8n inspector. Source availability is not runtime verification.

## Source graph findings

These pre-existing issues are exposed, not silently repaired. A Mermaid diagram contains only connections whose endpoints can be resolved. Duplicate names can make interpretation ambiguous. Read the original JSON before attempting a port.

### [receive-mqtt-message-from-ikea-5-button-switch-and-route-actions](agents/receive-mqtt-message-from-ikea-5-button-switch-and-route-actions/specification.md)

- Unresolved connection: MQTT Trigger - Ikea Remote Switch -> Globals

### [receive-notion-events-and-webhook-and-update-database-page-notion](agents/receive-notion-events-and-webhook-and-update-database-page-notion/specification.md)

- Duplicate executable node names need review.

### [seo-blog-generator-with-gpt-4o-perplexity-and-telegram-integration](agents/seo-blog-generator-with-gpt-4o-perplexity-and-telegram-integration/specification.md)

- Unresolved connection: AI Agent -> Copywriter AI Agent
- Unresolved connection: gpt-4o-mini -> Copywriter AI Agent
- Unresolved connection: Simple Memory1 -> Create Title, Slug, Meta
- Unresolved connection: OpenAI Chat Model -> Create Title, Slug, Meta
- Unresolved connection: Copywriter AI Agent -> Create Title, Slug, Meta
- Unresolved connection: Copywriter AI Agent -> AI Agent1
- Unresolved connection: Call n8n Workflow Tool -> AI Agent
- Unresolved connection: Create Title, Slug, Meta -> Merge
- Unresolved connection: Structured Output Parser -> Create Title, Slug, Meta
- Unresolved connection: Structured Output Parser1 -> AI Agent1

### [academic-assistant-chatbot-telegram-openai](agents/academic-assistant-chatbot-telegram-openai/specification.md)

- Unresolved connection: 20a2d959-5412-447b-a2c4-7736b6b758b3 -> error-handler-20a2d959-5412-447b-a2c4-7736b6b758b3-d3388f15
- Unresolved connection: 8b30f207-8204-4548-8f51-38c387d98ae9 -> error-handler-8b30f207-8204-4548-8f51-38c387d98ae9-061eba47
- Unresolved connection: 15bb5fd5-7dfe-4da9-830c-e1d905831640 -> error-handler-15bb5fd5-7dfe-4da9-830c-e1d905831640-68c06fa7

### [puq-docker-nextcloud-deploy](agents/puq-docker-nextcloud-deploy/specification.md)

- Duplicate executable node names need review.
- Unresolved connection: d01-test.uuq.pl -> Code
- Unresolved connection: d01-test.uuq.pl -> Code
- Unresolved connection: d02-test.uuq.pl -> Code
- Unresolved connection: d02-test.uuq.pl -> Code

### [threads](agents/threads/specification.md)

- Unresolved connection: Form Trigger -> Set Fields
- Unresolved connection: Set Fields -> Exchange Token

### [workflow-n8n-d-auto-post-sur-les-reseaux-sociaux-vide](agents/workflow-n8n-d-auto-post-sur-les-reseaux-sociaux-vide/specification.md)

- Unresolved connection: Upload Video to Blotato -> TWITTER

### [retry-execution-hourly](agents/retry-execution-hourly/specification.md)

- Unresolved connection: execution_id -> retry workflow automatically
- Unresolved connection: Loop Over Items -> execution_id

### [get-elastic-alert-and-send-email-notification-and-receive-schedule-events](agents/get-elastic-alert-and-send-email-notification-and-receive-schedule-events/specification.md)

- Unresolved connection: Schedule Trigger -> Get PRISM Elastic Alert
- Unresolved connection: Get PRISM Elastic Alert -> Response is not empty

### [outlook](agents/outlook/specification.md)

- Unresolved connection: Draft a Reply [optional] -> Add AI Agent Instructions

## Compatibility

Old repository links use GitHub's repository redirect after the rename from N8N to Agents. Do not recreate a repository with the old name. Old workflow README paths remain landing pages. Raw JSON paths within GitHub moved; `migration.json` records every move and the original commit so old source files can be recovered. Existing website n8n detail and JSON download URLs remain available.

## Next implementation work

Review meaningful titles and purposes first, particularly entries whose inherited names describe setup instructions. Define concrete input/output contracts and synthetic fixtures before porting. Build and test representative Python ports, then add frameworks where they contribute useful behavior. Promote an implementation's status only with dated, scoped execution evidence. Preserve source licenses and attribution for each port.
