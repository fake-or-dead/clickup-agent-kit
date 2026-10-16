---
name: techlead-clickup-feasibility
description: Assess technical approaches, infrastructure, actual implementation/preparation work, stakeholder MD and one-time/recurring costs. Use for proper Tech Feas and conditional build-versus-buy recommendations.
---

# Technical feasibility

Read [shared policy](../techlead-analyse-clickup/references/shared-policy.md) and [feasibility template](../techlead-analyse-clickup/references/feasibility-template.md). Read [stakeholder summary template](../techlead-analyse-clickup/references/stakeholder-comment-template.md) only for a stakeholder-comment request.

## Input

Current understanding, source receipt, available samples/contracts, scope, owners and current project constraints/rate. Reuse a valid rebrief; [rebrief](../techlead-clickup-rebrief/SKILL.md) missing business understanding. Weak evidence permits assumption-based options/POC, not production guarantees.

## Work

1. State feasible now, feasible with conditions or blocked for named scope. Separate demoable behavior from acceptance with actual data.
2. Describe systems/APIs/data/permissions/jobs/UI and useful diagrams. Compare custom/SaaS/hybrid only when relevant or requested. Use available architecture guidance or the bundled domain-modeling supplement for the specific design depth needed, through [handoff compatibility](../techlead-clickup-handoff/references/skill-compatibility.md); do not duplicate generic design methods or implement code during a planning request.
3. For each material feature show required input, Dev implementation, non-Dev preparation/human proof, output, acceptance and gaps. SaaS still needs configuration/integration/tuning/data work.
4. Assign source preparation to actual system owners. Separate company/client, Dev/non-Dev, setup/recurring and included/excluded. Shared work counts once, not per requirement; ownership changes transfer MD.
5. Give workstream MD ranges/basis. Person-days differ from calendar duration/wait time. Name inputs that narrow the range.
6. Paid-service estimates need usage units/assumptions, current official price/date/links, servers/tools/backups/monitoring, backfill/setup, human review/maintenance and total cost. Separate allowances/reserve/FX/tax/markup and existing fees. Do not apply company rates to client effort automatically.
7. Map risks/unknowns to owners and affected steps. Include POC/acceptance evidence, release/Ops prerequisites and unverified expectations.

For logic-heavy work, estimate the safe implementation: normalization, indexed/low-cost lookup, relevant validation/error handling and enough observability to diagnose failures. Do not assume fragile shortcuts in the baseline.

## AI/data analysis

Include taxonomy/definitions, representative samples, human truth set, peer review/adjudication, development/holdout separation, tuning/evaluation and ongoing review, with owner/MD separate from API charges. Map source messages/events to the real analysis unit before estimating calls/workflow executions. Measure tokens/reruns/throughput/reviewer minutes in POC; confidence is not measured accuracy or calibrated probability.

## Output / check

Proper standalone Feasibility.md or requested HTML, containing approach/architecture, feature feasibility, actual work/data/owners, stakeholder MD, costs, risks, scoped dependencies and acceptance. A request for a separate Tech Feas gets a separate readable file, not an embedded MD-only section.

Reconcile totals/transfers; label included POC/backfill to avoid double charging. Return a concise recommendation in the requested language with material assumptions. Publishing is a separate route.
