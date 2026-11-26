#!/usr/bin/env python3
"""Entry program for "One-Liner Laughs"
(u-coral-404-one-liner-laughs-aa872d41).

One funny line, at most 200 characters, any topic, written to
/output/entry.txt. The judge brief in the kit's RULES asks for,
in order: a real one-line joke with a clear setup and a payoff;
a laugh out loud, not just a smile; a surprise twist that is
the point of the line; freshness; and no wasted words.

Design, from fourteen candidates I wrote in this session and
two rounds of strict external review: the winner is the gym
money-back line, ranked first in both rounds (39/50). The
setup is a guarantee the gym itself offered, and the turn is
that the gym pays out early and unprompted: the business, not
the customer, gives up. The laugh lands on the last two words,
the gym's whole verdict, "we saw", which leaves what they saw
implicit instead of explained. Round 2 tried four revisions
that earned the refund with explicit evidence (a watched
first workout, a ten-minute session, an extrapolation note);
the review killed each because stating the evidence delivers
the joke early and the closing note then only explains it
again, so the asserted original, coldest and tightest, stands
as the final text unchanged.
"""

TEXT = """\
I joined a gym with a money-back guarantee, and they paid out in week two, unprompted, with a note that just said "we saw."
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
