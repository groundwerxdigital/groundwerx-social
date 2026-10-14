"""Render GroundWerx posts for the week of Oct 19-23, 2026.
Usage: python3 templates/week3_build.py
Outputs 1080x1350 JPGs to images/2026-10-w3/.
"""
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
TMP = ROOT / "templates/_tmp"; TMP.mkdir(exist_ok=True)
W3 = ROOT / "images/2026-10-w3"; W3.mkdir(parents=True, exist_ok=True)

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

# ---------- Mon Oct 19: dark editorial carousel (6), answering a 1-star review ----------
N = 6
POSTS[W3 / "p1_review_reply_1.jpg"] = page("""<div class=kicker style="margin-top:120px">quick win &middot; save this</div>
<div class=h style="font-size:250px;margin-top:70px;color:var(--gold2);line-height:1">1<span style="font-size:170px;vertical-align:12px">&#9733;</span></div>
<div class=h style="font-size:124px;margin-top:30px">got a bad review?<br><em>here's how<br>to answer it.</em></div>
<div class=rule></div>
<div class=body style="max-width:800px">four steps. no panic, no firing back.</div>""", "dark", "<span class=swipe>swipe &rarr;</span>")
steps = [
 ("wait an hour.", "reply when you're calm, not when you're mad. then answer within a day or two."),
 ("thank them.<br><em>own what's yours.</em>", "if you dropped the ball, say so. if you didn't, stay polite and stick to the facts."),
 ("take it offline.", "give them a name and a number. &ldquo;call me directly. I want to make this right.&rdquo; leave job details and personal info out of it."),
 ("remember<br><em>who's reading.</em>", "your reply is for the next customer as much as this one. calm and professional says a lot about how you'd treat them."),
]
for i, (h, b) in enumerate(steps, 2):
    POSTS[W3 / f"p1_review_reply_{i}.jpg"] = page(f"""<div class=kicker style="margin-top:110px">step {i - 1} of 4</div>
<div class=h style="font-size:300px;margin-top:20px;color:var(--gold);line-height:.85">{i - 1}</div>
<div class=h style="font-size:118px;margin-top:40px">{h}</div>
<div class=rule></div>
<div class=body style="max-width:820px;font-size:38px">{b}</div>""", "dark", f"{i} / {N}")
POSTS[W3 / "p1_review_reply_6.jpg"] = page("""<div class=kicker style="margin-top:120px">want a second set of eyes?</div>
<div class=h style="font-size:120px;margin-top:40px">free 15-minute call<br><em>with tyler and cade.</em></div>
<div class=rule></div>
<div class=body style="max-width:820px">we'll look at your google profile, your reviews and your website with you.</div>
<div style="margin-top:50px;display:inline-block;border:2px solid var(--gold);padding:28px 40px">
<div style="font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>""", "dark", "6 / 6")

