"""Generate the student template from master.tex.

    python3 gen.py <output directory>

writes the complete student folder:
    workshop.tex                       state 0 of master.tex
    checkpoints/checkpoint-0n.tex      state n (n = 0 to 4)
    README.md, references.bib, figures/   copied from this directory
Nothing else ends up in it, so it can be zipped as it is.

Syntax in master.tex:
    <<<            start of a region
    @k             the following lines are used from state k on
    >>>            end of a region
Lines outside regions appear in every state. For state s, a region emits
the part with the largest k <= s (nothing if there is none).
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATIC = ["README.md", "references.bib", "figures"]
STATES = range(5)


def render(lines, state):
    out = []
    in_region = False
    parts = {}
    current = None
    for n, line in enumerate(lines, 1):
        tag = line.strip()
        if tag == "<<<":
            assert not in_region, f"master.tex:{n}: nested region"
            in_region, parts, current = True, {}, None
        elif tag == ">>>":
            assert in_region, f"master.tex:{n}: >>> without <<<"
            keys = [k for k in parts if k <= state]
            if keys:
                out.extend(parts[max(keys)])
            in_region = False
        elif in_region and tag.startswith("@") and tag[1:].isdigit():
            current = int(tag[1:])
            parts[current] = []
        elif in_region:
            assert current is not None, f"master.tex:{n}: text before @k"
            parts[current].append(line)
        else:
            out.append(line)
    assert not in_region, "master.tex: region not closed"
    return "".join(out)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    # Start from an empty folder, so no stale or auxiliary files get zipped.
    # Only ever delete a folder this script made (or an empty one).
    if out.exists():
        if any(out.iterdir()) and not (out / "workshop.tex").exists():
            sys.exit(f"{out} is not empty and not a generated template; not deleting it")
        shutil.rmtree(out)
    (out / "checkpoints").mkdir(parents=True)

    lines = (HERE / "master.tex").read_text(encoding="utf-8").splitlines(keepends=True)
    (out / "workshop.tex").write_text(render(lines, 0), encoding="utf-8")
    for s in STATES:
        (out / "checkpoints" / f"checkpoint-0{s}.tex").write_text(render(lines, s), encoding="utf-8")
    for name in STATIC:
        src = HERE / name
        if src.is_dir():
            shutil.copytree(src, out / name)
        else:
            shutil.copy2(src, out / name)
    print(f"generated {out}")


if __name__ == "__main__":
    main()
