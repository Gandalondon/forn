# Grader test 1 (21 Nov 17:35)

Blind run of notes/GRADER.md by a separate agent on batches 9 and 10 (40 cards, shuffled, neutral refs, no verdicts). Only batch 4 to 8 examples were in the prompt.

- Agreement with Tony: 27 of 40 (68%). Target was about 9 in 10. Not ready to be the gate.
- Tony's 6 rejects: grader caught 2 (perry-statue, st-helier-alphabet), missed 4 (becontree-no-roads, clattern-goal, kew-pagoda-dragons old ending, barking-abbey).
- Tony's 34 keeps: grader rejected 9 (plath-hughes, tabard-mp, name-kingston, name-stepney, primrose-hill-tunnel, lundenwic-covent-garden, kingston-bridge-old, temple-church-round, tutankhamun-putney).
- Pattern: the grader is harsher than Tony on "so what" and history, and softer on quirky customs and vague endings. It also read "rests on a death" too widely (a grave, a wedding night).
- For comparison: cards written to the rules passed Tony at 19/20 in batch 10. As a filter, this grader would have cost 4 good batch 10 cards and kept the one dull one.
- Next if tuning: add these 13 disagreements as examples, then test on a different held-out set (batches 6 and 7), not on these 40 again.

# Grader test 2 (21 Nov 17:55)

GRADER.md tuned with the test 1 lessons, then run blind on a different set: 35 cards Tony kept in batches 6 and 7, plus cavendish-time (rejected). Examples that would leak the answers were swapped out (notes/GRADER.md holds the tuned version; the test copy used batch 9 and 10 examples instead).

- Agreement: 24 of 36 (67%). Same as test 1. Tuning didn't move it.
- It caught the one reject, but rejected 11 of 35 keeps, mostly as "Confusing" or "Dull" (tube boring machines named by schoolchildren, Marmite factory hostel, Franklin's chess, Olympic McDonald's as a "restaurant").
- Some of its notes are good edits, not good verdicts: Norway's tree should say it's a wartime thank-you; the Leaning Tower card never says why it leans; the Crooked Billet card just repeats the line.

## Conclusion
- The grader is about 2 in 3 with Tony, twice, before and after tuning. It's much stricter than Tony. Not usable as a gate.
- The gate is the writing rules (batch 10: 19/20 with Tony) plus Tony's night review when a new area opens.
- Keep GRADER.md as an optional editor pass: its notes can point at weak endings or missing "why" before a batch goes out. It never drops a card on its own.
