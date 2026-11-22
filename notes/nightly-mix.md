# Nightly mix: picking the 5 finds (agreed 21 Nov, not built)

Tony, 21 Nov 16:25: up to 5 finds a night, the most interesting first, but not five from the same year or subject. Aim for the whole spectrum of time (e.g. something from 1890, music in the 1960s, the railways in the 1980s). If a day only offers one era (a day at Stonehenge), that's fine.

## Data (each fact gets two new fields)
- year: when the thing in the fact happened (rough is fine; negative for BC).
- topic: one word from a fixed list: war, transport, music, film, comedy, sport, royals, people, politics, law, science, invention, design, buildings, art, books, religion, names, traditions, everyday, work, shops, animals, nature, secrets, ancient.
- Era is worked out from year: prehistory, roman, saxon, medieval, tudor, stuart, georgian, victorian, early-20c (1901 to 1944), late-20c (1945 to 1999), 21c.
- Tags for all 112 London and SW20 facts so far: content/facts/fact-tags.json. New facts get tagged when written.

## Rule for the 9pm run
1. Candidates: untold zones he passed today (score 7+ as now).
2. Pick the highest score first.
3. For each next pick, take the highest of: score minus 1.5 for every already-picked find in the same era, minus 1.5 for every one with the same topic.
4. Stop at 5 or when candidates run out. Unpicked ones stay untold for another day, as now.
- Interest still leads: a 9 from an era already picked (7.5) beats a 7 from a new one.
- No personalisation: the mix depends only on the facts, never on what he tapped.

## Test (simulated on a central London walk, 13 candidates)
- Score only: Foyles in the Blitz, Fore Street bomb, Chenies D-Day shelter, Down Street, Bomber Command. Five Second World War facts.
- With the mix: Foyles in the Blitz (1940s, war), Sex Pistols (1970s, music), Prince Regent's bum cannon (Georgian, royals), Duck Island bombs (Victorian, secrets), Charles II fountain (Stuart, art).

## Content gap this shows
- Of 112 facts: 55 are 20th century, 30 are 1700s to 1800s, only 9 are before 1500.
- So the sourcing should lean older next: place-name origins and British History Online (needs british-history.ac.uk allowed), which are strongest on medieval and earlier.

## Build (Monday, with the zone fix)
- Add year and topic to spots.json from fact-tags.json.
- Change the 9pm pick to the rule above.
- Add to RULES.md.
