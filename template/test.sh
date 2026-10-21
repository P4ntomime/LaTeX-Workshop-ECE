#!/bin/bash
# Build workshop.tex, workshop.tex with TODO 1.1 done, and every checkpoint,
# each copied to the template root as a student would, and report problems.
# Fails on any error, warning or undefined reference.
#
# Usage: bash test.sh [template folder] [build folder]
#   defaults: build/workshop-template next to this script, and a new
#   temporary folder for the builds
here=$(cd "$(dirname "$0")" && pwd)
T=$(realpath "${1:-$here/build/workshop-template}")
B=$(realpath "${2:-$(mktemp -d)}")
mkdir -p "$B"
status=0

build () {  # name, source file
    d="$B/$1"; mkdir -p "$d"
    cp -r "$T/figures" "$T/references.bib" "$d/"
    cp "$2" "$d/main.tex"
    # -gg: remove earlier build files first, so every run starts from scratch
    (cd "$d" && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex >latexmk.out 2>&1)
    rc=$?
    probs=$(grep -hE "^!|Warning|Underfull|Overfull|undefined|Rerun to|WARN|ERROR" "$d/main.log" "$d/main.blg" 2>/dev/null)
    pages=$(pdfinfo "$d/main.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
    printf '%-16s rc=%s pages=%s\n' "$1" "$rc" "${pages:-none}"
    [ -n "$probs" ] && { echo "$probs" | sed 's/^/    /'; status=1; }
    [ $rc -ne 0 ] && status=1
}

build workshop "$T/workshop.tex"
sed 's/^%   Write Hello OST! on the line after \\begin{document}, then compile.$//; s/^\\begin{document}$/\\begin{document}\nHello OST!/' \
    "$T/workshop.tex" > "$B/hello.tex"
build workshop-1.1 "$B/hello.tex"
for n in 0 1 2 3 4; do
    build "checkpoint-0$n" "$T/checkpoints/checkpoint-0$n.tex"
done

echo "builds in $B"
[ $status -eq 0 ] && echo "all clean" || echo "PROBLEMS"
exit $status
