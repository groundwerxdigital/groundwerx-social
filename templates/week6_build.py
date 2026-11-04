"""Render GroundWerx posts for the week of Nov 9-13, 2026 (all library looks).
Usage: python3 templates/week6_build.py [file.jpg ...]
Outputs 1080x1350 JPGs to images/2026-11-w2/.
"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "templates"))
_argv = sys.argv; sys.argv = [_argv[0], "__import_only__"]   # looks_library renders on import; render nothing
import looks_library as L
sys.argv = _argv
page, tape, LOGO_INK, zig = L.page, L.tape, L.LOGO_INK, L.zig

OUT = ROOT / "images/2026-11-w2"; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / "templates/_tmp_w6"; TMP.mkdir(exist_ok=True)
POSTS = {}

# ---------- Mon Nov 9 · Money you're losing · look 3 RECEIPT: a year of not asking for reviews (example) ----------
lines = [("jobs finished", "140"), ("asked for a review", "12"), ("reviews left", "9")]
lr = "".join(f'<div style="display:flex;justify-content:space-between;padding:9px 0"><span>{a}</span><span>{b}</span></div>' for a, b in lines)
POSTS["p1_receipt_reviews.jpg"] = page(f"""
<div style="position:absolute;left:80px;top:96px;width:380px">
<div style="font:600 19px In;letter-spacing:.24em;color:var(--gold);text-transform:uppercase">money you're losing</div>
<div style="font:700 86px/0.98 CG;color:var(--paper);margin-top:26px">the receipt for a year of not asking.</div>
<div style="font:400 26px/1.5 In;color:#a8a293;margin-top:30px">great work doesn't turn into reviews on its own.</div></div>
<div class=mo style="position:absolute;right:76px;top:70px;width:530px;background:#FBF9F3;color:#1a1814;padding:50px 40px 70px;
font-size:24px;transform:rotate(2.2deg);clip-path:{zig};box-shadow:0 0 0 1px #000">
<div style="text-align:center;font-weight:700;font-size:30px;letter-spacing:.08em">YOUR BUSINESS</div>
<div style="text-align:center;font-size:20px;color:#6b6352;margin-top:6px">EXAMPLE YEAR &middot; REVIEWS</div>
<div style="border-top:2px dashed #1a1814;margin:26px 0 14px"></div>{lr}
<div style="border-top:2px dashed #1a1814;margin:16px 0 18px"></div>
<div style="display:flex;justify-content:space-between;font-weight:700;font-size:30px"><span>JOBS NEVER<br>ASKED</span><span style="align-self:flex-end;font-size:46px">128</span></div>
<div style="border-top:2px dashed #1a1814;margin:22px 0 18px"></div>
<div style="text-align:center;font-size:20px;color:#6b6352;line-height:1.6">*example numbers. yours will differ.<br><br>NEXT TIME SOMEONE COMPARES<br>YOU ON GOOGLE, THEY'LL<br>READ THE 9.</div>
<div style="margin:26px auto 0;height:70px;width:360px;background:repeating-linear-gradient(90deg,#1a1814 0 3px,transparent 3px 6px,#1a1814 6px 10px,transparent 10px 12px,#1a1814 12px 13px,transparent 13px 17px)"></div>
</div>
<div style="position:absolute;left:80px;top:800px;width:380px;font:500 27px/1.5 In;color:#CFC9BA">review automation sends a request after <b style="color:var(--gold2)">every</b> finished job. nobody has to remember to ask.</div>""",
"#0B0B0B", "dark")

# ---------- Tue Nov 10 · Quick wins · look 5 BLUEPRINT carousel (6): google profile description in 4 lines ----------
GRID = """<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(186,153,65,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(186,153,65,.09) 1px,transparent 1px),linear-gradient(rgba(186,153,65,.2) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(186,153,65,.2) 1.5px,transparent 1.5px);background-size:30px 30px,30px 30px,150px 150px,150px 150px"></div>"""
def tblock(sheet):
    return f"""<div class=mo style="position:absolute;right:80px;bottom:62px;width:410px;border:2px solid rgba(217,191,114,.7);font-size:17px;color:#CFC9BA">
<div style="display:flex;border-bottom:1.5px solid rgba(217,191,114,.5)"><div style="padding:10px 14px;flex:1;border-right:1.5px solid rgba(217,191,114,.5)">PROJECT<br><b style="color:#E8DDB8">YOUR GOOGLE PROFILE</b></div><div style="padding:10px 14px">SHEET<br><b style="color:#E8DDB8">{sheet} OF 6</b></div></div>
<div style="padding:10px 14px">DRAWN BY <b style="color:#E8DDB8">GROUNDWERX DIGITAL</b></div></div>"""
bx = lambda x, y, w, t, hi=False, h=92: f'<div class=mo style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:2.5px solid {"#D9BF72" if hi else "rgba(217,191,114,.7)"};background:{"rgba(217,191,114,.14)" if hi else "#0d0d0b"};display:flex;align-items:center;justify-content:center;text-align:center;font-size:23px;font-weight:700;color:#E8DDB8;letter-spacing:.05em;line-height:1.25">{t}</div>'
parts = ["WHAT YOU<br>DO", "WHERE YOU<br>WORK", "WHY<br>YOU", "WHAT TO<br>DO NEXT"]
xs = [80, 312, 544, 776]
def diagram(top, hi=None):
    lns = "".join(f'<line x1="540" y1="{top+140}" x2="{x+112}" y2="{top+140}" stroke="#BA9941" stroke-width="2.5"/><line x1="{x+112}" y1="{top+140}" x2="{x+112}" y2="{top+190}" stroke="#BA9941" stroke-width="2.5"/>' for x in xs)
    svg = f'<svg width=1080 height=1350 style="position:absolute;left:0;top:0"><line x1="540" y1="{top+92}" x2="540" y2="{top+140}" stroke="#BA9941" stroke-width="2.5"/>{lns}</svg>'
    return svg + bx(330, top, 420, "BUSINESS DESCRIPTION", hi is None) + "".join(
        bx(x, top + 190, 224, f'<span><span style="color:var(--gold)">0{i+1}</span><br>{t}</span>', hi == i, 120) for i, (x, t) in enumerate(zip(xs, parts)))

