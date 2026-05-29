<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Brian Phu — Data Analyst</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Sora:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}

  :root{
    --teal-dark:#0F6E56;
    --teal-mid:#1D9E75;
    --teal-light:#5DCAA5;
    --teal-pale:#9FE1CB;
    --teal-bg:#E1F5EE;
    --slate:#2C2C2A;
    --slate-mid:#5F5E5A;
    --slate-light:#B4B2A9;
    --cream:#F1EFE8;
    --white:#ffffff;
  }

  html{scroll-behavior:smooth}
  body{
    font-family:'Sora',sans-serif;
    background:var(--cream);
    color:var(--slate);
    line-height:1.6;
    min-height:100vh;
  }

  .page{max-width:900px;margin:0 auto;padding:3rem 2rem}

  /* HEADER */
  .header{
    display:grid;
    grid-template-columns:1fr auto;
    gap:2rem;
    align-items:end;
    border-bottom:2px solid var(--teal-mid);
    padding-bottom:2rem;
    margin-bottom:2.5rem;
  }
  .label-sm{
    font-size:11px;
    letter-spacing:.18em;
    text-transform:uppercase;
    color:var(--teal-mid);
    font-weight:500;
    margin-bottom:.5rem;
  }
  .name{
    font-family:'DM Serif Display',serif;
    font-size:3.8rem;
    line-height:1.05;
    color:var(--slate);
    margin-bottom:.4rem;
  }
  .name em{color:var(--teal-dark);font-style:normal}
  .tagline{
    font-size:.95rem;
    color:var(--slate-mid);
    font-weight:300;
    max-width:400px;
    line-height:1.7;
  }
  .header-meta{
    text-align:right;
    font-size:.8rem;
    color:var(--slate-light);
    line-height:2.2;
  }
  .header-meta a{
    display:block;
    color:var(--teal-dark);
    text-decoration:none;
    font-weight:500;
    font-size:.85rem;
    transition:color .15s;
  }
  .header-meta a:hover{color:var(--teal-mid)}

  /* ABOUT STRIP */
  .about{
    background:var(--teal-dark);
    color:var(--teal-bg);
    border-radius:3px;
    padding:1.75rem 2rem;
    margin-bottom:2.5rem;
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:1.5rem;
  }
  .about-item .num{
    font-family:'DM Serif Display',serif;
    font-size:2.4rem;
    color:var(--teal-pale);
    line-height:1;
    margin-bottom:.3rem;
  }
  .about-item .desc{
    font-size:.78rem;
    color:var(--teal-pale);
    opacity:.7;
    font-weight:300;
    line-height:1.5;
  }
  .about-divider{
    border-left:1px solid rgba(255,255,255,.15);
    padding-left:1.5rem;
  }

  /* TICKER */
  .ticker-wrap{
    overflow:hidden;
    border-top:1px solid var(--teal-pale);
    border-bottom:1px solid var(--teal-pale);
    padding:.55rem 0;
    margin-bottom:2.5rem;
    background:var(--white);
  }
  .ticker{
    display:flex;
    gap:3rem;
    width:max-content;
    animation:ticker 24s linear infinite;
  }
  @keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}
  .ticker-item{
    font-size:.72rem;
    letter-spacing:.14em;
    text-transform:uppercase;
    color:var(--slate-light);
    white-space:nowrap;
  }
  .ticker-item.hi{color:var(--teal-mid);font-weight:600}

  /* SECTION LABEL */
  .section-label{
    font-size:11px;
    letter-spacing:.18em;
    text-transform:uppercase;
    color:var(--teal-mid);
    font-weight:500;
    margin-bottom:1rem;
    display:flex;
    align-items:center;
    gap:.75rem;
  }
  .section-label::after{
    content:'';flex:1;height:1px;background:var(--teal-pale);
  }

  /* PROJECT CARDS */
  .projects{
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:1px;
    background:var(--slate-light);
    border:1px solid var(--slate-light);
    margin-bottom:2.5rem;
  }
  .proj-card{
    background:var(--white);
    padding:1.5rem 1.25rem;
    display:flex;
    flex-direction:column;
    gap:.75rem;
    text-decoration:none;
    color:inherit;
    transition:background .18s;
  }
  .proj-card:hover{background:var(--teal-bg)}
  .proj-tag{
    font-size:10px;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:var(--teal-dark);
    font-weight:600;
    background:var(--teal-bg);
    padding:3px 8px;
    width:fit-content;
    border-radius:2px;
  }
  .proj-card:hover .proj-tag{background:var(--teal-pale)}
  .proj-title{
    font-family:'DM Serif Display',serif;
    font-size:1.15rem;
    color:var(--slate);
    line-height:1.25;
  }
  .proj-desc{
    font-size:.78rem;
    color:var(--slate-mid);
    line-height:1.65;
    font-weight:300;
    flex:1;
  }
  .proj-finding{
    font-size:.73rem;
    color:var(--teal-dark);
    border-left:2px solid var(--teal-mid);
    padding-left:.6rem;
    font-style:italic;
    line-height:1.55;
  }
  .proj-stack{
    display:flex;
    flex-wrap:wrap;
    gap:4px;
  }
  .stack-pill{
    font-family:'DM Mono',monospace;
    font-size:10px;
    color:var(--slate-mid);
    border:1px solid var(--slate-light);
    padding:2px 7px;
    border-radius:2px;
  }

  /* PHILOSOPHY */
  .philosophy{
    border:1px solid var(--teal-pale);
    padding:1.75rem 2rem;
    margin-bottom:2.5rem;
    position:relative;
    background:var(--white);
  }
  .philosophy-quote{
    font-family:'DM Serif Display',serif;
    font-size:1.7rem;
    color:var(--teal-dark);
    line-height:1.35;
    margin-bottom:.75rem;
  }
  .philosophy-sub{
    font-size:.85rem;
    color:var(--slate-mid);
    font-weight:300;
    max-width:560px;
    line-height:1.75;
  }
  .philosophy-tag{
    position:absolute;
    top:-11px;
    left:1.5rem;
    background:var(--cream);
    padding:0 .5rem;
    font-size:10px;
    letter-spacing:.15em;
    text-transform:uppercase;
    color:var(--teal-mid);
    font-weight:600;
  }

  /* SKILLS */
  .skills-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:1px;
    background:var(--slate-light);
    border:1px solid var(--slate-light);
    margin-bottom:2.5rem;
  }
  .skill-cell{
    background:var(--white);
    padding:1.1rem 1rem;
  }
  .skill-cell .category{
    font-size:10px;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:var(--slate-light);
    font-weight:500;
    margin-bottom:.65rem;
  }
  .skill-list{list-style:none;display:flex;flex-direction:column;gap:.35rem}
  .skill-list li{
    font-family:'DM Mono',monospace;
    font-size:.78rem;
    color:var(--slate-mid);
  }
  .skill-list li.primary{color:var(--teal-dark);font-weight:500}

  /* CONTACT */
  .contact{
    background:var(--slate);
    color:var(--cream);
    padding:1.75rem 2rem;
    display:grid;
    grid-template-columns:1fr auto;
    align-items:center;
    gap:2rem;
    border-radius:3px;
  }
  .contact-title{
    font-family:'DM Serif Display',serif;
    font-size:1.5rem;
    color:var(--teal-pale);
    margin-bottom:.4rem;
  }
  .contact-sub{font-size:.82rem;color:var(--slate-light);font-weight:300;line-height:1.65;max-width:400px}
  .contact-links{display:flex;flex-direction:column;gap:.6rem;text-align:right}
  .contact-links a{
    font-size:.82rem;
    color:var(--teal-pale);
    text-decoration:none;
    font-family:'DM Mono',monospace;
    transition:color .15s;
  }
  .contact-links a:hover{color:var(--white)}

  /* RESPONSIVE */
  @media(max-width:680px){
    .header{grid-template-columns:1fr;gap:1rem}
    .header-meta{text-align:left}
    .about{grid-template-columns:1fr;gap:1.25rem}
    .about-divider{border-left:none;padding-left:0;border-top:1px solid rgba(255,255,255,.15);padding-top:1.25rem}
    .projects{grid-template-columns:1fr}
    .skills-grid{grid-template-columns:1fr 1fr}
    .contact{grid-template-columns:1fr;gap:1rem}
    .contact-links{text-align:left}
    .name{font-size:2.6rem}
  }
