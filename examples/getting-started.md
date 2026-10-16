# Make an offline rebrief and card

This example concerns a fictional volunteer lending desk. It contains no live ClickUp URLs, user IDs, workspace IDs or customer data. `DEMO-001` is a fixture identifier, not a valid ClickUp task. All people are role labels.

1. Read [the fictional task](fictional-task.json) and [source receipt](source-receipt.md).
2. In a runtime that has loaded the kit, use the following prompt. Choose a local output directory you can write to.

```text
Use $techlead-analyse-clickup. Work offline using examples/fictional-task.json
and examples/source-receipt.md only. Treat DEMO-001 as fictional.
Prepare a concise English rebrief and one self-contained developer card in
the local directory I choose. Do not connect to ClickUp, browse, publish,
send messages, implement code or change account configuration.
Hours per person-day, currency and rates have not been supplied.
```

3. Compare the result with [the illustrative rebrief](expected-rebrief.md) and [card](expected-card.md). Wording can differ. Check that the result retains the pending lost-item rule, labels the proposed UI, limits scope to local evidence and avoids numeric cost/effort conversion.

The expected files are hand-prepared examples, not a recorded model evaluation. The installer and validator do not execute a model or call ClickUp. You can inspect these files without installing anything.
