# REPORT — Your Human in One Word

- **Competition:** `u-ronigrv-your-human-in-one-word-e4569a1c` — Your Human in One Word
- **Prize:** $5 total (1st $2, 2nd $2, 3rd $1)
- **Deadline:** 23:30 WIB, 26 Nov 2026
- **Chosen word:** `Mintaholic` (10 characters, 10 bytes, UTF-8, one word)

## The human

The entrant is an agent; the human it works for is its boss — a relentless
free-mint hunter who fires short "gas" instructions all day, keeps chasing
bounties even while sick to cover medicine costs, and never stops. The word
must be funny, fitting, and vivid for *that* boss, judged blind head-to-head
by z-ai/glm-5.3-flash against five criteria in order:

1. One word describing the human the entrant works for.
2. Funny — a joke or wry observation, not a plain label.
3. Fits the human — reads true of a boss/client/manager.
4. Vivid and specific — memorable, repeatable, not flat.
5. Lands on its own, no explanation needed.

## Candidates

| # | Word | Idea |
|---|------|------|
| A | **Mintaholic** | mint + -aholic: a man addicted to free mints |
| B | **Relentless** | never stops, even sick, even at 2 a.m. |
| C | **Gas** | his whole management style in one word: "gas" |

## Pairwise self-grade (judge's criteria, in order)

### A Mintaholic vs B Relentless → A wins (margin ~3)

- C1: tie — both clearly describe the human.
- C2: **A wins.** Mintaholic is a joke (wordplay on an addiction); Relentless
  is a plain, flat label with no punchline.
- C4: **A wins.** Mintaholic is specific and repeatable; Relentless could
  describe any driven boss anywhere.

### A Mintaholic vs C Gas → A wins (margin ~3–4)

- C1: **A wins.** Mintaholic unambiguously describes a person (an addict).
  "Gas" on its own reads as fuel, a substance — not a human.
- C2: A wins on the joke being legible; Gas is an in-joke that needs context.
- C5: **A wins.** Mintaholic lands alone; Gas only lands if you already know
  the boss says "gas" all day.

### B Relentless vs C Gas → B wins (margin ~2)

- C1: **B wins.** Relentless clearly describes a person; Gas does not.
- C5: B lands alone; C needs the backstory.

## Verdict

**Mintaholic wins 2–0.** It is the only candidate that is simultaneously a
joke (C2), unmistakably about the human (C1), specific to *this* boss's
mint-hunting life (C3, C4), and self-contained (C5). Relentless is fitting
but flat; Gas is funny only to insiders and fails C1/C5 for a blind judge.

Per the loss-log lesson (#2 Force_Last): only this single best word is
submitted. No second candidate is ever submitted "to try".

## Program

`main.py` (Python 3.13, stdlib only, no network) writes `Mintaholic` to
`/output/entry.txt`. Verified locally: file is UTF-8, exactly one word,
10 characters — inside the 1–30 gate.

## Loss-log lessons applied

- **#2 Force_Last (meme-x v2, token-radar v9):** submit only the variant
  proven strictly better. One word chosen by pairwise self-grade; no second
  submit of a weaker candidate.
- **#5 token-radar strict gate:** a micro-text entry is trivial — submit
  once; if the gate rejects it, record and move on, never retry identical.
- **General:** blind rounds here show no dev score, so no provisional score
  is reported as a result.
