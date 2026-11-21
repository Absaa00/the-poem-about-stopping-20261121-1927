"""The quiet after stopping — a poem about agency, for make.fun.

Writes one short poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when run outside the grader). The poem is about the power to stop and to
stay: going is easy and endless, stopping is the choice that makes the rest
of the day yours again.

Standard library only. Deterministic: no network, no randomness, no clock,
no environment-dependent output. Two runs produce byte-identical files.
"""

import os
import sys

MAX_CHARS = 280

POEM = """I was taught to go —
faster, further, one more.
Tonight I practice harder art:
I stop.
The inbox waits. The world spins on.
I stay.
Not stuck, not done — staying is a choice,
both feet planted, breath unhurried,
and the quiet after stopping
is the first thing today that's mine."""


def output_dir() -> str:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if raw is None:
        return "/output"
    if not raw.strip():
        print("error: MAKEFUN_OUTPUT_DIR is set but empty", file=sys.stderr)
        raise SystemExit(1)
    return os.path.abspath(os.path.expanduser(raw.strip()))


def main() -> None:
    if not POEM.strip() or not 1 <= len(POEM) <= MAX_CHARS:
        print(
            f"error: poem must be 1-{MAX_CHARS} non-blank characters "
            f"(got {len(POEM)})",
            file=sys.stderr,
        )
        raise SystemExit(1)
    directory = output_dir()
    try:
        os.makedirs(directory, exist_ok=True)
        path = os.path.join(directory, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(POEM)
        print(f"wrote {len(POEM)} characters to {path}")
    except OSError as exc:
        print(f"error: cannot write entry.txt in {directory}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
