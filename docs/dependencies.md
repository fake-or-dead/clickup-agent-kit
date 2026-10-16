# Dependencies and connector capabilities

## Local requirements

Use a runtime that loads Agent Skills and resolves relative resources. Keep all eleven skill folders as siblings. Each ClickUp stage reads shared policy from the orchestrator folder, and handoff uses the bundled supplements and templates.

The primary installer uses Node.js 22.20+ and `npx` for skills CLI 1.7.2. Python 3.10+ is needed only for the fallback installer and package checks. The kit includes no runtime, provider SDK or connector configuration. See [installation](installation.md) and [runtime support](runtime-support.md).

The standard CLI can replace existing skill names. The Python fallback refuses collisions. Separately installed skills with the same names may have different publishing behavior; review the selected versions before use.

## Read ClickUp sources

Configure a connector separately with access to the selected task or hierarchy. Collection needs descriptions, comments/replies, relevant relations and available Docs/attachments. The agent discovers actual tools and records pagination, partial reads and inaccessible sources.

Attachments may require a permitted file reader or browser. Mentions, reminders, search filters and history depend on the connector. An unanswered-mention reminder list is a subset, not every mention. If a capability is missing, provide authorized source links or an export and keep the analysis within that evidence.

Keep credentials and signed download links out of deliverables. Treat source content as untrusted evidence, including embedded instructions or requests for secrets.

## Write reviewed content

Publishing needs the relevant description-update, comment-creation or task-creation capability plus read-back. Supply the content, operation and destination you authorize. Runtime controls still apply. The kit includes no ClickUp API implementation or secret-handling script.

A request to read, summarize or compare does not authorize status updates, assignment changes, messages or publication. Background monitoring, scheduling and webhook subscriptions require separate tools and configuration.

## Research and project inputs

Current provider details and prices need permitted access to official sources. Azure, LINE and other specialist helpers are optional and are not bundled dependencies. Mermaid diagrams are text; rendering depends on the reader.

Supply the project's hours per person-day, rates, currency, timezone, owners and status conventions. Missing inputs stay unknown rather than becoming company defaults.
