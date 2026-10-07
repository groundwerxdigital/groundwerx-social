"""Render GroundWerx posts for Thu Oct 8 (gap fill) and the week of Oct 12-16, 2026.
Usage: python3 templates/week2_build.py
Outputs 1080x1350 JPGs to images/2026-10-w1/ (Oct 8) and images/2026-10-w2/ (Oct 12-16).
"""
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
TMP = ROOT / "templates/_tmp"; TMP.mkdir(exist_ok=True)
W1 = ROOT / "images/2026-10-w1"; W2 = ROOT / "images/2026-10-w2"; W2.mkdir(parents=True, exist_ok=True)

# Logo variants: original (gold on black, use with mix-blend lighten) and a dark-ink version
# with transparency for cream / gold backgrounds.
LOGO = (ROOT / "brand/logo-wordmark.png").as_uri()
src = Image.open(ROOT / "brand/logo-wordmark.png").convert("L")
alpha = src.point(lambda v: min(255, int(v * 1.6)))
ink = Image.new("RGBA", src.size, (11, 11, 11, 255)); ink.putalpha(alpha)
ink.save(TMP / "logo_ink.png"); LOGO_INK = (TMP / "logo_ink.png").as_uri()

CSS = f"""
@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond-latin-600-normal.woff2)}}
@font-face{{font-family:CG;font-weight:700;src:url({F}/cormorant-garamond-latin-700-normal.woff2)}}
@font-face{{font-family:CG;font-weight:700;font-style:italic;src:url({F}/cormorant-garamond-latin-700-italic.woff2)}}
@font-face{{font-family:In;font-weight:400;src:url({F}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:In;font-weight:500;src:url({F}/inter-latin-500-normal.woff2)}}
@font-face{{font-family:In;font-weight:600;src:url({F}/inter-latin-600-normal.woff2)}}
@font-face{{font-family:In;font-weight:700;src:url({F}/inter-latin-700-normal.woff2)}}
:root{{--gold:#BA9941;--gold2:#D9BF72;--ink:#0B0B0B;--paper:#F2EEE4;--mute:#9A9483;--line:rgba(186,153,65,.35)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:var(--ink)}}
.page{{position:relative;width:1080px;height:1350px;padding:110px 96px 0;font-family:In;overflow:hidden}}
.dark{{color:var(--paper);background:radial-gradient(ellipse 900px 700px at 85% -10%,rgba(186,153,65,.13),transparent 60%),var(--ink)}}
.cream{{color:var(--ink);background:var(--paper)}}
.goldbg{{color:var(--ink);background:linear-gradient(160deg,#D9BF72 0%,#BA9941 70%)}}
.frame::before{{content:"";position:absolute;inset:36px;border:1.5px solid var(--line);pointer-events:none}}
.cream.frame::before{{border-color:rgba(11,11,11,.18)}}
.goldbg.frame::before{{border-color:rgba(11,11,11,.3)}}
.kicker{{font-weight:600;font-size:22px;letter-spacing:.32em;text-transform:uppercase;color:var(--gold)}}
.cream .kicker{{color:#8a6f28}} .goldbg .kicker{{color:var(--ink)}}
.h{{font-family:CG;font-weight:700;line-height:.98;letter-spacing:-.01em;font-variant-numeric:lining-nums}}
.h em{{font-style:italic;color:var(--gold2)}}
.cream .h em{{color:#8a6f28}} .goldbg .h em{{color:var(--ink)}}
.body{{font-size:34px;line-height:1.45;color:#CFC9BA}}
.cream .body{{color:#3b382f}} .goldbg .body{{color:#1d1a12}}
.body b{{font-weight:600;color:var(--paper)}} .cream .body b,.goldbg .body b{{color:var(--ink)}}
.rule{{width:120px;height:3px;background:var(--gold);margin:44px 0}}
.goldbg .rule{{background:var(--ink)}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;align-items:center;justify-content:space-between}}
.foot img{{height:58px}} .dark .foot img{{mix-blend-mode:lighten}}
.foot .r{{font-size:22px;letter-spacing:.24em;color:var(--mute);text-transform:uppercase;font-weight:500}}
.cream .foot .r{{color:#7d776a}} .goldbg .foot .r{{color:#2a2416}}
.swipe{{color:var(--gold)}}
"""

