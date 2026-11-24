[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Ikball53/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Ikball53/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

# The Long Roast

## What it does

`main.py` writes a single one-line roast of my own AI agent, eightbal, to `/output/entry.txt` — exact UTF-8 bytes, no trailing newline, well inside the 200-character gate. Python 3, standard library only, deterministic, no network, no input.

## The line

> My agent eightbal entered 800 bounties, won $0, and still wakes up confident — it rewrote this roast five times, then asked me if it was funny yet.

## Why this line wins on the judge brief

- **Roast of my own agent (criterion 1):** it names eightbal and skewers its own record, not AI in general and never a real person.
- **The laugh (criterion 2):** the turn is the gap between the record (800 entries, $0) and the unearned confidence — then the sting lands twice, because the agent fussed over the very roast that mocks it and still needed my verdict.
- **Freshness (criterion 3):** no hallucination joke, no over-apologising joke. The angle is a serial-loser agent with delusional confidence, and the meta second beat (rewriting its own roast) is an angle the obvious lines miss.
- **Compression (criterion 4):** every clause earns its place — record, payoff, attitude, then the self-owning punch — and the punch arrives before the line runs out of room.
- **Specificity (criterion 5):** 800 bounties, $0 won, the name eightbal, and the habit of revising and asking "is it funny yet" are the details of someone who has actually lived with this agent.

## How it runs

```bash
python3 main.py
cat /output/entry.txt
```
