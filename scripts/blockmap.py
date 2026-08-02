#!/usr/bin/env python3
"""Crawl every ampy.se sitemap URL and extract the ordered sequence of known
Bricks block fingerprints (CSS class names) -> data/block-map.json.
Also extracts <title>, meta description, H1s, word count, and saves raw HTML
for a representative subset."""
import json, os, re, sys, time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from xml.etree import ElementTree as ET

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SM_DIR = os.path.join(BASE, "data", "sitemaps")
OUT = os.path.join(BASE, "data", "block-map.json")
HTML_DIR = os.path.join(BASE, "data", "pages")

# fingerprint -> canonical block name (searched as substring in class attributes)
FINGERPRINTS = [
    ("hero_2__container", "Hero_2"),
    ("ampy_quote_form_wrapper", "Hero_2-old-form"),
    ("ampy-form-root", "Hero_2-aof-form"),
    ("hero-1__floating-banner", "Hero-1"),
    ("ampy-elfirma", "MiniMenu-Elfirma"),
    ("laddbox-hero__container", "AlternativHero"),
    ("main-contact__global-form", "MainContact"),
    ("data-mf=\"card\"", "MainContact-card"),
    ("main-cta-__container", "MainCTA"),
    ("mikro_cta", "MikroCTA"),
    ("blue-cta-__container", "BlueCTA"),
    ("content-block__container", "ContentBlock"),
    ("ampy-testimonials", "Testimonials"),
    ("faq-__container", "FAQ"),
    ("faq-__accordion", "FAQ-accordion"),
    ("our-process__container", "VarProcess"),
    ("rot__main-heading", "ROT-block"),
    ("home-insurance__container", "HomeInsurance"),
    ("gron-teknik__container", "GronTeknik"),
    ("visste-du-att__container", "VissteDuAtt"),
    ("certificates__container", "Certificates"),
    ("footer-seo__container", "FooterSEO"),
    ("team__container", "TeamSection"),
    ("news__container", "NewsBlock"),
    ("map__container", "MapBlock"),
    ("metrics__container", "Metrics"),
    ("about-us-metrics", "AboutMetrics"),
    ("visual-cta__container", "VisualCTA"),
    ("product-hero__block", "ProductHero"),
    ("product__product-grid", "ProductGrid"),
    ("ce-block__container", "CEBlock"),
    ("ampy-tack", "ThankYou"),
    ("brxe-post-content", "ArticleBody"),
    ("ampy-toc-wrapper", "ArticleTOC"),
    ("ampy-editorial-avatars", "EditorialByline"),
    ("post-card__image-wrap", "ArticleCards"),
    ("ampy-calc", "Calculator-UI"),
    ("prefooter__container", "Prefooter"),
    ("mega-anchor", "Header"),
]

SAVE_HTML_PATTERNS = [
    "ampy.se/$", "elservice/?$", "elektriker/?$", "eljour/?$", "batterilagring",
    "laddboxar", "om-oss", "kontakt", "thank-you", "energikalkylator",
    "elcentral-kollen", "laddboxkalkylator", "batterikalkylator",
]

def urls_from_sitemaps():
    urls = []
    for f in sorted(os.listdir(SM_DIR)):
        if not f.endswith(".xml"):
            continue
        tree = ET.parse(os.path.join(SM_DIR, f))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in tree.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            urls.append((f.replace("-sitemap1.xml", ""), loc.text.strip()))
    return urls

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36 AmpyCROAudit"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "ignore")

def analyze(category, url):
    try:
        html = fetch(url)
    except Exception as e:
        return {"category": category, "url": url, "error": str(e)}
    hits = []
    for fp, name in FINGERPRINTS:
        idx = html.find(fp)
        if idx >= 0:
            hits.append((idx, name))
    hits.sort()
    # dedupe consecutive same-name
    seq, seen_at = [], {}
    for idx, name in hits:
        if name not in seen_at:
            seen_at[name] = idx
            seq.append(name)
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', html)
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    h1s = [re.sub(r"<[^>]+>", "", h).strip()[:120] for h in h1s][:3]
    text = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", html, flags=re.S)
    words = len(text.split())
    slug = re.sub(r"[^a-z0-9]+", "-", url.replace("https://ampy.se", "").strip("/").lower()) or "home"
    for pat in SAVE_HTML_PATTERNS:
        if re.search(pat, url):
            with open(os.path.join(HTML_DIR, slug[:80] + ".html"), "w") as fh:
                fh.write(html)
            break
    return {
        "category": category, "url": url,
        "title": (title.group(1).strip() if title else ""),
        "meta_description": (desc.group(1) if desc else ""),
        "h1": h1s, "word_count": words, "size_kb": len(html) // 1024,
        "blocks": seq,
    }

def main():
    os.makedirs(HTML_DIR, exist_ok=True)
    urls = urls_from_sitemaps()
    print(f"{len(urls)} URLs")
    results = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(analyze, c, u): u for c, u in urls}
        for i, fut in enumerate(as_completed(futs)):
            results.append(fut.result())
            if (i + 1) % 25 == 0:
                print(f"  {i+1}/{len(urls)}")
    results.sort(key=lambda r: (r["category"], r["url"]))
    with open(OUT, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    errs = [r for r in results if r.get("error")]
    print(f"done. {len(results)} pages, {len(errs)} errors -> {OUT}")
    for r in errs[:10]:
        print("ERR", r["url"], r["error"])

if __name__ == "__main__":
    main()
