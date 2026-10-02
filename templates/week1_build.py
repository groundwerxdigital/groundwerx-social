"""Render GroundWerx post graphics (1080x1350) from HTML templates."""
import asyncio, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
F = (ROOT / "node_modules/@fontsource").as_uri()
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
LOGO = (ROOT / "logo_crop.png").as_uri()

CSS = f"""
@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2)}}
@font-face{{font-family:CG;font-weight:700;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2)}}
@font-face{{font-family:CG;font-weight:700;font-style:italic;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-700-italic.woff2)}}
@font-face{{font-family:SC;font-weight:700;src:url({F}/cormorant-sc/files/cormorant-sc-latin-700-normal.woff2)}}
@font-face{{font-family:In;font-weight:400;src:url({F}/inter/files/inter-latin-400-normal.woff2)}}
@font-face{{font-family:In;font-weight:500;src:url({F}/inter/files/inter-latin-500-normal.woff2)}}
@font-face{{font-family:In;font-weight:600;src:url({F}/inter/files/inter-latin-600-normal.woff2)}}
@font-face{{font-family:In;font-weight:700;src:url({F}/inter/files/inter-latin-700-normal.woff2)}}
:root{{--gold:#BA9941;--gold2:#D9BF72;--ink:#0B0B0B;--paper:#F2EEE4;--mute:#9A9483;--line:rgba(186,153,65,.35)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;background:var(--ink);overflow:hidden}}
.page{{position:relative;width:1080px;height:1350px;padding:110px 96px 0;color:var(--paper);font-family:In;
  background:radial-gradient(ellipse 900px 700px at 85% -10%,rgba(186,153,65,.13),transparent 60%),var(--ink)}}
.page::before{{content:"";position:absolute;inset:36px;border:1.5px solid var(--line);pointer-events:none}}
.kicker{{font-family:In;font-weight:600;font-size:22px;letter-spacing:.32em;text-transform:uppercase;color:var(--gold)}}
.h{{font-family:CG;font-weight:700;color:var(--paper);line-height:.98;letter-spacing:-.01em;font-variant-numeric:lining-nums}}
.h em{{font-style:italic;color:var(--gold2)}}
.body{{font-size:34px;line-height:1.45;color:#CFC9BA}}
.body b{{color:var(--paper);font-weight:600}}
.rule{{width:120px;height:3px;background:var(--gold);margin:44px 0}}
.foot{{position:absolute;left:96px;right:96px;bottom:84px;display:flex;align-items:center;justify-content:space-between}}
.foot img{{height:58px;mix-blend-mode:lighten}}
.foot .r{{font-size:22px;letter-spacing:.24em;color:var(--mute);text-transform:uppercase;font-weight:500}}
.swipe{{color:var(--gold)}}
"""

def page(inner, right=""):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head>
<body><div class=page>{inner}<div class=foot><img src="{LOGO}"><div class=r>{right}</div></div></div></body></html>"""

POSTS = {}

# ---------- POST 1: carousel "the math on a missed call" ----------
N = 6
def c(i, inner, right=None):
    POSTS[f"p1_carousel_{i}"] = page(inner, right if right is not None else f"{i} / {N}")

c(1, """<div class=kicker style="margin-top:120px">for contractors</div>
<div class=h style="font-size:168px;margin-top:40px">the math<br>on a <em>missed</em><br><em>call.</em></div>
<div class=rule></div>
<div class=body style="max-width:760px">it costs more than you think. here's how to run your own numbers.</div>""",
  "<span class=swipe>swipe &rarr;</span>")

c(2, """<div class=kicker style="margin-top:150px">picture this</div>
<div class=h style="font-size:118px;margin-top:44px">you're up on a roof.<br>the phone rings.<br><em>you can't pick up.</em></div>
<div class=rule></div>
<div class=body style="max-width:780px">happens every day. it's not a mistake. you're doing the actual work.</div>""")

c(3, """<div class=kicker style="margin-top:150px">here's the problem</div>
<div class=h style="font-size:112px;margin-top:44px">most people don't leave a voicemail.</div>
<div class=h style="font-size:112px;margin-top:30px"><em>they call the next name on google.</em></div>
<div class=rule></div>
<div class=body style="max-width:780px">by the time you call back, they've booked someone else.</div>""")

rows = [("3", "missed calls a week"), ("&times; 1 in 3", "would have booked"), ("&times; $1,000", "average job")]
math = "".join(f"""<div style="display:flex;align-items:baseline;gap:34px;padding:26px 0;border-bottom:1.5px solid var(--line)">
<div class=h style="font-size:92px;color:var(--gold2);min-width:430px">{a}</div><div class=body style="font-size:32px">{b}</div></div>""" for a, b in rows)
c(4, f"""<div class=kicker style="margin-top:40px">run your numbers</div>
<div style="margin-top:34px">{math}</div>
<div style="margin-top:44px"><div class=h style="font-size:150px">= <em>$52,000</em></div>
<div class=body style="margin-top:14px">a year, walking to your competitors.</div>
<div style="font-size:24px;color:var(--mute);margin-top:30px">example numbers. plug in your own: calls missed, close rate, ticket size.</div></div>""")