# ---------- Tue Oct 20: cream background + phone mock, does your profile look abandoned ----------
def house(sky1, sky2, wall, roofc, x):
    return f"""<svg viewBox="0 0 160 120" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" style="filter:saturate(.45) sepia(.25)">
<defs><linearGradient id="g{x}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky1}"/><stop offset="1" stop-color="{sky2}"/></linearGradient></defs>
<rect width="160" height="120" fill="url(#g{x})"/><rect x="0" y="96" width="160" height="24" fill="#6f7f5e"/>
<rect x="34" y="62" width="92" height="40" fill="{wall}"/><polygon points="24,64 80,26 136,64" fill="{roofc}"/>
<rect x="70" y="78" width="18" height="24" fill="#3b3b3b"/>
<rect x="44" y="72" width="16" height="13" fill="#cfe3f2"/><rect x="100" y="72" width="16" height="13" fill="#cfe3f2"/></svg>"""
PHONE_CSS = """
.phone{position:absolute;left:96px;top:380px;width:500px;height:800px;border-radius:64px;background:#1b1b1b;padding:15px;box-shadow:0 30px 70px rgba(0,0,0,.28)}
.scr{position:relative;width:100%;height:100%;border-radius:50px;background:#fff;overflow:hidden;color:#1f1f1f;font-family:In}
.isl{position:absolute;top:14px;left:50%;transform:translateX(-50%);width:116px;height:32px;border-radius:20px;background:#111}
.sb{display:flex;justify-content:space-between;padding:19px 32px 0;font-weight:600;font-size:18px}
.srch{margin:24px 18px 0;height:56px;border-radius:30px;background:#f1f3f4;display:flex;align-items:center;gap:14px;padding:0 22px;font-size:20px}
.tabs{display:flex;gap:24px;padding:14px 24px 0;font-size:16px;color:#5f6368;border-bottom:1px solid #e3e3e3}
.tabs span{padding-bottom:11px} .tabs .on{color:#1f1f1f;font-weight:600;border-bottom:3px solid #1f1f1f}
.card{padding:18px 22px 0}
.nm{font-size:29px;font-weight:600;letter-spacing:-.01em}
.rt{margin-top:7px;font-size:17px;color:#5f6368;display:flex;align-items:center;gap:6px}
.rt b{color:#1f1f1f;font-weight:500} .st{color:#f2a400;letter-spacing:1px;font-size:18px}
.op{margin-top:5px;font-size:17px;color:#5f6368} .op .g{color:#188038;font-weight:600}
.sec{margin-top:13px;padding-top:11px;border-top:1px solid #e3e3e3;font-size:15px;font-weight:600;color:#1f1f1f;display:flex;align-items:center;justify-content:space-between}
.photos{display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:62px 62px;gap:5px;margin-top:10px;border-radius:12px;overflow:hidden}
.photos div:first-child{grid-row:1/3}
.upd{margin-top:10px;background:#f6f6f6;border-radius:12px;padding:14px 16px;font-size:16px;line-height:1.4;color:#3c4043}
.upd .when{font-size:14px;color:#80868b;margin-bottom:4px}
.rv{margin-top:10px;display:flex;gap:12px}
.av{flex:none;width:36px;height:36px;border-radius:50%;background:#5b8fd6;color:#fff;font-weight:600;display:flex;align-items:center;justify-content:center;font-size:16px}
.rv .t{font-size:16px;line-height:1.4;color:#3c4043}
.old{color:#c5221f;font-weight:600}
.bd{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:#BA9941;color:#0B0B0B;font-weight:700;font-size:16px;flex:none;font-family:In}
.co{position:absolute;left:640px;width:350px;display:flex;gap:18px}
.co .bd{width:46px;height:46px;font-size:22px;margin-top:-4px}
.co .k{font-weight:600;font-size:30px;color:#0B0B0B;line-height:1.15}
.co .d{margin-top:8px;font-size:23px;line-height:1.4;color:#3b382f}
"""
def co(top, n, k, d):
    return f'<div class="co" style="top:{top}px"><div class="bd">{n}</div><div><div class="k">{k}</div><div class="d">{d}</div></div></div>'
POSTS[W3 / "p2_phone_quiet_profile.jpg"] = page(f"""<style>{PHONE_CSS}</style>
<div class=kicker style="margin-top:0">what customers notice</div>
<div class=h style="font-size:92px;margin-top:24px">does your profile look<br><em>like you're still open?</em></div>
<div class=phone><div class=scr><div class=isl></div>
 <div class=sb><span>9:41</span><span>&#9679;&#9679;&#9679; &#9646;</span></div>
 <div class=srch><svg viewBox="0 0 24 24" width="22" height="22" fill="#5f6368"><path d="M15.5 14h-.8l-.3-.3A6.5 6.5 0 1 0 14 15.5l.3.3v.8l5 5 1.5-1.5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>plumber near me</div>
 <div class=tabs><span class=on>All</span><span>Maps</span><span>Images</span><span>Reviews</span></div>
 <div class=card>
  <div class=nm>Example Plumbing Co.</div>
  <div class=rt><b>4.6</b><span class=st>&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>(31) &middot; Plumber</span></div>
  <div class=op><span class=g>Open</span> &middot; Closes 5 PM</div>
  <div class=sec><span>Updates from the business</span><span class=bd>1</span></div>
  <div class=upd><div class=when>Posted <span class=old>2 years ago</span></div>Happy holidays from our crew! Now booking for spring.</div>
  <div class=sec><span>Photos</span><span class=bd>2</span></div>
  <div class=photos><div>{house("#b9c9d6","#e9eef2","#d8cdbb","#5a4a3e",1)}</div><div>{house("#c9c1b0","#efe9de","#cbbfa9","#4a4e55",2)}</div><div>{house("#bcc6cc","#eceff1","#c6c6c6","#3d4247",3)}</div></div>
  <div class=sec><span>Reviews</span><span class=bd>3</span></div>
  <div class=rv><div class=av>M</div><div class=t><span class=st>&#9733;&#9733;&#9733;&#9733;&#9733;</span> &nbsp;<span class=old>8 months ago</span><br>Showed up on time and fixed it.</div></div>
 </div>
</div></div>
{co(470, 1, "last update:<br>2 years ago", "looks like nobody's minding the shop.")}
{co(690, 2, "newest photo:<br>years old", "nothing from the jobs you did this year.")}
{co(910, 3, "latest review:<br>8 months ago", "makes people wonder if you're still busy.")}
""", "cream", "example profile")

