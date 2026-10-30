"""GroundWerx REVIEW POSTS: share a real Google review on Facebook/Instagram.
Look 13 in the library. Rules live in strategy.md ("Google review posts"); the review queue is calendar/reviews.md.

Usage: python3 templates/review_posts.py [key ...]   (no args = render every review in REVIEWS)
Output: images/reviews/review_<key>.jpg at 1080x1350.

Compliance built into this template (do not remove):
- Review text is passed in exactly as written on Google. Only trim with an ellipsis (…), never reword or fix typos.
- Official Google "G" logo (brand/third_party/google_g.png, unmodified, from gstatic) is shown at the same height as
  our wordmark, and is kept away from the stars (stars live inside the card, the logo sits under it).
- Copy says "on Google", never "Google rating" / "Google-rated". No overall rating or review count is shown
  (that would need an "as of" date).
- Reviewer shown as initial avatar + first name and last initial. No profile photos.
"""
import asyncio, pathlib, sys, html
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
OUT = ROOT / "images/reviews"; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / "templates/_tmp_reviews"; TMP.mkdir(exist_ok=True)
LOGO = (ROOT / "brand/logo-wordmark.png").as_uri()
GLOGO = (ROOT / "brand/third_party/google_g.png").as_uri()
src = Image.open(ROOT / "brand/logo-wordmark.png").convert("L")
ink = Image.new("RGBA", src.size, (11, 11, 11, 255)); ink.putalpha(src.point(lambda v: min(255, int(v * 1.6))))
ink.save(TMP / "logo_ink.png"); LOGO_INK = (TMP / "logo_ink.png").as_uri()

# Real reviews from GroundWerx Digital's Google Business Profile (copied Oct 29, 2026).
# text = exactly what we show (verbatim, or a verbatim excerpt with …). "" = star-only rating.
REVIEWS = {
    "keyling": dict(name="Keyling P.", initial="K", color="#00897B", month="October 2026", theme="dark",
        headline="fast, professional,<br><i>and it shows.</i>",
        text="Working with Cade and the Groundwex team was an outstanding experience! They were incredibly fast, "
             "professional, and communicative throughout the entire process. They kept me updated, listened to my "
             "needs, and did an amazing job bringing my vision for my website to life. …"),
    "trey": dict(name="Trey H.", initial="T", color="#795548", month="October 2026", theme="cream",
        headline="changes made<br><i>quickly.</i>",
        text="Very knowledgeable and was very easy to work with. Website looks amazing and he is able to make any "
             "changes very quickly."),
    "nick": dict(name="Nick F.", initial="N", color="#D81B60", month="October 2026", theme="gold",
        headline="great work,<br><i>great results.</i>",
        text="We’ve had a great experience working with Groundwerx Digital for Fox Heating & Air. Their "
             "communication has been great, and we’ve been really happy with both the work and the results. "
             "Highly recommend them to other business owners!"),
    "nerea": dict(name="Nerea", initial="N", color="#5E35B1", month="October 2026", theme="dark",
        headline="another one<br><i>on Google.</i>", text=""),
}

THEMES = {  # background, headline color, accent, label color, logo variant, footer text color
    "dark":  ("radial-gradient(ellipse 900px 700px at 80% 0%,#2a2416,#0B0B0B 65%)", "#F2EEE4", "#D9BF72", "#BA9941", "dark", "#CFC9BA"),
    "cream": ("#F2EEE4", "#0B0B0B", "#8a6d24", "#8a6d24", "ink", "#3b362c"),
    "gold":  ("linear-gradient(160deg,#D9BF72,#BA9941 70%)", "#0B0B0B", "#0B0B0B", "#2a2416", "ink", "#1d1a12"),
}

STAR = '<svg viewBox="0 0 24 24" width="40" height="40"><path fill="#FBBC04" d="M12 2.6l2.9 6.2 6.7.7-5 4.6 1.4 6.6L12 17.3 6 20.7l1.4-6.6-5-4.6 6.7-.7z"/></svg>'

def font_css():
    ff = lambda fam, f, w, st="normal": f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{f})}}"
    return "\n".join([ff("CG", "cormorant-garamond-latin-700-normal.woff2", 700),
                      ff("CG", "cormorant-garamond-latin-700-italic.woff2", 700, "italic"),
                      ff("In", "inter-latin-400-normal.woff2", 400), ff("In", "inter-latin-500-normal.woff2", 500),
                      ff("In", "inter-latin-600-normal.woff2", 600), ff("In", "inter-latin-700-normal.woff2", 700)])

def review_post(r):
    bg, hc, acc, lab, logo, foot = THEMES[r["theme"]]
    text = html.escape(r["text"])
    n = len(r["text"])
    size = 44 if n < 160 else 38 if n < 260 else 33          # auto-fit long reviews
    body = (f'<div style="margin-top:34px;font:400 {size}px/1.45 In;color:#202124">{text}</div>' if text else "")
    lg = f'<img style="position:absolute;left:80px;bottom:70px;height:56px;{"mix-blend-mode:lighten" if logo=="dark" else ""}" src="{LOGO if logo=="dark" else LOGO_INK}">'
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{font_css()}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:1080px;height:1350px;overflow:hidden}}
</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:{bg};font-family:In">
  <div style="position:absolute;left:80px;top:96px;right:80px">
    <div style="font:600 22px In;letter-spacing:.3em;color:{lab};text-transform:uppercase">from our google reviews</div>
    <div style="font:700 96px/0.98 CG;color:{hc};margin-top:22px">{r["headline"].replace("<i>", f'<i style="color:{acc}">')}</div>
  </div>
  <div style="position:absolute;left:80px;right:80px;top:390px;bottom:250px;display:flex;align-items:center">
  <div id=card style="width:100%;background:#fff;border-radius:28px;
       padding:52px 56px 56px;box-shadow:0 30px 70px rgba(0,0,0,.35)">
    <div style="display:flex;align-items:center;gap:26px">
      <div style="width:96px;height:96px;border-radius:50%;background:{r["color"]};color:#fff;display:flex;align-items:center;
           justify-content:center;font:500 48px In">{r["initial"]}</div>
      <div><div style="font:600 38px In;color:#202124">{html.escape(r["name"])}</div>
           <div style="display:flex;align-items:center;gap:4px;margin-top:10px">{STAR*5}
             <span style="font:400 28px In;color:#5f6368;margin-left:16px">{r["month"]}</span></div></div>
    </div>
    {body}
  </div></div>
  <div id=gl style="position:absolute;left:80px;right:80px;bottom:170px;display:flex;align-items:center;gap:20px">
    <img src="{GLOGO}" style="height:56px;width:56px;background:#fff;border-radius:50%;padding:6px">
    <div style="font:500 28px In;color:{foot}">Review on Google, shared with permission</div>
  </div>
  {lg}
</div></body></html>"""

async def main():
    only = sys.argv[1:]
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for key, r in REVIEWS.items():
            if only and key not in only: continue
            f = TMP / f"{key}.html"; f.write_text(review_post(r))
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            # layout check: card must not run into the Google line
            card = await pg.eval_on_selector("#card", "e=>e.getBoundingClientRect().bottom")
            gl = await pg.eval_on_selector("#gl", "e=>e.getBoundingClientRect().top")
            assert card + 30 < gl, f"{key}: review card overlaps the Google line ({card:.0f} vs {gl:.0f}); shorten the excerpt"
            png = TMP / f"{key}.png"; await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(OUT / f"review_{key}.jpg", quality=86); print("wrote", key)
        await b.close()

if __name__ == "__main__":
    asyncio.run(main())
