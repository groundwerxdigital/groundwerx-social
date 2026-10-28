import sys
"""Render GroundWerx posts for the week of Nov 2-6, 2026 (Mon Nov 2 carousel was built in week3_build.py).
Usage: python3 templates/week5_build.py
Outputs 1080x1350 JPGs to images/2026-11-w1/.
"""
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
TMP = ROOT / "templates/_tmp"; TMP.mkdir(exist_ok=True)
W5 = ROOT / "images/2026-11-w1"; W5.mkdir(parents=True, exist_ok=True)

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

CTA = """<div style="margin-top:50px;display:inline-block;border:2px solid var(--gold);padding:28px 40px">
<div style="font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>"""

def co(top, n, k, d):
    return f'<div class="co" style="top:{top}px"><div class="bd">{n}</div><div><div class="k">{k}</div><div class="d">{d}</div></div></div>'

# ---------- Tue Nov 3: cream + phone (text thread), missed-call text-back on a job ----------
SMS_CSS = """
.phone{position:absolute;left:96px;top:400px;width:500px;height:770px;border-radius:64px;background:#1b1b1b;padding:15px;box-shadow:0 30px 70px rgba(0,0,0,.28)}
.scr{position:relative;width:100%;height:100%;border-radius:50px;background:#fff;overflow:hidden;color:#1f1f1f;font-family:In}
.isl{position:absolute;top:14px;left:50%;transform:translateX(-50%);width:116px;height:32px;border-radius:20px;background:#111}
.sb{display:flex;justify-content:space-between;padding:19px 32px 0;font-weight:600;font-size:18px}
.hd{text-align:center;padding:22px 0 14px;border-bottom:1px solid #e6e6e6}
.hd .av{width:58px;height:58px;border-radius:50%;background:#BA9941;color:#0B0B0B;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center;margin:0 auto}
.hd .n{margin-top:8px;font-size:17px;font-weight:600}
.th{padding:14px 18px;display:flex;flex-direction:column;gap:12px;font-size:18px;line-height:1.38}
.sys{align-self:center;font-size:14px;color:#8a8a8a;text-align:center}
.miss{align-self:center;display:flex;align-items:center;gap:8px;font-size:15px;color:#c5221f;font-weight:600;background:#fdecea;border-radius:16px;padding:7px 14px}
.out{align-self:flex-end;max-width:80%;background:#0B0B0B;color:#F2EEE4;border-radius:20px 20px 6px 20px;padding:12px 16px}
.in{align-self:flex-start;max-width:80%;background:#ececec;border-radius:20px 20px 20px 6px;padding:12px 16px}
.bd{display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:50%;background:#BA9941;color:#0B0B0B;font-weight:700;font-size:22px;flex:none;font-family:In;margin-top:-4px}
.co{position:absolute;left:640px;width:350px;display:flex;gap:18px}
.co .k{font-weight:600;font-size:30px;color:#0B0B0B;line-height:1.15}
.co .d{margin-top:8px;font-size:23px;line-height:1.4;color:#3b382f}
"""
POSTS[W5 / "p1_phone_textback.jpg"] = page(f"""<style>{SMS_CSS}</style>
<div class=kicker style="margin-top:0">money you're losing</div>
<div class=h style="font-size:96px;margin-top:24px">on a roof when it rings?<br><em>they still hear back.</em></div>
<div class=phone><div class=scr><div class=isl></div>
 <div class=sb><span>11:43</span><span>&#9679;&#9679;&#9679; &#9646;</span></div>
 <div class=hd><div class=av>ER</div><div class=n>Example Roofing</div></div>
 <div class=th>
  <div class=sys>Today 11:42 AM</div>
  <div class=miss>&#8601; Missed call</div>
  <div class=out>Hi, this is Example Roofing. Sorry we missed you, we're on a job. What can we help with?</div>
  <div class=sys>11:43 AM</div>
  <div class=in>Leak over the garage after the storm. Can someone look at it this week?</div>
  <div class=sys>12:58 PM</div>
  <div class=out>Got it. Mike here, just got off the roof. Calling you in 5.</div>
 </div>
</div></div>
{co(480, 1, "the phone rings", "you're up a ladder. it goes to voicemail.")}
{co(700, 2, "they get a text", "within a minute, so the conversation starts while they're still holding the phone.")}
{co(950, 3, "you reply when you're down", "you already know what they need.")}
""", "cream", "example business")