POSTS["p2_blueprint_1.jpg"] = page(GRID + f"""
<div style="position:absolute;left:80px;top:100px">
<div class=mo style="font-size:22px;color:var(--gold);letter-spacing:.2em">SHEET A-1 &middot; GOOGLE PROFILE DESCRIPTION</div>
<div class=os style="font-size:116px;color:var(--paper);margin-top:20px">write your<br>description<br><span style="color:var(--gold2)">in 4 lines.</span></div></div>
{diagram(560)}
<div class=mo style="position:absolute;left:80px;right:80px;top:930px;font-size:25px;line-height:1.75;color:#CFC9BA">
the box on your google profile a lot of<br>contractors leave blank, or fill with a slogan.<br>
<span style="color:var(--gold2)">swipe for the plan &rarr;</span></div>
{tblock(1)}""", "#0d0d0b", "dark")

steps = [
 ("what you do", "lead with the work people search for. plain words, not a slogan.",
  "Example Roofing repairs and replaces roofs, gutters and siding for homeowners."),
 ("where you work", "name the towns you really cover, so people there know you come to them.",
  "We work in Anytown, Lakeview, Millbrook and the towns around them."),
 ("why you", "real facts only: years in business, licensed and insured, how you work.",
  "Family-owned, licensed and insured. We send photos of what we find before any work starts."),
 ("what to do next", "tell them the next step. keep links, prices and sales out of it. google's rules.",
  "Call us for a free inspection, or send a message right here on our profile."),
]
for i, (title, note, ex) in enumerate(steps):
    POSTS[f"p2_blueprint_{i+2}.jpg"] = page(GRID + f"""
<div style="position:absolute;left:80px;top:100px;right:80px">
<div class=mo style="font-size:22px;color:var(--gold);letter-spacing:.2em">SHEET A-{i+2} &middot; LINE 0{i+1}</div>
<div class=os style="font-size:100px;color:var(--paper);margin-top:20px;white-space:nowrap"><span style="color:var(--gold2)">0{i+1}</span> {title}</div></div>
{diagram(300, i)}
<div style="position:absolute;left:80px;right:80px;top:720px">
<div class=mo style="font-size:20px;color:var(--gold);letter-spacing:.2em">EXAMPLE BUSINESS &middot; WHAT IT COULD SAY</div>
<div class=mo style="margin-top:16px;border:2.5px dashed rgba(217,191,114,.75);background:rgba(217,191,114,.07);padding:28px 30px;font-size:29px;line-height:1.5;color:#F2EEE4">&ldquo;{ex}&rdquo;</div>
<div class=mo style="margin-top:30px;font-size:25px;line-height:1.6;color:#CFC9BA"><span style="color:#8d8676">// </span>{note}</div></div>
{tblock(i+2)}""", "#0d0d0b", "dark")