</style>
</head>
<body>
<div class="page">

  <header class="header">
    <div>
      <p class="label-sm">Data Analyst — Sydney, AU</p>
      <h1 class="name">Brian <em>Phu</em></h1>
      <p class="tagline">I turn messy data into decisions. Former barista. Muay Thai practitioner. Supply chain obsessive.</p>
    </div>
    <div class="header-meta">
      <span>Sydney, NSW</span>
      <a href="mailto:brianphu2310@gmail.com">brianphu2310@gmail.com</a>
      <a href="https://linkedin.com/in/brianphu2310">linkedin/brianphu2310</a>
      <a href="https://github.com/brianphu2310">github/brianphu2310</a>
    </div>
  </header>

  <div class="about">
    <div class="about-item">
      <div class="num">42</div>
      <div class="desc">factories analyzed across 11 countries — Nike vs Adidas</div>
    </div>
    <div class="about-item about-divider">
      <div class="num">117</div>
      <div class="desc">UFC fighters. Stance × handedness. Real data, real patterns.</div>
    </div>
    <div class="about-item about-divider">
      <div class="num">3+</div>
      <div class="desc">end-to-end projects: scrape → model → deploy</div>
    </div>
  </div>

  <div class="ticker-wrap" aria-hidden="true">
    <div class="ticker">
      <span class="ticker-item">PostgreSQL</span>
      <span class="ticker-item hi">OODA Framework</span>
      <span class="ticker-item">Tableau</span>
      <span class="ticker-item">Python</span>
      <span class="ticker-item hi">Supply Chain Analysis</span>
      <span class="ticker-item">HHI Analysis</span>
      <span class="ticker-item">Web Scraping</span>
      <span class="ticker-item hi">Statistical Modeling</span>
      <span class="ticker-item">Pandas / NumPy</span>
      <span class="ticker-item">NLP</span>
      <span class="ticker-item hi">End-to-End Projects</span>
      <span class="ticker-item">PostgreSQL</span>
      <span class="ticker-item hi">OODA Framework</span>
      <span class="ticker-item">Tableau</span>
      <span class="ticker-item">Python</span>
      <span class="ticker-item hi">Supply Chain Analysis</span>
      <span class="ticker-item">HHI Analysis</span>
      <span class="ticker-item">Web Scraping</span>
      <span class="ticker-item hi">Statistical Modeling</span>
      <span class="ticker-item">Pandas / NumPy</span>
      <span class="ticker-item">NLP</span>
      <span class="ticker-item hi">End-to-End Projects</span>
    </div>
  </div>

  <p class="section-label">Projects</p>

  <div class="projects">
    <a class="proj-card" href="https://github.com/brianphu2310/NIKE-AND-ADIDAS-FACTORIES-STRATERGY" target="_blank" rel="noopener">
      <span class="proj-tag">Supply Chain</span>
      <h2 class="proj-title">Nike vs Adidas — Global Factory Intelligence</h2>
      <p class="proj-desc">Mapped 42 factories across 11 countries. Ran HHI concentration analysis to quantify production risk. Traced the strategic divergence between two brands with radically different manufacturing footprints.</p>
      <p class="proj-finding">Adidas keeps domestic German factories at a cost premium. Nike has zero European production. Not an accident — a deliberate strategic divergence.</p>
      <div class="proj-stack">
        <span class="stack-pill">PostgreSQL</span>
        <span class="stack-pill">Tableau</span>
        <span class="stack-pill">OODA</span>
        <span class="stack-pill">HHI</span>
      </div>
    </a>
    <a class="proj-card" href="https://github.com/brianphu2310/Head-Barista-Coffee-Intelligence" target="_blank" rel="noopener">
      <span class="proj-tag">Recommender System</span>
      <h2 class="proj-title">Head Barista — Coffee Intelligence</h2>
      <p class="proj-desc">Built from behind the counter. Customers kept asking the same questions — I realized intuition wasn't enough. Scraped, cleaned, and modeled flavor profiles into a real recommendation engine.</p>
      <p class="proj-finding">The best recommenders aren't built by engineers. They're built by people who worked the domain.</p>
      <div class="proj-stack">
        <span class="stack-pill">Python</span>
        <span class="stack-pill">NLP</span>
        <span class="stack-pill">Scraping</span>
      </div>
    </a>
    <a class="proj-card" href="https://github.com/brianphu2310/UFC_STANCE_AND_HANDEDNESS_INTELLIGENCE" target="_blank" rel="noopener">
      <span class="proj-tag">Sports Analytics</span>
      <h2 class="proj-title">UFC Stance × Handedness Intelligence</h2>
      <p class="proj-desc">117 fighters. Analyzed how stance and hand dominance interact — a question coaches argue about constantly but rarely quantify. Applied statistical testing to separate signal from folklore.</p>
      <p class="proj-finding">Most beliefs about southpaw advantage are survivorship bias. The numbers tell a different story.</p>
      <div class="proj-stack">
        <span class="stack-pill">Python</span>
        <span class="stack-pill">Statistics</span>
        <span class="stack-pill">Tableau</span>
      </div>
    </a>
  </div>

  <p class="section-label">Approach</p>

  <div class="philosophy">
    <span class="philosophy-tag">How I work</span>
    <p class="philosophy-quote">"If I can't measure it, I don't trust my opinion on it."</p>
    <p class="philosophy-sub">Every project starts with Observe → Orient → Decide → Act. Not because someone taught me the framework — because when I was making coffee, I learned that fast feedback loops beat slow deliberation. Data is just a way to run those loops faster and with less guessing.</p>
  </div>

  <p class="section-label">Stack</p>

  <div class="skills-grid">
    <div class="skill-cell">
      <div class="category">Databases</div>
      <ul class="skill-list">
        <li class="primary">PostgreSQL</li>
        <li>SQL</li>
        <li>Data modeling</li>
      </ul>
    </div>
    <div class="skill-cell">
      <div class="category">Visualization</div>
      <ul class="skill-list">
        <li class="primary">Tableau</li>
        <li>Matplotlib</li>
        <li>Seaborn</li>
      </ul>
    </div>
    <div class="skill-cell">
      <div class="category">Analysis</div>
      <ul class="skill-list">
        <li class="primary">Python</li>
        <li>Pandas / NumPy</li>
        <li>Statistics</li>
      </ul>
    </div>
    <div class="skill-cell">
      <div class="category">Methods</div>
      <ul class="skill-list">
        <li class="primary">OODA Loop</li>
        <li>HHI Analysis</li>
        <li>Web Scraping</li>
      </ul>
    </div>
  </div>

  <div class="contact">
    <div>
      <p class="contact-title">Open to opportunities.</p>
      <p class="contact-sub">Data analyst roles in Sydney — supply chain, operations, or anywhere the data is messy and the stakes are real. I work best when I own a problem end-to-end.</p>
    </div>
    <div class="contact-links">
      <a href="mailto:brianphu2310@gmail.com">brianphu2310@gmail.com</a>
      <a href="https://linkedin.com/in/brianphu2310" target="_blank" rel="noopener">linkedin/brianphu2310</a>
      <a href="https://github.com/brianphu2310" target="_blank" rel="noopener">github/brianphu2310</a>
    </div>
  </div>

</div>
</body>
</html>