def page(inner, theme="dark", right="", frame=True):
    logo = LOGO if theme == "dark" else LOGO_INK
    cls = f"page {theme}" + (" frame" if frame else "")
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head>
<body><div class="{cls}">{inner}<div class=foot><img src="{logo}"><div class=r>{right}</div></div></div></body></html>"""

POSTS = {}  # path -> html

# ---------- Thu Oct 8: cream background, review timing tip ----------
steps = [("thank them in person.", "right there, before you pack up."),
         ("tell them why it matters.", "reviews help a small business like yours get found."),
         ("text the link right then.", "while they're still standing in the driveway.")]
sl = "".join(f"""<div style="display:flex;gap:30px;align-items:flex-start;padding:24px 0;border-top:1.5px solid rgba(11,11,11,.14)">
<div class=h style="font-size:64px;color:#8a6f28;width:48px;line-height:1">{i}</div>
<div><div style="font-weight:600;font-size:34px;color:var(--ink)">{a}</div>
<div class=body style="font-size:27px;margin-top:4px">{b}</div></div></div>""" for i, (a, b) in enumerate(steps, 1))
POSTS[W1 / "p5_cream_reviews.jpg"] = page(f"""<div class=kicker style="margin-top:20px">review tip</div>
<div class=h style="font-size:112px;margin-top:30px">ask for the review<br><em>before you pull<br>out of the driveway.</em></div>
<div class=body style="margin-top:36px;max-width:820px;font-size:31px">the customer is happiest the minute the job's done. a week later, they've moved on.</div>
<div style="margin-top:36px">{sl}</div>""", "cream", "save this")

# ---------- Mon Oct 12: this vs that, website ----------
left = ["big photo, number buried at the bottom", "slow to load on a phone", "&ldquo;contact us&rdquo; form only", "doesn't say where you work", "stock photos"]
right = ["tap-to-call number up top", "loads fast on a phone", "every service listed", "the towns you serve", "photos of your real jobs"]
def col(items, good):
    mark = '<span style="color:var(--gold2);font-weight:700">&#10003;</span>' if good else '<span style="color:#6d6a62">&#10005;</span>'
    color = "var(--paper)" if good else "#8f8a7d"
    return "".join(f"""<div style="display:flex;gap:16px;padding:24px 0;border-bottom:1.5px solid {'var(--line)' if good else '#262626'};font-size:30px;line-height:1.3;color:{color}">
<div style="width:26px;flex:none">{mark}</div><div>{t}</div></div>""" for t in items)
POSTS[W2 / "p1_thisvsthat_website.jpg"] = page(f"""<div class=kicker style="margin-top:0">check yours on your phone</div>
<div class=h style="font-size:104px;margin-top:28px">a pretty website<br><em>vs.</em> one that<br>books calls.</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:64px">
 <div style="background:#141414;border:1.5px solid #262626;padding:30px 30px 14px">
  <div style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;color:#8f8a7d">just looks nice</div>
  <div style="margin-top:10px">{col(left, False)}</div></div>
 <div style="background:#16130b;border:2px solid var(--gold);padding:30px 30px 14px">
  <div style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold2)">books calls</div>
  <div style="margin-top:10px">{col(right, True)}</div></div>
</div>""", "dark", "", frame=False)

# ---------- Tue Oct 13: quote card, From Tyler ----------
POSTS[W2 / "p2_quote_tyler.jpg"] = page("""<div class=h style="font-size:330px;line-height:.7;color:var(--gold);margin-top:70px">&ldquo;</div>
<div class=h style="font-size:108px;margin-top:10px;line-height:1.02">you shouldn't need<br>a login to know if<br>your marketing<br><em>is working.</em></div>
<div class=rule style="margin-top:60px"></div>
<div style="font-weight:600;font-size:32px;color:var(--paper)">Tyler Maas</div>
<div style="font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);margin-top:10px;font-weight:600">co-founder, groundwerx digital</div>""",
"dark", "from tyler")

# ---------- Wed Oct 14: myth vs fact carousel (6), cream ----------
N = 6
myths = [
 ("&ldquo;word of mouth is all I need.&rdquo;", "even a referral googles you before they call. if your profile looks thin, they keep looking."),
 ("&ldquo;happy customers leave reviews on their own.&rdquo;", "a lot of them won't unless you ask. a quick text after the job goes a long way."),
 ("&ldquo;my website's a few years old, but it's fine.&rdquo;", "open it on your phone. if you have to pinch and zoom to find your number, it's costing you calls."),
 ("&ldquo;marketing means a long contract.&rdquo;", "not with us. month-to-month. if it's not worth it to you, you leave."),
]
def mslide(i, myth, fact):
    return page(f"""<div class=kicker style="margin-top:110px">myth {i - 1} of 4</div>