POSTS["p2_blueprint_6.jpg"] = page(GRID + f"""
<div style="position:absolute;left:80px;top:100px;right:80px">
<div class=mo style="font-size:22px;color:var(--gold);letter-spacing:.2em">SHEET A-6 &middot; NOTES</div>
<div class=os style="font-size:116px;color:var(--paper);margin-top:20px">4 lines.<br><span style="color:var(--gold2)">one box.</span></div></div>
<div class=mo style="position:absolute;left:80px;right:80px;top:440px;font-size:28px;line-height:1.7;color:#CFC9BA">
<span style="color:var(--gold2)">01</span>&nbsp; up to 750 characters<br>
<span style="color:var(--gold2)">02</span>&nbsp; the top part shows first, so lead with line 01<br>
<span style="color:var(--gold2)">03</span>&nbsp; no links, no prices, no sales<br>
<span style="color:var(--gold2)">04</span>&nbsp; update it when your services change</div>
<div style="position:absolute;left:80px;right:80px;top:810px;border:2.5px solid #D9BF72;background:rgba(217,191,114,.14);padding:34px 36px">
<div class=mo style="font-size:20px;color:var(--gold);letter-spacing:.2em">NO TIME TO WRITE IT?</div>
<div style="font:700 60px/1.05 CG;color:var(--paper);margin-top:14px">that's where we come in.</div>
<div style="font:400 25px/1.5 In;color:#CFC9BA;margin-top:14px">we build out your google profile and keep it current, every week.</div></div>
{tblock(6)}""", "#0d0d0b", "dark")

