"""Primitive SVG builders shared by all badge generators.

Every helper returns a single line of SVG markup. Attributes are always
emitted in the same order so output stays stable across runs.
"""

from xml.sax.saxutils import escape


def _attrs(pairs):
    return "".join(
        f' {name}="{value}"' for name, value in pairs if value is not None
    )


def _num(value):
    if value is None:
        return None
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def document(width, height, body):
    """Wrap indented body lines in an <svg> root element."""
    lines = [
        f'<svg width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    ]
    lines.extend(body)
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def rect(
    width,
    height,
    fill,
    *,
    x=None,
    y=None,
    rx=None,
    stroke=None,
    stroke_width=None,
):
    return "  <rect" + _attrs(
        [
            ("x", _num(x)),
            ("y", _num(y)),
            ("width", _num(width)),
            ("height", _num(height)),
            ("fill", fill),
            ("rx", _num(rx)),
            ("stroke", stroke),
            ("stroke-width", _num(stroke_width)),
        ]
    ) + "/>"


def line(x1, y1, x2, y2, stroke, stroke_width, *, opacity=None):
    return "  <line" + _attrs(
        [
            ("x1", _num(x1)),
            ("y1", _num(y1)),
            ("x2", _num(x2)),
            ("y2", _num(y2)),
            ("stroke", stroke),
            ("stroke-width", _num(stroke_width)),
            ("opacity", _num(opacity)),
        ]
    ) + "/>"


def text(
    x,
    y,
    content,
    *,
    font,
    size,
    fill,
    weight=None,
    style=None,
    letter_spacing=None,
    opacity=None,
):
    attrs = _attrs(
        [
            ("x", _num(x)),
            ("y", _num(y)),
            ("font-family", font),
            ("font-size", _num(size)),
            ("font-weight", weight),
            ("font-style", style),
            ("fill", fill),
            ("letter-spacing", _num(letter_spacing)),
            ("opacity", _num(opacity)),
        ]
    )
    return f"  <text{attrs}>{escape(content)}</text>"


def text_block(x, y, lines, *, leading, **style):
    """Stack `lines` of text downwards, one <text> per line."""
    return [
        text(x, y + index * leading, content, **style)
        for index, content in enumerate(lines)
    ]
