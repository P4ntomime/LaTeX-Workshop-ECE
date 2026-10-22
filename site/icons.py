"""Draw the README button and the favicon as SVG, with the text as paths.

Usage: python3 icons.py <Latin Modern font directory> [<output directory>]

On Ubuntu the fonts come with the package fonts-lmodern:
    python3 site/icons.py /usr/share/texmf/fonts/opentype/public/lm site
Needs: pip install fonttools uharfbuzz

The text is converted to paths because GitHub shows an SVG in a README as
an image, where it cannot load a font. The output only needs regenerating
after changing something here; the SVGs are committed.

Writes:
    readme-button.svg     the button at the top of the repository's README
    favicon.svg           the browser tab icon of the Pages site
    apple-touch-icon.svg  the same with square corners, for phone home screens
The PNG versions are rendered from these, e.g. with Inkscape:
    inkscape favicon.svg -w 32 -o favicon-32.png
    inkscape apple-touch-icon.svg -w 180 -o apple-touch-icon.png
"""

import sys
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

# The slides' theme colour (mythemecolor), also used on the Pages site.
PLUM = "#8c195f"
WHITE = "#ffffff"


class Font:
    """One OpenType font: shapes text with HarfBuzz, draws it with fontTools."""

    def __init__(self, path):
        data = Path(path).read_bytes()
        self.hb_font = hb.Font(hb.Face(data))
        self.tt = TTFont(path)
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.upm = self.tt["head"].unitsPerEm

    def shape(self, text):
        """Glyph names and advances (in em) of text, with the font's kerning."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf, {"kern": True, "liga": True})
        return [(self.order[info.codepoint], pos.x_advance / self.upm)
                for info, pos in zip(buf.glyph_infos, buf.glyph_positions)]


class Line:
    """A row of glyphs in em units, y pointing up as in the font.

    add() appends text at the current position; kern() moves the position,
    raise_ shifts what follows up (negative: down), like \\kern and \\raise.
    """

    def __init__(self):
        self.items = []  # (font, glyph name, x, y, size)
        self.x = 0.0

    def add(self, font, text, size=1.0, raise_=0.0):
        for name, advance in font.shape(text):
            self.items.append((font, name, self.x, raise_, size))
            self.x += advance * size
        return self

    def kern(self, em):
        self.x += em
        return self

    def _draw(self, pen_for, scale, dx, dy):
        for font, name, x, y, size in self.items:
            s = scale * size / font.upm
            # Font coordinates have y up, SVG has y down.
            pen = TransformPen(pen_for(), (s, 0, 0, -s, dx + x * scale, dy - y * scale))
            font.glyphs[name].draw(pen)

    def bounds(self, scale=1.0):
        """(xmin, ymin, xmax, ymax) in SVG coordinates at the given scale."""
        box = BoundsPen(None)
        self._draw(lambda: box, scale, 0, 0)
        return box.bounds

    def path(self, scale, dx, dy):
        """SVG path data, scaled to scale units per em, origin at (dx, dy)."""
        pen = SVGPathPen(None, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        self._draw(lambda: pen, scale, dx, dy)
        return pen.getCommands()


def latex_logo(font, line=None):
    """The \\LaTeX logo, with the kerns and shifts of the LaTeX kernel."""
    line = line or Line()
    line.add(font, "L").kern(-0.36)
    # The small A: about \scriptsize at 10pt, raised so its top meets the T.
    line.add(font, "A", size=0.7, raise_=0.21).kern(-0.15)
    line.add(font, "T").kern(-0.1667)
    line.add(font, "E", raise_=-0.215).kern(-0.125)
    return line.add(font, "X")


def centred(line, scale, width, height, dy=0.0, fit=None):
    """Path data of line, centred in a width × height box (optical shift dy).

    With fit=(w, h), scale is chosen so the drawn glyphs fit into w × h.
    """
    if fit:
        x0, y0, x1, y1 = line.bounds(1.0)
        scale = min(fit[0] / (x1 - x0), fit[1] / (y1 - y0))
    x0, y0, x1, y1 = line.bounds(scale)
    dx = (width - (x1 - x0)) / 2 - x0
    dyy = (height - (y1 - y0)) / 2 - y0 + dy
    return line.path(scale, dx, dyy)


def readme_button(fonts):
    """Plum button: \\LaTeX Workshop and an arrow (the link leaves GitHub)."""
    height, pad, gap, arrow, size = 76, 34, 16, 13, 34
    text = latex_logo(fonts["regular"]).kern(0.333).add(fonts["regular"], "Workshop")
    x0, y0, x1, y1 = text.bounds(size)
    width = round(pad + (x1 - x0) + gap + arrow + pad)
    baseline = 49
    d = text.path(size, pad - x0, baseline)
    ax = pad + (x1 - x0) + gap   # left edge of the arrow
    ay = baseline - 9            # its vertical centre, at about x-height
    h = arrow / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="LaTeX Workshop">
<title>LaTeX Workshop</title>
<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="10" fill="{PLUM}"/>
<path d="{d}" fill="{WHITE}"/>
<path d="M{ax:.1f} {ay + h:.1f}L{ax + arrow:.1f} {ay - h:.1f}M{ax + arrow - 5.5:.1f} {ay - h:.1f}H{ax + arrow:.1f}V{ay - h + 5.5:.1f}" fill="none" stroke="{WHITE}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def favicon(fonts, radius=12):
    """A page with a folded corner and the start of the \\LaTeX logo, on plum.

    The document the students write. radius rounds the plum tile; 0 for the
    phone home-screen icon, whose corners the phone rounds itself.
    """
    page = "M16 6H40L52 18V54A4 4 0 0 1 48 58H16A4 4 0 0 1 12 54V10A4 4 0 0 1 16 6Z"
    fold = "M40 6V16A2 2 0 0 0 42 18H52Z"
    # L and the small raised A, as in latex_logo().
    line = Line().add(fonts["bold"], "L").kern(-0.36)
    line.add(fonts["bold"], "A", size=0.7, raise_=0.21)
    x0, y0, x1, y1 = line.bounds(26)
    logo = line.path(26, 18 - x0, 36)
    # Two lines of text under it.
    rules = "".join(f'<rect x="18" y="{y}" width="{w}" height="3.4" rx="1.7"/>'
                    for y, w in ((42, 28), (49, 20)))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<rect width="64" height="64" rx="{radius}" fill="{PLUM}"/>
<path d="{page}" fill="{WHITE}"/>
<path d="{fold}" fill="{PLUM}" opacity=".35"/>
<path d="{logo}" fill="{PLUM}"/>
<g fill="{PLUM}" opacity=".45">{rules}</g>
</svg>
"""


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    fontdir = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else Path(__file__).resolve().parent
    fonts = {
        "regular": Font(fontdir / "lmroman10-regular.otf"),
        "bold": Font(fontdir / "lmroman10-bold.otf"),
    }
    (out / "readme-button.svg").write_text(readme_button(fonts))
    (out / "favicon.svg").write_text(favicon(fonts))
    (out / "apple-touch-icon.svg").write_text(favicon(fonts, radius=0))
    print(f"wrote {out}/")


if __name__ == "__main__":
    main()