# ---------- Wed Nov 11 · Offers · look 9 TEAR-OFF FLYER: referral program ----------
tabs = "".join(f"""<div style="flex:1 1 0;min-width:0;border-left:2px dashed #b9b09a;{'background:#14120f;border-color:transparent;color:transparent;' if i == 2 else ''}display:flex;align-items:center;justify-content:center">
<div style="transform:rotate(-90deg);white-space:nowrap;font:700 19px Mo;text-align:center;line-height:1.35">groundwerxdigital<br>.com/referral</div></div>""" for i in range(7))
POSTS["p3_flyer_referral.jpg"] = page(f"""
<div style="position:absolute;inset:0;background:radial-gradient(#2a2620 1.2px,transparent 1.5px) 0 0/14px 14px,linear-gradient(#1b1915,#11100d)"></div>
<div style="position:absolute;left:110px;right:110px;top:80px;height:1120px;background:#F7F3E8;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.6);display:flex;flex-direction:column">
<div style="position:absolute;left:50%;top:-14px;width:46px;height:46px;margin-left:-23px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#f2dc96,#BA9941 55%,#6d5620);box-shadow:0 8px 12px rgba(0,0,0,.5)"></div>
<div style="padding:80px 64px 0;flex:1">
<div class=os style="font-size:132px;color:#0B0B0B">know a<br>contractor?</div>
<div style="background:#0B0B0B;color:#D9BF72;display:inline-block;font:700 40px Os;letter-spacing:.06em;padding:12px 24px;margin-top:30px;text-transform:uppercase">$100 cash per referral</div>
<div style="font:400 30px/1.5 In;color:#2b2820;margin-top:30px">send a business our way. <b>you get $100 cash. they get their first month free.</b> already a client? take a free month instead. no limit.</div>
<img src="{LOGO_INK}" style="height:54px;margin-top:36px"></div>
<div style="height:290px;border-top:2px dashed #b9b09a;display:flex;margin:0 0 0 -2px;color:#1a1814">{tabs}</div></div>
<div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font:600 20px In;letter-spacing:.3em;color:#9A9483">TAKE ONE. PASS IT ON.</div>""",
"#11100d", "none")

# ---------- Thu Nov 12 · Quick wins · look 1 CAUTION TAPE: does your website look old? ----------
POSTS["p4_caution_website.jpg"] = page(tape(95, -7, "CAUTION") + tape(165, 6, "CAUTION") + """
<div style="position:absolute;left:80px;right:80px;top:350px">
<div style="font:600 24px In;letter-spacing:.3em;color:var(--gold);text-transform:uppercase">quick check &middot; your website</div>
<div class=os style="font-size:132px;color:var(--paper);margin-top:24px">does your<br>website<br><span style="color:var(--gold2)">look old?</span></div>
<div style="margin-top:46px;display:flex;gap:16px;flex-wrap:wrap">
""" + "".join(f'<div style="border:2px solid rgba(217,191,114,.55);color:#CFC9BA;font:500 27px In;padding:14px 22px">{x}</div>' for x in
["&copy; 2019 in the footer", "a &ldquo;summer special&rdquo; from 2 summers ago", "photos of a truck you sold"]) + """</div>
<div style="font:400 28px/1.5 In;color:#a8a293;margin-top:36px;max-width:860px">customers notice. an old-looking site makes people wonder if you're still around. <b style="color:var(--gold2)">spot one? that's where we come in.</b></div>
</div>""",
"radial-gradient(ellipse at 50% 45%,#1d1a12,#0B0B0B 70%)", "dark")

# ---------- Fri Nov 13 · Behind GroundWerx · look 6 SPLIT POSTER: no account managers, just two brothers ----------
POSTS["p5_split_brothers.jpg"] = page("""
<div style="position:absolute;left:0;right:0;top:0;height:675px;background:#D9BF72"></div>
<div style="position:absolute;left:80px;top:170px"><div class=os style="font-size:176px;color:#0B0B0B;line-height:.88">no account<br>managers.</div></div>
<div style="position:absolute;left:80px;top:765px"><div class=os style="font-size:176px;color:#D9BF72;line-height:.88">just two<br>brothers.</div>
<div style="font:500 27px In;color:#CFC9BA;margin-top:44px;letter-spacing:.04em">tyler and cade &middot; every account, start to finish</div></div>
<div style="position:absolute;right:80px;top:84px;font:600 22px In;letter-spacing:.3em;color:#0B0B0B">WHO YOU WORK WITH</div>""",
"#0B0B0B", "dark")

async def main():
    only = sys.argv[1:]
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, html in POSTS.items():
            if only and name not in only: continue
            f = TMP / (name[:-4] + ".html"); f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            png = TMP / (name[:-4] + ".png"); await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(OUT / name, quality=86); print("wrote", name)
        await b.close()
asyncio.run(main())
