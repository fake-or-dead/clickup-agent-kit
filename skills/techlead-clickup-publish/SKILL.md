---
name: techlead-clickup-publish
description: Publish an authorized ClickUp description update, comment or approved card set with targeted writes and read-back verification. Use after concrete content, operation and destination are known.
---

# Publish authorized ClickUp content

Read [shared policy](../techlead-analyse-clickup/references/shared-policy.md). Discover actual write/read tools; do not assume field names or supported capabilities.

## Input / authorization

Concrete reviewable content, exact target(s), operation and authorization from this session. A request to update a named description authorizes that update; reuse earlier authorization. Local analysis/rebrief alone does not authorize writes.

Prepare local content before seeking missing approval/destination. Record update-description, comment or create-cards; do not impose new PRD/spec/list approvals on an already-authorized existing-description update.

## Existing description

1. Read current task/description/metadata. Reconcile material changes since the reviewed draft before writing; do not silently overwrite newer requirements.
2. Write only the description, using markdown_description when the verified tool/API supports it or its supported equivalent. Preserve status/name/assignees/dates/estimates/relations/attachments unless separately authorized.
3. Read back and compare normalized intended content; verify unrelated fields unchanged. Inspect state before retrying ambiguous results.

## Comment / new cards

For a comment, use the authorized target/text, verify persisted content/ID and inspect existing state before ambiguous retries to avoid duplicates.

New cards require explicit approval of the concrete set, relevant contracts and destination list. Self-contained approved card contracts can satisfy specs input; separate document approvals apply only when requested. Read list/parent state, never guess destination, create only approved hierarchy/fields, verify IDs/relations/descriptions/explicit estimates and check state before partial/ambiguous retries. Convert person-days to the tool's time unit only when hours per day are explicitly supplied and estimates are authorized. If either is missing, leave the estimate field untouched.

## Receipt / stopping condition

Keep target URLs/IDs, operation, before/after evidence, content and unrelated-field checks, plus partial failures. Stop when authorized content is persisted and verified. If tools/approval prevent the write, report the exact action; do not claim publication or evade restrictions through another surface.
