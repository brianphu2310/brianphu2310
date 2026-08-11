"""Composite pieces reused across the README badges."""

from . import theme
from .elements import document, line, rect, text, text_block

CARD_WIDTH = 280
CARD_HEIGHT = 265
CARD_PADDING = 16
CHIP_GAP = 6


def category_tag(text_content, width, *, x=CARD_PADDING, y=18, height=17):
    return [
        rect(width, height, theme.GREEN_PALE, x=x, y=y, rx=2),
        text(
            x + 6,
            y + 12,
            text_content,
            font=theme.SANS,
            size=9,
            weight=700,
            fill=theme.GREEN_DARK,
            letter_spacing=1,
        ),
    ]


def chip_row(chips, *, x=CARD_PADDING, y=245, height=14):
    """Lay out `(label, width)` chips left to right with a fixed gap."""
    out = []
    cursor = x
    for label, width in chips:
        out.append(rect(width, height, theme.PAPER, x=cursor, y=y, rx=2))
        out.append(
            text(
                cursor + 4,
                y + 11,
                label,
                font=theme.MONO,
                size=9,
                fill=theme.INK_MUTED,
            )
        )
        cursor += width + CHIP_GAP
    return out


def pull_quote(lines, *, x=CARD_PADDING, y=188):
    return [
        rect(2.5, 42, theme.GREEN, x=x, y=y),
        *text_block(
            x + 10,
            y + 13,
            lines,
            leading=15,
            font=theme.SANS,
            size=9.5,
            style="italic",
            fill=theme.GREEN_DARK,
        ),
    ]


def project_card(card):
    """Render one project card; `card` is a dict from content.PROJECTS."""
    body = [
        rect(
            CARD_WIDTH,
            CARD_HEIGHT,
            theme.WHITE,
            rx=5,
            stroke=theme.GREEN_LIGHT,
            stroke_width=1,
        ),
        rect(CARD_WIDTH, 5, card["accent"], rx=5),
        rect(CARD_WIDTH, 1, card["accent"], y=4),
        "",
        *category_tag(card["tag"], card["tag_width"]),
        "",
        *text_block(
            CARD_PADDING,
            64,
            card["title"],
            leading=19,
            font=theme.SERIF,
            size=16,
            fill=theme.INK,
        ),
        "",
        line(
            CARD_PADDING,
            95,
            CARD_WIDTH - CARD_PADDING,
            95,
            theme.GREEN_PALE,
            1,
        ),
        "",
        *text_block(
            CARD_PADDING,
            113,
            card["body"],
            leading=16,
            font=theme.SANS,
            size=10.5,
            fill=theme.INK_MUTED,
        ),
        "",
        *pull_quote(card["quote"]),
        "",
        *chip_row(card["chips"]),
    ]
    return document(CARD_WIDTH, CARD_HEIGHT, body)


def kpi(x, y, value, caption, *, value_size=40, caption_dx=0, caption_dy=18):
    """A big serif number with a small all-caps caption."""
    return [
        text(x, y, value, font=theme.SERIF, size=value_size, fill=theme.GREEN_LIGHT),
        text(
            x + caption_dx,
            y + caption_dy,
            caption,
            font=theme.SANS,
            size=9,
            fill=theme.GREEN_MID,
            letter_spacing=1,
        ),
    ]


def skill_column(x, category, headline, detail):
    return [
        text(
            x,
            22,
            category,
            font=theme.SANS,
            size=9,
            fill=theme.INK_GHOST,
            letter_spacing=1.5,
        ),
        text(
            x,
            44,
            headline,
            font=theme.MONO,
            size=12,
            weight="bold",
            fill=theme.GREEN_DARK,
        ),
        text(x, 62, detail, font=theme.MONO, size=10.5, fill=theme.INK_FAINT),
    ]
