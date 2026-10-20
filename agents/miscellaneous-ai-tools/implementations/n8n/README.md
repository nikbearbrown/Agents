# MISCELLANEOUS AI TOOLS

This folder contains the **MISCELLANEOUS AI TOOLS** workflow. Its executable nodes use `agent`, `aggregate`, `aiTransform`, `bitly`, `bluesky`, `calendlyTrigger`, `chainLlm`, `chainRetrievalQa`, `chainSummarization`, `chatTrigger`, `code`, `convertToFile`, `dateTime`, `documentDefaultDataLoader`, `dropbox`, `elevenLabs`, `emailReadImap`, `emailSendTool`, `embeddingsGoogleGemini`, `embeddingsOpenAi`, `executeCommand`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `extractFromFile`, `filter`, `formTrigger`, `ftp`, `gmail`, `gmailTool`, `gmailTrigger`, `googleCalendar`, `googleCalendarTool`, `googleDocs`, `googleDocsTool`, `googleDriveTrigger`, `googleSheets`, `googleSheetsTool`, `googleSheetsTrigger`, `gumroadTrigger`, `html`, `httpRequest`, `if`, `informationExtractor`, `limit`, `lmChatAnthropic`, `lmChatGoogleGemini`, `lmChatOpenAi`, `localFileTrigger`, `manualTrigger`, `markdown`, `mcpClientTool`, `memoryBufferWindow`, `memoryManager`, `memoryPostgresChat`, `memoryRedisChat`, `merge`, `noOp`, `openAi`, `outputParserAutofixing`, `outputParserItemList`, `outputParserStructured`, `perplexity`, `postgresTool`, `pushbullet`, `reddit`, `redisTool`, `removeDuplicates`, `renameKeys`, `respondToWebhook`, `rssFeedRead`, `scheduleTrigger`, `sentimentAnalysis`, `set`, `sort`, `splitInBatches`, `splitOut`, `summarize`, `textClassifier`, `toolCalculator`, `toolCode`, `toolHttpRequest`, `toolSerpApi`, `toolVectorStore`, `toolWikipedia`, `toolWolframAlpha`, `toolWorkflow`, `twitter`, `vectorStoreInMemory`, `vectorStorePGVector`, `vectorStorePinecone`, `vectorStoreSupabase`, `wait`, `webhook`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`miscellaneous-ai-tools.json`](miscellaneous-ai-tools.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropboxOAuth2Api`, `elevenLabsApi`, `googleCalendarOAuth2Api`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`, `serpApi`

**Entry nodes:** Gmail Trigger App, Google Sheets Trigger App, Calendly Trigger, Google Drive Trigger, Gumroad Trigger, Local File Trigger, On form submission, Schedule Trigger, Webhook, When chat message received, When clicking 'Test workflow', Workflow Input Trigger, Gmail Trigger, Google Sheets Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Information Extractor | `informationExtractor` | Inspect parameters |
| Question and Answer Chain | `chainRetrievalQa` | Inspect parameters |
| Sentiment Analysis | `sentimentAnalysis` | Inspect parameters |
| Summarization Chain | `chainSummarization` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| Chat Memory Manager | `memoryManager` | Inspect parameters |
| Bitly App | `bitly` | Inspect parameters |
| Dropbox App | `dropbox` | download |
| Gmail App | `gmail` | Inspect parameters |
| Google Calendar App | `googleCalendar` | Inspect parameters |
| Google Docs App | `googleDocs` | get |
| Google Sheets App | `googleSheets` | append |
| Pushbullet App | `pushbullet` | Inspect parameters |
| YouTube App | `youTube` | playlist / create |
| Bluesky App | `bluesky` | Inspect parameters |
| Perplexity App | `perplexity` | Inspect parameters |
| ElevenLabs App | `elevenLabs` | Inspect parameters |
| Reddit App | `reddit` | Inspect parameters |
| Gmail Trigger App | `gmailTrigger` | Inspect parameters |
| Google Sheets Trigger App | `googleSheetsTrigger` | Inspect parameters |
| Call n8n Workflow Tool | `toolWorkflow` | Inspect parameters |
| Code Tool | `toolCode` | Inspect parameters |
| HTTP Request1 | `toolHttpRequest` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Postgres | `postgresTool` | Inspect parameters |
| Redis | `redisTool` | Inspect parameters |
| Send Email | `emailSendTool` | Inspect parameters |
| SerpAPI | `toolSerpApi` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Wolfram Alpha | `toolWolframAlpha` | Inspect parameters |
| gmailTool App | `gmailTool` | Inspect parameters |
| googleCalendarTool App | `googleCalendarTool` | Inspect parameters |
| googleDocsTool App | `googleDocsTool` | Inspect parameters |
| googleSheetsTool App | `googleSheetsTool` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Answer questions with a vector store | `toolVectorStore` | Inspect parameters |
| In-Memory Vector Store | `vectorStoreInMemory` | Inspect parameters |
| Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Postgres PGVector Store | `vectorStorePGVector` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Redis Chat Memory | `memoryRedisChat` | Inspect parameters |
| Item List Output Parser | `outputParserItemList` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| X | `twitter` | Inspect parameters |
| Calendly Trigger | `calendlyTrigger` | Inspect parameters |
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| Gumroad Trigger | `gumroadTrigger` | Inspect parameters |
| Local File Trigger | `localFileTrigger` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| When clicking 'Test workflow' | `manualTrigger` | Inspect parameters |
| Workflow Input Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Date & Time | `dateTime` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Summarize | `summarize` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Extract from File | `extractFromFile` | pdf |
| HTML | `html` | extractHtmlContent |
| Markdown | `markdown` | Inspect parameters |
| Rename Keys | `renameKeys` | Inspect parameters |
| Sort | `sort` | Inspect parameters |
| If | `if` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Replace Me | `noOp` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Execute Command | `executeCommand` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| FTP | `ftp` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| RSS Read | `rssFeedRead` | Inspect parameters |
| AI Transform | `aiTransform` | Inspect parameters |
| MCP Client | `mcpClientTool` | Inspect parameters |

## Connection map

- Replace Me → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Replace Me (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Bitly/0910_Bitly_Datetime_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Bitly/0910_Bitly_Datetime_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