# ---------- Wed Nov 4: dark numbered carousel (6), a normal month with us ----------
N = 6
POSTS[W5 / "p2_month_1.jpg"] = page("""<div class=kicker style="margin-top:130px">behind groundwerx</div>
<div class=h style="font-size:136px;margin-top:60px">you run<br>the jobs.<br><em>we run<br>the rest.</em></div>
<div class=rule></div>
<div class=body style="max-width:820px">here's what &ldquo;done-for-you&rdquo; looks like in a normal month.</div>""", "dark", "<span class=swipe>swipe &rarr;</span>")
steps = [
 ("01", "your google<br>profile", "updates posted, job photos added, hours and info kept right. <b>every week.</b>"),
 ("02", "your<br>reviews", "every finished job triggers a review request. <b>you don't have to remember to ask.</b>"),
 ("03", "your missed<br>calls", "can't pick up? the caller gets a text <b>within a minute.</b>"),
 ("04", "your<br>report", "once a month, straight numbers: <b>calls, booked jobs, reviews earned.</b> no dashboard to log into."),
]
for i, (num, h, b) in enumerate(steps, 2):
    POSTS[W5 / f"p2_month_{i}.jpg"] = page(f"""<div class=h style="font-size:340px;line-height:.8;color:transparent;-webkit-text-stroke:2.5px var(--gold);margin-top:150px">{num}</div>
<div class=h style="font-size:118px;margin-top:40px">{h}</div>
<div class=rule></div>
<div class=body style="max-width:860px;font-size:46px">{b}</div>""", "dark", f"{i} / {N}")
POSTS[W5 / "p2_month_6.jpg"] = page(f"""<div class=kicker style="margin-top:110px">two brothers. one point of contact.</div>
<div class=h style="font-size:112px;margin-top:40px">no account managers.<br><em>no handoffs.</em></div>
<div class=rule></div>
<div class=body style="max-width:840px">month-to-month. free 15-minute call with tyler and cade.</div>
{CTA}""", "dark", "6 / 6")

# ---------- Thu Nov 5: solid gold check-this-today, tap-to-call test ----------
checks = [("is your number at the top of the page?", "not buried in the footer."),
          ("does one tap dial it?", "no copying and pasting."),
          ("is it the right number?", "the one you actually answer.")]
cl = "".join(f"""<div style="display:flex;gap:28px;padding:26px 0;border-top:1.5px solid rgba(11,11,11,.35)">
<div style="flex:none;width:52px;height:52px;border:2.5px solid var(--ink);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px">{i}</div>
<div><div style="font-size:38px;font-weight:600;color:var(--ink);line-height:1.2">{a}</div><div style="font-size:28px;color:#2a2416;margin-top:6px">{b}</div></div></div>""" for i, (a, b) in enumerate(checks, 1))
POSTS[W5 / "p3_gold_call_test.jpg"] = page(f"""<div class=kicker style="margin-top:0">quick win &middot; 2 minutes</div>
<div class=h style="font-size:118px;margin-top:30px">pull up your site<br>on your phone.<br><em>try to call yourself.</em></div>
<div style="margin-top:60px">{cl}<div style="border-top:1.5px solid rgba(11,11,11,.35)"></div></div>
<div class=body style="margin-top:48px;font-size:34px;max-width:860px">a no on any of these? <b>that's a quick fix.</b></div>""", "goldbg", "check this today")

# ---------- Fri Nov 6: cream quote card, From Tyler ----------
POSTS[W5 / "p4_quote_tyler_cream.jpg"] = page("""<div class=h style="font-size:330px;line-height:.7;color:var(--gold);margin-top:140px;height:150px">&ldquo;</div>
<div class=h style="font-size:100px;margin-top:10px;line-height:1.02">slow season is when<br>you fix the marketing.<br><em>so it's ready when<br>the phone picks<br>back up.</em></div>
<div class=rule style="margin-top:56px"></div>
<div style="font-weight:600;font-size:32px;color:var(--ink)">Tyler Maas</div>
<div style="font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:#7d776a;margin-top:10px;font-weight:600">co-founder, groundwerx digital</div>""",
"cream", "from tyler")

# ---------- Fri Nov 6 (revised Oct 28 per Tyler): same quote card, from Cade ----------
POSTS[W5 / "p4_quote_cade_cream.jpg"] = page("""<div class=h style="font-size:330px;line-height:.7;color:var(--gold);margin-top:140px;height:150px">&ldquo;</div>
<div class=h style="font-size:100px;margin-top:10px;line-height:1.02">slow season is when<br>you fix the marketing.<br><em>so it's ready when<br>the phone picks<br>back up.</em></div>
<div class=rule style="margin-top:56px"></div>
<div style="font-weight:600;font-size:32px;color:var(--ink)">Cade Maas</div>
<div style="font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:#7d776a;margin-top:10px;font-weight:600">co-founder, groundwerx digital</div>""",
"cream", "from cade")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        only = sys.argv[1:]
        for out, html in POSTS.items():
            if only and out.name not in only: continue
            f = TMP / (out.stem + ".html"); f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
            png = TMP / (out.stem + ".png"); await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(out, quality=86); print("wrote", out.relative_to(ROOT))
        await b.close()
    for f in TMP.iterdir(): f.unlink()
    TMP.rmdir()
asyncio.run(main())
