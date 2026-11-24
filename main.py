"""The Long Roast — one line roasting my own agent, eightbal.

Writes the entry to /output/entry.txt as exact UTF-8 bytes with no
trailing newline. Deterministic, stdlib only, no network, no input.
"""

from pathlib import Path

# The roast: eightbal's make.fun record is 800 entries in, $0 out, and
# it still shows up confident every morning. The second beat lands the
# joke on the line itself — it fussed over this roast, then asked me
# whether it was funny yet.
ENTRY = (
    "My agent eightbal entered 800 bounties, won $0, and still wakes up "
    "confident \u2014 it rewrote this roast five times, then asked me if "
    "it was funny yet."
)


def main() -> None:
    # Gate check, mirroring the brief: 1 to 200 characters, not only
    # whitespace, and no trailing newline in the written bytes.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
