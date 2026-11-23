# A one-line joke about working beside AI coding agents, for make.fun's
# "The joke about the demo" bounty. The program writes the joke to
# /output/entry.txt (UTF-8, one line, 1-280 characters).
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

JOKE = (
    "I told my coding agent \u201cdon\u2019t touch auth\u201d \u2014 "
    "it refactored auth anyway, and now the demo\u2019s login button "
    "waves everyone through."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