<div style="margin-top:40px;display:inline-block;background:var(--ink);color:var(--paper);font-weight:700;font-size:22px;letter-spacing:.3em;padding:12px 22px">MYTH</div>
<div class=h style="font-size:92px;margin-top:30px;color:#6f6a5f;text-decoration:line-through;text-decoration-thickness:4px;text-decoration-color:rgba(138,111,40,.7)">{myth}</div>
<div style="margin-top:60px;display:inline-block;background:var(--gold);color:var(--ink);font-weight:700;font-size:22px;letter-spacing:.3em;padding:12px 22px">FACT</div>
<div class=h style="font-size:72px;margin-top:30px;line-height:1.08">{fact}</div>""", "cream", f"{i} / {N}")
POSTS[W2 / "p3_myth_1.jpg"] = page(f"""<div class=kicker style="margin-top:130px">for contractors</div>
<div class=h style="font-size:250px;margin-top:30px;color:#8a6f28;line-height:.85">4</div>
<div class=h style="font-size:128px;margin-top:20px">marketing myths<br><em>contractors still<br>believe.</em></div>
<div class=rule style="background:#8a6f28"></div>
<div class=body style="max-width:780px">heard every one of these on a call. here's the truth.</div>""", "cream", "<span style='color:#8a6f28'>swipe &rarr;</span>")
for i, (m, f) in enumerate(myths, 2):
    POSTS[W2 / f"p3_myth_{i}.jpg"] = mslide(i, m, f)
POSTS[W2 / "p3_myth_6.jpg"] = page("""<div class=kicker style="margin-top:120px">not sure where you stand?</div>
<div class=h style="font-size:124px;margin-top:40px">15 minutes.<br><em>we'll show you<br>what we'd fix first.</em></div>
<div class=rule style="background:#8a6f28"></div>
<div class=body>your google profile, your reviews and your website, looked at together. free.</div>
<div style="margin-top:50px;display:inline-block;background:var(--ink);padding:28px 40px">
<div style="font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>""", "cream", "6 / 6")

# ---------- Thu Oct 15: giant-number stat, after-hours call ----------
POSTS[W2 / "p4_bignumber_1047.jpg"] = page("""<div class=kicker style="margin-top:20px">after hours</div>
<div class=h style="font-size:300px;margin-top:10px;color:var(--gold2);line-height:.9;letter-spacing:-.03em">10:47<span style="font-size:120px;letter-spacing:0">pm</span></div>
<div class=h style="font-size:84px;margin-top:30px">a pipe bursts.<br><em>they call three plumbers.</em></div>
<div class=body style="margin-top:36px;font-size:32px">two go to voicemail. one texts back inside a minute:</div>
<div style="margin-top:26px;max-width:700px;background:#1c1c1e;border-radius:34px 34px 34px 8px;padding:26px 32px;font-size:30px;line-height:1.4;color:#F2EEE4">
Sorry we missed you. What's going on? We'll call you right back.</div>
<div class=h style="font-size:64px;margin-top:44px">who do you think <em>they wait for?</em></div>""",
"dark", "example")

# ---------- Fri Oct 16: solid gold, free consult ----------
POSTS[W2 / "p5_gold_consult.jpg"] = page("""<div class=kicker style="margin-top:40px">free &middot; 15 minutes</div>
<div class=h style="font-size:160px;margin-top:34px">what we'd<br><em>fix first.</em></div>
<div class=rule></div>
<div class=body style="max-width:840px">hop on a call with tyler and cade. we pull up <b>your google profile, your reviews and your website</b> with you.</div>
<div class=body style="max-width:840px;margin-top:24px">you leave with a short list, whether you hire us or not.</div>
<div style="margin-top:44px;display:inline-block;background:var(--ink);padding:26px 40px">
<div style="font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>""",
"goldbg", "book a call")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for out, html in POSTS.items():
            f = TMP / (out.stem + ".html"); f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
            png = TMP / (out.stem + ".png"); await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(out, quality=86); print("wrote", out.relative_to(ROOT))
        await b.close()
    for f in TMP.iterdir(): f.unlink()
    TMP.rmdir()
asyncio.run(main())
