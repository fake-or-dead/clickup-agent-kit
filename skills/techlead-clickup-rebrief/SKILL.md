---
name: techlead-clickup-rebrief
description: Summarize client goals, supplied inputs, scope and missing information from collected evidence, with BA concerns and diagrams. Use before solution design or when the original brief is hard to understand.
---

# Rebrief the client request

Read [shared policy](../techlead-analyse-clickup/references/shared-policy.md) and [rebrief template](references/rebrief-template.md).

## Input

Source contents/read receipt, user context, decisions and existing overview. Use [collect](../techlead-clickup-collect/SKILL.md) for unread essential sources, or disclose the boundary.

## Work

- Open with 5–8 plain-language lines: who has what problem today, what outcome the client wants, who uses it, main journey, evidence-backed scope, proposed additions and important limitations. Use a concrete example and explain project terms; do not paste the source brief or a stack list.
- Summarize what the client supplied and what each item confirms. Separate documents, real samples/data, designs, claimed APIs/access and actual source/runtime verification.
- Show current vs expected behavior. Label Confirmed / Proposed / Assumed / Unknown with source or owner.
- Select 3–5 highest-impact BA gaps for the overview, with impact, required evidence/decision, owner and dependent step. Put additional detail in the reference fold.
- Choose concerns by domain: business rules/permissions/lifecycle, integrations/data quality, migration, money/refunds, reporting, privacy, AI proof or operations. Offer useful defaults/options with rationale; proposals are not client approval.
- Add user-journey/system-context/data-flow diagrams when useful. Add proposed infrastructure when hosting/storage/security/capacity affects the solution. Label verified current facts separately from proposed/unknown topology. With weak technical inputs, draw logical components and mark hosting/runtime unknown.
- For overloaded business terms, use the available domain-modeling skill selectively to clarify meaning. Do not force a codebase glossary/ADR in a collection-only task.

## Output / check

One independently readable rebrief.md, existing brief.md or requested self-contained HTML. Keep evidence local and requirement references on ClickUp. Show next steps and scoped readiness, not a final budget/date or development approval.

Check that opening lines explain the client outcome, supplied inputs have evidence, material gaps have owner/impact and diagrams do not present proposals as deployment facts. Update current understanding when evidence or decisions change.
