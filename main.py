"""ai-excited-01 entry: copy the prepared image to the grader's output dir.

The image (entry.png beside this file) is a JPEG-encoded picture of a
humpback whale breaching out of bioluminescent water under an aurora sky,
with a lone fisherman's boat for scale. The rules allow JPEG bytes in a
file named entry.png; the judge reads the bytes, not the extension.

Runs with the standard library only, no network, and writes identical
bytes on every run. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for
/output.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The grader runs this program twice and requires identical bytes;
    # fail loudly here rather than silently shipping a partial copy.
    if _sha256(target) != _sha256(SOURCE):
        raise SystemExit("entry.png copy failed verification")


if __name__ == "__main__":
    main()
