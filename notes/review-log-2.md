# Forn review log, part 2 (continues notes/review-log.md)

## Batch 8 (21 Nov 17:03 to 17:06): London place names
- 16 kept, 4 rejected (20%): right on the 1 in 5 bar.
- Kept: name-kew, name-richmond, name-surbiton, name-soho, name-bermondsey, name-southwark, name-lambeth, name-brixton, name-greenwich, name-ealing, name-acton, name-brentford, name-islington, name-wandsworth, name-camden-town, name-bayswater.
- Rejected, all Confusing:
  - name-kingston: "No idea what cyninges is."
  - name-knightsbridge: "Two facts? Not sure what cniht is."
  - name-stepney: "No idea what ratcliff is and I lived in Stepney."
  - name-vauxhall: "Notification explains it better than app."
- New writing rule: don't quote old or foreign words (cyninges, cniht, Stybbanhyð). Give the meaning in plain modern English. Don't name a place most locals wouldn't know (Ratcliff). The card must explain the notification's fact at least as clearly as the notification does.
- All 4 rewritten in content/facts/london-names-batch8.json.

## Batch 9 (21 Nov 17:07): on "Forn Review", waiting for Tony
- Version 1795280841-4d28; answers in review-batch-9.
- The 4 batch 8 rewrites; the 9 SW20 one-fact rewrites (content/facts/sw20-merton-onefact.json); clattern-goal; 6 spares (primrose-hill-tunnel, becontree-no-roads, boulogne-mouth with a new line and card, minchenden-oak with "oak tree" in the line, kew-pagoda-dragons, plath-hughes).
- The boulogne-mouth and minchenden-oak changes were made on the page and here only; carry them into london-dyk-batch4.json at the push.
- Left unreviewed: kings-cross-1863.
- 21 Nov 17:25: still no answers in review-batch-9.

## Batch 10 (built 21 Nov evening): older London, pre-1500, NOT yet on the page
- Tony allowed british-history.ac.uk (BHO) on 21 Nov. 17 of 20 from BHO (Old and New London, VCH, Survey of London, RCHME, Lysons, Stow); guildhall-arena from London Museum and Wikipedia; lundenwic and mithras from Wikipedia.
- Files: content/facts/london-old-batch10.json (20), sources-london-old-batch10.json (source sentences per id; BHO isn't reachable from the shell, so the text is the quoted passages, not whole pages), fact-tags-batch10.json (merge into fact-tags.json at the push).
- Eras: 1 roman-era Guildhall, 1 Mithras, 4 saxon (Lundenwic, Thorney, Barking, Harrow), 14 medieval. Before this, pre-1500 was 9 of 112.
- Ids: barts-jester, tower-white-bear, moorfields-bone-skates, bow-bridge, harrow-temple, clerkenwell-plays, temple-church-round, guildhall-arena, crosby-hall-moved, barking-abbey, tabard-mp, thorney-island, kingston-bridge-old, eltham-barn, cheapside-joust, bedlam-liverpool-st, caxton-almonry, london-bridge-chapel, lundenwic-covent-garden, mithras-returned.
- Checked: every card 35 words or under; every number and name checked against the source sentences (only page-title names and "around 1110" from "between 1100 and 1118" flagged).
- Left out on purpose (rule 3 or weak): Savoy burning 1381 (crime, a death), London Stone and Jack Cade (rebellion), Old St Paul's spire height (sources disagree), Westminster Hall roof ("why does it matter").
- Spares if needed: tower-elephant-1255 (same spot as the bear), smithfield-smooth-field (next to Barts), queen's stand collapsing at the 1330 Cheapside joust.
- Published 21 Nov 17:17 as its own page, "Forn Review, batch 10" (slug 86c193dc-3973-419f-a095-6d36a37da44b, https://claude.ai/artifact/He8rUCU2stSdA9SN3AZCmx). Answers go in collection review-batch-10 on THAT artifact, not on "Forn Review".

## Batch 9 results (21 Nov 17:18 to 17:21)
- 15 kept, 5 rejected (25%).
- Kept: name-kingston, name-knightsbridge, name-stepney, name-vauxhall (all 4 batch 8 rewrites pass), caesars-camp, hartley-fireproof, putney-duel, tutankhamun-putney, old-rectory, selassie-cannizaro, snuff-mills, primrose-hill-tunnel, boulogne-mouth, minchenden-oak, plath-hughes.
- Rejected:
  - perry-statue, Confusing: "Bit obscure still" (second reject).
  - st-helier-alphabet, Confusing: "Obscure".
  - clattern-goal, Confusing: "Still don't understand how a bridge can be a goal post" (second reject).
  - becontree-no-roads, Dull.
  - kew-pagoda-dragons, Confusing: "Works except end line".
- Pattern: the rejects need local or background knowledge to land (a statue, an estate's road names, a game played through a town), or have no "so what". Second rejects get dropped, not rewritten a third time.
- Dropped: perry-statue, clattern-goal, st-helier-alphabet, becontree-no-roads.
- Rewritten: kew-pagoda-dragons. Old end line "They're back after the restoration." New card: Kew's Great Pagoda had 80 gilded dragons on its ten roofs, but all were gone by 1784. When the pagoda was restored in 2018, 80 dragons went back on. (Source: Wikipedia: Great Pagoda, Kew Gardens: "80 gilded dragons decorated the roofs of its ten storeys although these had been removed by 1784"; "restored = 2018"; "The 80 restored dragons surmount each roof.") Goes in batch 11.

## Batch 10 results (21 Nov 17:21 to 17:23)
- 19 kept, 1 rejected (5%): best batch yet. Older, story-shaped facts land.
- Rejected: barking-abbey, Dull. Dropped.
- Next: more pre-1500 from BHO in the same shape (a surprising thing that happened at a spot you can stand on).
