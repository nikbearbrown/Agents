# Annotation policy

Every included workflow has a locally generated overview sticky note derived from its node metadata, entry points, and license evidence. No model is used for this pass, and adding the note is checked not to alter the sanitized executable nodes or connections.

The official [Auto-generate sticky notes and rename nodes](https://n8n.io/workflows/13868-auto-generate-sticky-notes-and-rename-nodes/) template is a possible second pass. It requires OpenAI credentials and sends workflow context to the configured model. Do not send unsanitized workflows. Use copies and an explicit spending budget.

Keep `renameNodes=false`: the downloaded renamer does not cover every legacy expression format and may cascade names. Require exact equality of executable node IDs, names, types, versions, parameters, execution settings and connections; allow only note/layout edits. Review generated claims and the rendered canvas, then repeat meaningful execution tests. Pilot three workflows before a batch. The official tool is linked, not bundled, because its redistribution license has not been established.