c(5, """<div class=kicker style="margin-top:120px">the fix</div>
<div class=h style="font-size:130px;margin-top:40px">missed-call<br><em>text-back.</em></div>
<div class=rule></div>
<div class=body style="max-width:820px">can't pick up? the caller gets a text from your business <b>inside a minute</b>.</div>
<div class=body style="max-width:820px;margin-top:28px">they know you saw it. the conversation stays with <b>you</b>, not the next contractor.</div>""")

c(6, """<div class=kicker style="margin-top:120px">want it set up?</div>
<div class=h style="font-size:120px;margin-top:40px">15 minutes<br>with the <em>brothers</em><br>who'd run it.</div>
<div class=rule></div>
<div class=body>no dashboards. no homework. month-to-month.</div>
<div style="margin-top:56px;display:inline-block;border:2px solid var(--gold);padding:28px 40px">
<div style="font-family:In;font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>""", "6 / 6")

# ---------- POST 2: single graphic, search results mock ----------
def listing(name, stars, reviews, note, strong):
    s = "&#9733;" * stars + '<span style="color:#3a3a3a">' + "&#9733;" * (5 - stars) + "</span>" if stars else '<span style="color:#666">no reviews</span>'
    bd = "2px solid var(--gold)" if strong else "1.5px solid #2a2a2a"
    op = "1" if strong else ".55"
    return f"""<div style="border:{bd};background:#121212;padding:28px 32px;margin-bottom:22px;opacity:{op}">
<div style="display:flex;justify-content:space-between;align-items:center">
<div style="font-weight:600;font-size:32px;color:var(--paper)">{name}</div>
<div style="font-size:20px;letter-spacing:.2em;color:{'var(--gold)' if strong else '#777'};font-weight:600">{note}</div></div>
<div style="font-size:28px;color:var(--gold2);margin-top:10px">{s} <span style="color:#9A9483;font-size:24px">{reviews}</span></div></div>"""
POSTS["p2_single_search"] = page(f"""<div class=kicker style="margin-top:10px">right now, in your town</div>
<div class=h style="font-size:104px;margin-top:30px">someone's searching<br><em>"roofer near me."</em></div>
<div style="margin-top:50px;border:1.5px solid #2a2a2a;padding:18px 28px;font-size:28px;color:#bdb7a8;display:flex;gap:18px;align-items:center;background:#111">
<span style="color:var(--gold)">&#9906;</span> roofer near me</div>
<div style="margin-top:26px">
{listing("Summit Roofing Co.", 5, "(214)", "CALLED", True)}
{listing("Ridge Line Exteriors", 4, "(88)", "", False)}
{listing("Your Business", 0, "", "SKIPPED", False)}
</div>
<div class=body style="margin-top:26px;font-size:32px">same work. same town. <b>the profile decides who gets the call.</b></div>""")

# ---------- POST 3: tip card ----------
tips = [("hours are right", "holiday hours too. wrong hours = a lost call."),
        ("real job photos", "your trucks, your crew, your work. skip the stock photos."),
        ("every service listed", "if it's not listed, google won't show you for it."),
        ("service area set", "the towns you actually drive to."),
        ("every review answered", "good and bad. people read the replies.")]
tl = "".join(f"""<div style="display:flex;gap:34px;padding:25px 0;border-bottom:1.5px solid var(--line)">
<div class=h style="font-size:68px;color:var(--gold);width:60px;line-height:1">{i}</div>
<div><div style="font-weight:600;font-size:36px;color:var(--paper)">{a}</div>
<div class=body style="font-size:27px;margin-top:6px">{b}</div></div></div>""" for i, (a, b) in enumerate(tips, 1))
POSTS["p3_tipcard_gbp"] = page(f"""<div class=kicker style="margin-top:0">5-minute check</div>
<div class=h style="font-size:96px;margin-top:26px">is your google profile<br><em>costing you calls?</em></div>
<div style="margin-top:34px">{tl}</div>""", "save this")

# ---------- POST 4: behind GroundWerx ----------
POSTS["p4_single_brothers"] = page("""<div class=kicker style="margin-top:110px">who you'd be working with</div>
<div class=h style="font-size:150px;margin-top:40px">two brothers.<br><em>no account<br>managers.</em></div>
<div class=rule></div>
<div class=body style="font-size:36px">when you call, you get <b>us</b>. start to finish.</div>
<div style="margin-top:60px;display:flex;flex-direction:column;gap:18px;font-size:30px;color:#CFC9BA">
<div><span style="color:var(--gold)">&mdash;</span>&nbsp; no dashboards to log into</div>
<div><span style="color:var(--gold)">&mdash;</span>&nbsp; no weekly homework</div>
<div><span style="color:var(--gold)">&mdash;</span>&nbsp; no handoffs to someone who's never met a contractor</div></div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, html in POSTS.items():
            f = ROOT / f"html_{name}.html"; f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(200)
            await pg.screenshot(path=str(OUT / f"{name}.png"))
            print("ok", name)
        await b.close()
asyncio.run(main())
