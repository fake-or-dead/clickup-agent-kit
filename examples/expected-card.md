# DEMO-001 local developer card

Visitors can inspect game title and available-copy count using the fictional lending desk inventory.

## Work

- Draft a read-only visitor list for the supplied fixture. The UI is proposed.
- Calculate availability as owned copies minus active loans. A returned loan stops reducing the count.
- Preserve the rule that only desk volunteers change loan records. This card adds no loan-write interface.
- Keep reservations, payments and lost-item behavior outside this card's implementation scope. The product owner must decide the lost-item rule before that case proceeds.

## Inputs and outputs

Input consists of `game_code`, `title`, `owned_copies` and `active_loans` from the local fixture. Output shows title and available-copy count. `GAME-A` produces 2 and `GAME-B` produces 0.

No existing production API is claimed. A live implementation requires the system owner to supply the inventory/loan contract, authorization and data invariants first. Negative or inconsistent source counts need a proposed handling rule before production acceptance.

## Acceptance and dependencies

- The two sample rows produce the stated counts and titles.
- Visitors cannot change loan data through the proposed list.
- The card does not invent a lost-copy rule or add a reservation/payment feature.
- Mock work can proceed locally. Production integration and lost-item acceptance depend on their named owners.

Effort and price are unestimated because the integration, hours-per-day basis and rates are unavailable. The source is [fictional-task.json](fictional-task.json), with the boundary recorded in [source-receipt.md](source-receipt.md). This is a draft for review, not a live task or permission to publish.
