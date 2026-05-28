import feedparser
from datetime import datetime, timedelta

FEEDS = {
    "Inc42":       "https://inc42.com/feed/",
    "YourStory":   "https://yourstory.com/feed",
    "Entrackr":    "https://entrackr.com/feed/",
    "StartupTalky":"https://startuptalky.com/feed/",
    "SutraHR":     "https://sutrahr.com/feed/",
}

FUNDING_KEYWORDS = [
    "funded", "funding", "raises", "raised", "investment", "investor",
    "series a", "series b", "series c", "seed round", "pre-seed",
    "crore", "million", "billion", "valuation", "startup india",
]

def is_funding_related(text):
    text_lower = text.lower()
    return any(kw in text_lower for kw in FUNDING_KEYWORDS)

def fetch_funded_brands(hours=24):
    cutoff = datetime.now() - timedelta(hours=hours)
    results = []

    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6])

                title   = entry.get("title", "")
                summary = entry.get("summary", "")

                if is_funding_related(title) or is_funding_related(summary):
                    if published is None or published >= cutoff:
                        snippet = summary[:220] + "..." if len(summary) > 220 else summary
                        results.append({
                            "source":    source,
                            "title":     title,
                            "link":      entry.get("link", ""),
                            "summary":   snippet,
                            "published": published.strftime("%d %b %Y, %I:%M %p") if published else "Unknown",
                        })
        except Exception as e:
            print(f"[scraper] Error fetching {source}: {e}")

    return results
