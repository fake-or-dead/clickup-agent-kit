---
name: codebase-design
description: Use for scoped module or interface design when ClickUp delivery planning needs ownership, dependency and testability decisions.
---

# Module and interface design

Use only code and contracts available within the user's authorized scope. Distinguish source inspection from runtime verification.

For each affected module, state its responsibility, what callers must know, hidden implementation details and owned data. Prefer an interface that hides real complexity. Include invariants, failure modes, dependencies and an observable verification point.

When alternatives matter, compare their effects on callers, ownership and tests. Record the selected option and unsettled inputs in the requested local artifact. This guidance does not implement code, require extra repository files or authorize external writes.
