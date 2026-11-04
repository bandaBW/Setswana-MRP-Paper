# Release approval checklist (review before making GitHub public)

The result CSVs in this package contain **original Setswana message texts and gold annotation spans**, not only numeric summary statistics. Such text can contain sensitive, offensive, or identifying details even if anonymised previously. Do not treat the absence of an email/URL as evidence that a message is non-identifying.

- [ ] Verify permission/licence to redistribute each source text and annotations from the FSIR dataset.
- [ ] Review direct and indirect identifiers, names, handles, message links, phone numbers, institutions, locations and cross-platform quotations.
- [ ] Verify that the applicable institutional ethical/data-sharing requirements allow public release.
- [ ] Decide whether textual CSVs should be public, access-controlled, or replaced with numeric-only summaries.
- [ ] Confirm consent/rights for any human annotation guidelines and associated files.
- [ ] Check notebook source and Git history for tokens, passwords, temporary URLs and participant data.
- [ ] Review and resolve known whitespace/span inconsistencies and document them without silently altering archived results.
- [ ] Add exact package versions, environment and checkpoint identifiers.
- [ ] Resolve published 977 vs experimental 976 total.
- [ ] Make repository public only after all checks and author approvals.

Run `python scripts/audit_release.py` for an initial automated signal scan. It is **not** a substitute for human review.