# ---------- Wed Oct 21: giant-number stat, how we work ----------
rows = [("0", "weekly homework."), ("0", "long contracts. we're month-to-month."),
        ("1", "straight report a month: calls, booked jobs, reviews earned.")]
rl = "".join(f"""<div style="display:flex;gap:40px;align-items:center;padding:20px 0;border-top:1.5px solid var(--line)">
<div class=h style="font-size:110px;color:var(--gold2);width:80px;line-height:.9;text-align:center">{n}</div>
<div style="font-size:34px;line-height:1.35;color:var(--paper);font-weight:500">{t}</div></div>""" for n, t in rows)
POSTS[W3 / "p3_bignumber_zero.jpg"] = page(f"""<div class=kicker style="margin-top:10px">how we work</div>
<div class=h style="font-size:320px;margin-top:0;color:var(--gold2);line-height:.9;letter-spacing:-.03em">0</div>
<div class=h style="font-size:100px;margin-top:10px">dashboards<br><em>you'll have to log into.</em></div>
<div style="margin-top:44px">{rl}</div>""", "dark", "done for you")

# ---------- Thu Oct 22: this vs that (cream), a page for every service ----------
left = ["roofing, gutters, siding, repairs: all in one list", "one paragraph covers everything", "customer has to dig to see if you do their job", "one call button, at the bottom"]
right = ["gutter repair gets its own page", "what you do and the towns you cover", "photos of those jobs", "a call button right there"]
def col(items, good):
    mark = '<span style="color:#8a6f28;font-weight:700">&#10003;</span>' if good else '<span style="color:#a39d8f">&#10005;</span>'
    color = "var(--ink)" if good else "#7d776a"
    return "".join(f"""<div style="display:flex;gap:16px;padding:22px 0;border-bottom:1.5px solid {'rgba(138,111,40,.35)' if good else 'rgba(11,11,11,.1)'};font-size:29px;line-height:1.3;color:{color}">
<div style="width:26px;flex:none">{mark}</div><div>{t}</div></div>""" for t in items)
POSTS[W3 / "p4_thisvsthat_service_pages.jpg"] = page(f"""<div class=kicker style="margin-top:0">website quick win</div>
<div class=h style="font-size:100px;margin-top:28px">one &ldquo;services&rdquo; page<br><em>vs.</em> a page for<br>every service.</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:56px">
 <div style="background:#e8e3d6;border:1.5px solid rgba(11,11,11,.12);padding:30px 30px 12px">
  <div style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;color:#7d776a">one list</div>
  <div style="margin-top:8px">{col(left, False)}</div></div>
 <div style="background:#fbf8f0;border:2px solid #BA9941;padding:30px 30px 12px">
  <div style="font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;color:#8a6f28">a page each</div>
  <div style="margin-top:8px">{col(right, True)}</div></div>
</div>""", "cream", "", frame=False)

# ---------- Fri Oct 23: quote card on solid gold, From Tyler ----------
POSTS[W3 / "p5_quote_tyler_gold.jpg"] = page("""<div class=h style="font-size:330px;line-height:.7;color:var(--ink);margin-top:70px">&ldquo;</div>
<div class=h style="font-size:104px;margin-top:10px;line-height:1.02">you didn't get into<br>the trades to do<br>marketing at 9pm.<br><em>that's what<br>we're for.</em></div>
<div class=rule style="margin-top:56px"></div>
<div style="font-weight:600;font-size:32px;color:var(--ink)">Tyler Maas</div>
<div style="font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:#2a2416;margin-top:10px;font-weight:600">co-founder, groundwerx digital</div>""",
"goldbg", "from tyler")

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
