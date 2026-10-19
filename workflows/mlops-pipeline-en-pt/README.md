# MLOps Pipeline EN-PT

This folder contains the **MLOps Pipeline EN-PT** workflow. Its executable nodes use `code`, `errorTrigger`, `executeCommand`, `httpRequest`, `if`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mlops-pipeline-en-pt.json`](mlops-pipeline-en-pt.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook - Iniciar Pipeline, Error Trigger - Capturar Falhas

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook - Iniciar Pipeline | `webhook` | Inspect parameters |
| Preparar Parametros | `set` | Inspect parameters |
| Validar Parametros | `code` | Inspect parameters |
| Preparar Dados - Container | `executeCommand` | Inspect parameters |
| Treinar Modelo - Container | `executeCommand` | Inspect parameters |
| Extrair Run ID e Metricas | `code` | Inspect parameters |
| Validar Threshold de Qualidade | `if` | Inspect parameters |
| Publicar Artefatos - Container | `executeCommand` | Inspect parameters |
| Consolidar Publicacao | `code` | Inspect parameters |
| Recarregar Modelo Publicado | `httpRequest` | POST |
| Resposta - Sucesso | `code` | Inspect parameters |
| Resposta - Modelo Rejeitado | `code` | Inspect parameters |
| Error Trigger - Capturar Falhas | `errorTrigger` | Inspect parameters |
| Registrar Incidente | `code` | Inspect parameters |
| Verificar Backend de Artefatos | `if` | Inspect parameters |
| Resposta - Publicacao Local | `code` | Inspect parameters |

## Connection map

- Webhook - Iniciar Pipeline → Preparar Parametros (`main`, output 0, input 0)
- Preparar Parametros → Validar Parametros (`main`, output 0, input 0)
- Validar Parametros → Preparar Dados - Container (`main`, output 0, input 0)
- Preparar Dados - Container → Treinar Modelo - Container (`main`, output 0, input 0)
- Treinar Modelo - Container → Extrair Run ID e Metricas (`main`, output 0, input 0)
- Extrair Run ID e Metricas → Validar Threshold de Qualidade (`main`, output 0, input 0)
- Validar Threshold de Qualidade → Publicar Artefatos - Container (`main`, output 0, input 0)
- Validar Threshold de Qualidade → Resposta - Modelo Rejeitado (`main`, output 1, input 0)
- Publicar Artefatos - Container → Consolidar Publicacao (`main`, output 0, input 0)
- Consolidar Publicacao → Verificar Backend de Artefatos (`main`, output 0, input 0)
- Recarregar Modelo Publicado → Resposta - Sucesso (`main`, output 0, input 0)
- Error Trigger - Capturar Falhas → Registrar Incidente (`main`, output 0, input 0)
- Verificar Backend de Artefatos → Resposta - Publicacao Local (`main`, output 0, input 0)
- Verificar Backend de Artefatos → Recarregar Modelo Publicado (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/giuliazc/mlops-neural-machine-translation/blob/e071531509a02b27d5b3b4dd9ae718c8d1377478/n8n.json](https://github.com/giuliazc/mlops-neural-machine-translation/blob/e071531509a02b27d5b3b4dd9ae718c8d1377478/n8n.json). License: **MIT**; preserve [the notice](../../licenses/giuliazc--mlops-neural-machine-translation.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
