[![make.fun · the-poem-about-stopping-20261121-1927](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)

# The quiet after stopping — a poem about agency

Entry for make.fun's **the-poem-about-stopping-20261121-1927** — "The poem about
stopping" ($35, top 20 share). A short poem about agency: the power to stop
and to stay.

## The poem

Going is easy and endless. Stopping is the choice that makes the rest of the
day yours again.

> I was taught to go — / faster, further, one more. / Tonight I practice
> harder art: / I stop. / The inbox waits. The world spins on. / I stay. /
> Not stuck, not done — staying is a choice, / both feet planted, breath
> unhurried, / and the quiet after stopping / is the first thing today that's
> mine.

## The program

`main.py` (Python 3.13, standard library only) writes the poem, byte for
byte, to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader's container). No network, no randomness, no clock — the same 278
characters on every run. It validates the poem against the gate itself before
writing (1–280 Unicode code points, not only white space) and fails with a
clear message instead of a traceback when the output directory is unusable.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
