---
name: techlead-clickup-handoff
description: Adapt existing PRD, architecture and issue-planning skills into local ClickUp specs and compact developer cards. Use for delivery handoff requiring self-contained contracts, BE/FE scope and per-card gap ownership.
---

# Delivery handoff through existing skills

Read [shared policy](../techlead-analyse-clickup/references/shared-policy.md) and [skill compatibility](references/skill-compatibility.md). For compact cards read [card template](references/compact-card-template.md). Read the bundled [specs](../techlead-analyse-clickup/references/specs-template.md) or [backlog](../techlead-analyse-clickup/references/tasks-template.md) templates only when their output is requested.

## Input / reuse

Use current understanding, scoped behavior, source URLs, decisions, available contracts and estimates. Existing complete source cards can supply these without generating PRD/specs documents. Use [feasibility](../techlead-clickup-feasibility/SKILL.md) only when approach/effort is unresolved.

Choose compatible existing skills rather than reimplementing PRD/specs/planning workflows. The compatibility reference defines local scope, output-shape and external-write boundaries. Respect explicit-only invocation metadata; reuse their documented templates/methods without treating that as permission to run the full workflow.

## ClickUp-specific output

- Use the requested language and granularity. Backend/frontend cards are an option when requested, not a fixed team structure. Include QA notes when relevant.
- Open with task ID/name, one outcome sentence and concrete action bullets. Include inputs/outputs, relevant rules/permissions, observable acceptance and complete relevant contracts inside each card.
- Title proposed contracts exactly "propose API contracts". Split each endpoint into METHOD/path, purpose, source/actions/verification, request, response and separate error-code blocks. Existing verified contracts retain their status; do not invent endpoints as current APIs.
- Give a short example/required-input list, roughly 10–20 lines where practical; preserve correctness when complex contracts need more.
- Questions go at the end of the affected card with impact, owner and dependent step. Separate missing evidence from proposed business decisions. Settled routine technical choices are not new approvals.
- Requirement references use actual ClickUp URLs. Do not require a reader to open another card or local spec to understand the contract.
- Count shared work once; show each card's estimate/dependencies without hiding non-Dev or client preparation from the project effort.
- Write only the requested local PRD/specs/tasks/card draft. Do not auto-publish, set ready-for-agent labels or implement code.

## Check / handoff

Check source traceability, consistent examples/contracts, independent readability, relevant gaps and requested granularity. Local ready-for-review is not automatic ready-for-development. Pass concrete approved content to [publish](../techlead-clickup-publish/SKILL.md) only when authorized.
