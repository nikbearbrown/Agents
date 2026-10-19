# [n8n] Advanced URL Parsing and Shortening Workflow - Switchy.io Integration

This folder contains the **[n8n] Advanced URL Parsing and Shortening Workflow - Switchy.io Integration** workflow. Its executable nodes use `aggregate`, `convertToFile`, `formTrigger`, `github`, `html`, `httpRequest`, `if`, `respondToWebhook`, `set`, `splitInBatches`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-advanced-url-parsing-and-shortening-workflow-switchy-io-integration.json`](n8n-advanced-url-parsing-and-shortening-workflow-switchy-io-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split In Batches | `splitInBatches` | Inspect parameters |
| Get Headers | `httpRequest` | Inspect parameters |
| OpenGraph API | `httpRequest` | Inspect parameters |
| Meta tags Scraper - dub.sh | `httpRequest` | Inspect parameters |
| IF OpenGraph invaild | `if` | Inspect parameters |
| Parse headers | `html` | extractHtmlContent |
| If - Enable ScreenShots (yes to enable) | `if` | Inspect parameters |
| API Auth | `set` | Inspect parameters |
| Method 1 - META | `set` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Final Data | `set` | Inspect parameters |
| CREATE | `httpRequest` | POST |
| UPDATE | `httpRequest` | PUT |
| IF Slug available | `if` | Inspect parameters |
| Final Meta | `aggregate` | Inspect parameters |
| Host Screenshot | `github` | file |
| Host OGImage | `github` | file |
| Host Favicon | `github` | file |
| Edit Fields | `set` | Inspect parameters |
| Download final OG | `httpRequest` | Inspect parameters |
| Download Favicon | `httpRequest` | Inspect parameters |
| Method 2 - META | `set` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Method 3 - META1 | `set` | Inspect parameters |
| Method 1 - SCR | `httpRequest` | Inspect parameters |
| Method 2 - SCR | `httpRequest` | POST |
| Final SCR | `aggregate` | Inspect parameters |
| Stop And Error | `stopAndError` | Inspect parameters |
| Shortened URL | `set` | Inspect parameters |
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Scan URL (Community) | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Check Reviews (Community) | `httpRequest` | Inspect parameters |
| Norton | `set` | Inspect parameters |
| bitdefender | `set` | Inspect parameters |
| HTML | `html` | extractHtmlContent |
| (Fraud Check) | `httpRequest` | POST |
| (Others) | `httpRequest` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| set unsafe | `set` | Inspect parameters |
| If3 | `if` | Inspect parameters |
| PhishTank | `httpRequest` | Inspect parameters |
| IF GH invaild | `if` | Inspect parameters |
| Method 4 - META | `set` | Inspect parameters |
| IF dub invaild | `if` | Inspect parameters |

## Connection map

- If → PhishTank (`main`, output 0, input 0)
- If → If1 (`main`, output 1, input 0)
- If1 → Check Reviews (Community) (`main`, output 0, input 0)
- If1 → Norton (`main`, output 1, input 0)
- If2 → OpenGraph API (`main`, output 0, input 0)
- If2 → set unsafe (`main`, output 1, input 0)
- If3 → Scan URL (Community) (`main`, output 0, input 0)
- If3 → OpenGraph API (`main`, output 1, input 0)
- HTML → bitdefender (`main`, output 0, input 0)
- CREATE → IF Slug available (`main`, output 0, input 0)
- Norton → PhishTank (`main`, output 0, input 0)
- UPDATE → Shortened URL (`main`, output 0, input 0)
- (Others) → HTML (`main`, output 0, input 0)
- API Auth → If3 (`main`, output 0, input 0)
- Final SCR → Host Screenshot (`main`, output 0, input 0)
- PhishTank → (Fraud Check) (`main`, output 0, input 0)
- Final Data → CREATE (`main`, output 0, input 0)
- Final Meta → If - Enable ScreenShots (yes to enable) (`main`, output 0, input 0)
- set unsafe → Split In Batches (`main`, output 0, input 0)
- Edit Fields → Download final OG (`main`, output 0, input 0)
- Get Headers → Parse headers (`main`, output 0, input 0)
- Get Headers → Meta tags Scraper - dub.sh (`main`, output 1, input 0)
- bitdefender → If2 (`main`, output 0, input 0)
- Host Favicon → Final Data (`main`, output 0, input 0)
- Host OGImage → Download Favicon (`main`, output 0, input 0)
- (Fraud Check) → (Others) (`main`, output 0, input 0)
- IF GH invaild → Meta tags Scraper - dub.sh (`main`, output 0, input 0)
- IF GH invaild → Final Meta (`main`, output 1, input 0)
- OpenGraph API → IF OpenGraph invaild (`main`, output 0, input 0)
- OpenGraph API → Get Headers (`main`, output 1, input 0)
- Parse headers → Method 2 - META (`main`, output 0, input 0)
- Shortened URL → Split In Batches (`main`, output 0, input 0)
- IF dub invaild → Method 4 - META (`main`, output 0, input 0)
- IF dub invaild → Method 3 - META1 (`main`, output 1, input 0)
- Method 1 - SCR → Final SCR (`main`, output 0, input 0)
- Method 1 - SCR → Method 2 - SCR (`main`, output 1, input 0)
- Method 2 - SCR → Convert to File (`main`, output 0, input 0)
- Method 2 - SCR → Stop And Error (`main`, output 1, input 0)
- Convert to File → Final SCR (`main`, output 0, input 0)
- Host Screenshot → Edit Fields (`main`, output 0, input 0)
- Method 1 - META → Final Meta (`main`, output 0, input 0)
- Method 2 - META → IF GH invaild (`main`, output 0, input 0)
- Method 4 - META → Final Meta (`main`, output 0, input 0)
- Download Favicon → Host Favicon (`main`, output 0, input 0)
- Method 3 - META1 → Final Meta (`main`, output 0, input 0)
- Split In Batches → API Auth (`main`, output 0, input 0)
- Split In Batches → Respond to Webhook (`main`, output 1, input 0)
- n8n Form Trigger → Split In Batches (`main`, output 0, input 0)
- Download final OG → Host OGImage (`main`, output 0, input 0)
- IF Slug available → Shortened URL (`main`, output 0, input 0)
- IF Slug available → UPDATE (`main`, output 1, input 0)
- IF OpenGraph invaild → Method 1 - META (`main`, output 0, input 0)
- IF OpenGraph invaild → Get Headers (`main`, output 1, input 0)
- Scan URL (Community) → If (`main`, output 0, input 0)
- Check Reviews (Community) → Norton (`main`, output 0, input 0)
- Meta tags Scraper - dub.sh → IF dub invaild (`main`, output 0, input 0)
- Meta tags Scraper - dub.sh → Stop and Error (`main`, output 1, input 0)
- If - Enable ScreenShots (yes to enable) → Method 1 - SCR (`main`, output 0, input 0)
- If - Enable ScreenShots (yes to enable) → Edit Fields (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0392_Stopanderror_GitHub_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0392_Stopanderror_GitHub_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
