#!/usr/bin/env python3
"""Regenerate every SVG used by README.md.

    python tools/build_svg.py            # write the SVGs
    python tools/build_svg.py --check    # fail if the committed SVGs are stale
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import content, theme  # noqa: E402
from svgkit.components import kpi, project_card, skill_column  # noqa: E402
from svgkit.elements import document, line, rect, text  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


def build_header():
    data = content.HEADER
    body = [
        rect(860, 180, theme.GREEN_DARK, rx=6),
        line(0, 60, 520, 60, theme.GREEN, 0.5, opacity=0.35),
        line(0, 120, 520, 120, theme.GREEN, 0.5, opacity=0.35),
        line(528, 0, 528, 180, theme.GREEN_LIGHT, 0.6, opacity=0.3),
        line(700, 16, 700, 164, theme.GREEN, 0.5, opacity=0.35),
        "",
        text(
            36,
            36,
            data["kicker"],
            font=theme.SANS_BLACK,
            size=10,
            weight=700,
            fill=theme.GREEN_MID,
            letter_spacing=3,
        ),
        text(
            34,
            108,
            data["name"],
            font=theme.SERIF,
            size=56,
            weight=400,
            fill=theme.GREEN_PALE,
        ),
        text(
            36,
            140,
            data["tagline"],
            font=theme.SANS,
            size=13,
            fill=theme.GREEN_LIGHT,
            opacity=0.9,
        ),
        text(
            36,
            162,
            data["subline"],
            font=theme.SANS,
            size=11.5,
            fill=theme.GREEN_LIGHT,
            opacity=0.6,
        ),
        "",
        *kpi(552, 52, "42", "FACTORIES ANALYZED"),
        "",
        *kpi(552, 110, "117", "UFC FIGHTERS"),
        "",
        *kpi(552, 162, "11", "COUNTRIES", value_size=28, caption_dx=40, caption_dy=0),
        "",
    ]
    for index, contact in enumerate(data["contacts"]):
        body.append(
            text(
                716,
                52 + index * 22,
                contact,
                font=theme.SANS,
                size=10.5,
                fill=theme.GREEN_PALE,
                opacity=0.55,
            )
        )
    return document(860, 180, body)


def build_skills():
    body = [
        rect(860, 76, theme.PAPER, rx=4, stroke=theme.GREEN_LIGHT, stroke_width=1),
        line(215, 0, 215, 76, theme.GREEN_LIGHT, 0.8),
        line(430, 0, 430, 76, theme.GREEN_LIGHT, 0.8),
        line(645, 0, 645, 76, theme.GREEN_LIGHT, 0.8),
    ]
    for column in content.SKILLS:
        body.append("")
        body.extend(skill_column(*column))
    return document(860, 76, body)


def build_footer():
    data = content.FOOTER
    body = [
        rect(860, 100, theme.INK, rx=4),
        text(
            18,
            78,
            '"',
            font=theme.SERIF,
            size=80,
            fill=theme.GREEN,
            opacity=0.18,
        ),
        text(52, 46, data["quote"], font=theme.SERIF, size=19, fill=theme.GREEN_LIGHT),
        text(
            53,
            70,
            data["subline"],
            font=theme.SANS,
            size=11,
            fill=theme.INK_FAINT,
            letter_spacing=0.5,
        ),
        rect(180, 56, theme.GREEN_DARK, x=658, y=22, rx=3),
        text(
            676,
            43,
            data["cta_title"],
            font=theme.SANS,
            size=9.5,
            weight=700,
            fill=theme.GREEN_LIGHT,
            letter_spacing=1,
        ),
        line(676, 50, 820, 50, theme.GREEN, 0.5),
        text(
            676,
            65,
            data["cta_detail"],
            font=theme.SANS,
            size=10,
            fill=theme.GREEN_PALE,
            opacity=0.7,
        ),
    ]
    return document(860, 100, body)


def render_all():
    files = {
        "header.svg": build_header(),
        "skills.svg": build_skills(),
        "footer.svg": build_footer(),
    }
    for name, card in content.PROJECTS.items():
        files[name] = project_card(card)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed SVGs match the generator output",
    )
    args = parser.parse_args()

    stale = []
    for name, markup in sorted(render_all().items()):
        path = REPO_ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != markup:
                stale.append(name)
        else:
            path.write_text(markup)
            print(f"wrote {name}")

    if args.check:
        if stale:
            print("stale: " + ", ".join(stale), file=sys.stderr)
            return 1
        print("all SVGs up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
