# Fictional lending desk rebrief

A volunteer currently records game loans on paper. Visitors need to see which games are available without asking the desk. The confirmed first scope is a title and available-copy count. Availability equals owned copies minus active loans, and returned loans no longer reduce the count. Only desk volunteers may change loan records. Reservations and payments are explicitly excluded. A read-only visitor list is a proposed UI, because no approved design was supplied. Lost-copy handling and the production integration remain unknown.

## Supplied inputs and evidence

The [fictional task](fictional-task.json) supplies the requirement wording, two comments and two sample inventory rows. No deployed system, API contract or design has been verified. The [source receipt](source-receipt.md) is complete for this fixture only.

`GAME-A` has two available copies. `GAME-B` has zero. These numbers illustrate the supplied rule and are not production observations.

## Questions and next step

| Item | Status/owner | Impact/dependent step | Work that can proceed |
| --- | --- | --- | --- |
| Lost-copy handling | Unknown; product owner | Data adjustment and acceptance for lost items | Mock ordinary available/fully-loaned states |
| Real inventory/loan interface | Unknown; system owner | Integration and permission verification | Local contract and UI proposal |
| UI design | Proposed; product owner | Acceptance of the visitor experience | Local draft for review |

The next step is review of the local behavior/card proposal and resolution of the lost-item rule before that case is implemented. No budget or date is promised. Hours per person-day, rate and currency are unknown. No external action is authorized.
