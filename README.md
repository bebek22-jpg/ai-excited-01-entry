# ai-excited-01 — "Breach Under the Aurora"

Entry for the make.fun competition **ai-excited-01** ("Make the AI judge
excited"): a program that writes one image to `/output/entry.png`.

## The image

A colossal humpback whale breaching vertically out of a glowing
electric-blue bioluminescent ocean at night, water exploding around it in
luminous spray, under a vivid green-and-purple aurora sky — with a tiny
wooden boat and a lone fisherman in the foreground for dramatic scale.

Why this image: one look gives a jolt of scale and awe (a creature the
size of a house hanging mid-air), the bioluminescence + aurora pairing is
a twist on the familiar whale-breach shot rather than a stock explosion,
the spray and the whale's arc carry real momentum, and the composition —
one huge diagonal shape against a dark sky — still reads clearly at
~300 pixels across.

The image was generated for this entry and resized to 1024×683. It is
stored as JPEG bytes in `entry.png` (the competition rules allow a JPEG
told apart by its first bytes; the name stays `entry.png`).

## The program

`main.py` (Python 3, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network, no
randomness: both grader runs produce identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
