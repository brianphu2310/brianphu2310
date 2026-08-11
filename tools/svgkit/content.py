"""Copy and numbers shown in the README badges — the only file to edit
when the profile text changes."""

from . import theme

PROJECTS = {
    "proj1.svg": {
        "accent": theme.GREEN_DARK,
        "tag": "SUPPLY CHAIN",
        "tag_width": 94,
        "title": ["Nike vs Adidas —", "Factory Intelligence"],
        "body": [
            "Mapped 42 factories across 11 countries",
            "using PostgreSQL. Ran HHI concentration",
            "index to quantify production risk — Nike",
            "scores 0.18 vs Adidas 0.24. Nike is more",
            "geographically diversified by design.",
        ],
        "quote": [
            "Adidas keeps German factories at a cost",
            "premium. Nike has zero EU production.",
            "Not an accident — deliberate divergence.",
        ],
        "chips": [
            ("PostgreSQL", 66),
            ("Tableau", 44),
            ("OODA", 32),
            ("HHI", 26),
        ],
    },
    "proj2.svg": {
        "accent": theme.GREEN,
        "tag": "RECOMMENDER SYSTEM",
        "tag_width": 122,
        "title": ["Head Barista —", "Coffee Intelligence"],
        "body": [
            "Built from 3 years behind the counter.",
            "Scraped and cleaned 500+ bean profiles,",
            "applied NLP on tasting notes, then built",
            "a content-based recommender covering",
            "origin, roast level, and flavor affinity.",
        ],
        "quote": [
            "Best recommenders are not built by",
            "engineers — they are built by people",
            "who actually worked the domain.",
        ],
        "chips": [
            ("Python", 40),
            ("NLP", 26),
            ("Scraping", 54),
            ("Pandas", 44),
        ],
    },
    "proj3.svg": {
        "accent": theme.GREEN_DEEP,
        "tag": "SPORTS ANALYTICS",
        "tag_width": 107,
        "title": ["UFC Stance x", "Handedness Study"],
        "body": [
            "Analyzed 117 fighters across UFC history.",
            "Chi-square tested stance x hand dominance",
            "interaction. Cross-referenced win rates,",
            "finish types, and weight classes to",
            "separate signal from survivorship bias.",
        ],
        "quote": [
            "Southpaw advantage is real — but only",
            "in specific weight and experience bands.",
            "Context collapses the folklore.",
        ],
        "chips": [
            ("Python", 40),
            ("Statistics", 62),
            ("Tableau", 44),
            ("Chi-sq", 44),
        ],
    },
}

HEADER = {
    "kicker": "DATA ANALYST — SYDNEY, AU",
    "name": "Brian Phu",
    "tagline": "I turn messy data into decisions.",
    "subline": "Former barista · Muay Thai · Supply chain obsessive",
    "contacts": [
        "brianphu2310@gmail.com",
        "linkedin/brianphu2310",
        "github/brianphu2310",
    ],
}

SKILLS = [
    (20, "DATABASES", "PostgreSQL", "SQL · Data modeling"),
    (232, "VISUALIZATION", "Tableau", "Matplotlib · Seaborn"),
    (447, "ANALYSIS", "Python", "Pandas · NumPy · Statistics"),
    (662, "METHODS", "OODA Loop", "HHI · Web Scraping"),
]

FOOTER = {
    "quote": "If I cannot measure it, I do not trust my opinion on it.",
    "subline": (
        "OODA · Observe — Orient — Decide — Act · "
        "end-to-end ownership · no hand-waving"
    ),
    "cta_title": "OPEN TO OPPORTUNITIES",
    "cta_detail": "Sydney · supply chain · ops · data",
}
