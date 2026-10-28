"""GroundWerx LOOKS LIBRARY: approved post styles (Oct 28, 2026). Reference renders live in looks/examples/.
Reuse these helpers/patterns in each week's build script: page(), tape(), iphone() (flat), iphone3d() (real depth),
statusbar(), ios_note(), bubble(), and the laptop scene. Usage: python3 templates/looks_library.py [name ...]
"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT
F = (ROOT / "brand/fonts").as_uri()
OUT = ROOT / "looks/examples"; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / "templates/_tmp_looks"; TMP.mkdir(exist_ok=True)
LOGO = (ROOT / "brand/logo-wordmark.png").as_uri()
src = Image.open(ROOT / "brand/logo-wordmark.png").convert("L")
ink = Image.new("RGBA", src.size, (11, 11, 11, 255)); ink.putalpha(src.point(lambda v: min(255, int(v * 1.6))))
ink.save(TMP / "logo_ink.png"); LOGO_INK = (TMP / "logo_ink.png").as_uri()

def ff(fam, file, w):
    return f"@font-face{{font-family:{fam};font-weight:{w};src:url({F}/{file})}}"
CSS = "\n".join([
    ff("CG", "cormorant-garamond-latin-700-normal.woff2", 700),
    "@font-face{font-family:CG;font-weight:700;font-style:italic;src:url(%s/cormorant-garamond-latin-700-italic.woff2)}" % F,
    ff("In", "inter-latin-400-normal.woff2", 400), ff("In", "inter-latin-500-normal.woff2", 500),
    ff("In", "inter-latin-600-normal.woff2", 600), ff("In", "inter-latin-700-normal.woff2", 700),
    ff("Os", "oswald-latin-500-normal.woff2", 500), ff("Os", "oswald-latin-600-normal.woff2", 600),
    ff("Os", "oswald-latin-700-normal.woff2", 700),
    ff("Mo", "jetbrains-mono-latin-400-normal.woff2", 400), ff("Mo", "jetbrains-mono-latin-500-normal.woff2", 500),
    ff("Mo", "jetbrains-mono-latin-700-normal.woff2", 700),
    ff("Hw", "caveat-latin-700-normal.woff2", 700),
]) + """
:root{--gold:#BA9941;--gold2:#D9BF72;--ink:#0B0B0B;--paper:#F2EEE4}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
.pg{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:In}
.os{font-family:Os;text-transform:uppercase;line-height:.92;letter-spacing:.005em}
.mo{font-family:Mo}
.logo{position:absolute;left:80px;bottom:70px;height:56px}
.logo.l{mix-blend-mode:lighten}
.tag{position:absolute;right:80px;bottom:88px;font:600 20px In;letter-spacing:.24em;text-transform:uppercase}
"""

def page(inner, bg, logo="dark", tag="", tagc="#9A9483"):
    lg = f'<img class="logo l" src="{LOGO}">' if logo == "dark" else (f'<img class=logo src="{LOGO_INK}">' if logo == "ink" else "")
    t = f'<div class=tag style="color:{tagc}">{tag}</div>' if tag else ""
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head>
<body><div class=pg style="background:{bg}">{inner}{lg}{t}</div></body></html>"""

P = {}

# 1. CAUTION TAPE — "does your Google profile look closed?"
tape = lambda top, rot, txt: f"""<div style="position:absolute;left:-120px;right:-120px;top:{top}px;height:96px;transform:rotate({rot}deg);
background:repeating-linear-gradient(-45deg,#D9BF72 0 46px,#0B0B0B 46px 92px);box-shadow:0 10px 30px rgba(0,0,0,.5)">
<div style="position:absolute;inset:16px 0;background:#D9BF72;display:flex;align-items:center;justify-content:center;gap:40px;
font:700 40px Os;letter-spacing:.18em;color:#0B0B0B;white-space:nowrap">{(txt + ' &#9888; ') * 6}</div></div>"""
P["01_caution_tape"] = page(tape(95, -7, "CAUTION") + tape(165, 6, "CAUTION") + """
<div style="position:absolute;left:80px;right:80px;top:350px">
<div style="font:600 24px In;letter-spacing:.3em;color:var(--gold);text-transform:uppercase">quick check</div>
<div class=os style="font-size:132px;color:var(--paper);margin-top:24px">does your<br>google profile<br><span style="color:var(--gold2)">look closed?</span></div>
<div style="margin-top:46px;display:flex;gap:16px;flex-wrap:wrap">
""" + "".join(f'<div style="border:2px solid rgba(217,191,114,.55);color:#CFC9BA;font:500 27px In;padding:14px 22px">{x}</div>' for x in
["last post: 8 months ago", "newest photo: 2023", "3 reviews, no replies"]) + """</div>
</div>""",
"radial-gradient(ellipse at 50% 45%,#1d1a12,#0B0B0B 70%)", "dark")

# 2. WORK ORDER — 5-minute Google profile check
checks = [("hours are right (holidays too)", 1), ("phone matches your website", 1), ("photos from this year", 1),
          ("replied to your last 5 reviews", 1), ("every service listed", 0)]
rows = "".join(f"""<div style="display:flex;align-items:center;gap:22px;padding:17px 0;border-bottom:1.5px solid #cfc6b0">
<div style="width:40px;height:40px;border:2.5px solid #0B0B0B;position:relative;flex:none">{'<div style="position:absolute;left:-4px;top:-26px;font:700 64px Hw;color:#a5812c">&#10003;</div>' if c else ''}</div>
<div class=mo style="font-size:29px;color:#1a1814">{t}</div></div>""" for t, c in checks)
P["02_work_order"] = page(f"""
<div style="position:absolute;left:96px;right:96px;top:84px;transform:rotate(-1.8deg);background:#F7F3E8;padding:54px 56px 48px;
box-shadow:0 30px 60px rgba(0,0,0,.35),0 2px 0 #ddd3bb">
<div style="position:absolute;left:50%;top:-34px;width:230px;height:70px;margin-left:-115px;background:linear-gradient(#3a3a3a,#111);border-radius:14px"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:4px solid #0B0B0B;padding-bottom:18px">
<div class=os style="font-size:78px;color:#0B0B0B">work order</div><div class=mo style="font-size:26px;color:#6b6352">No. 0005</div></div>
<div class=mo style="display:grid;grid-template-columns:auto 1fr;gap:12px 26px;margin-top:28px;font-size:25px;color:#6b6352">
<div>CUSTOMER</div><div style="color:#0B0B0B;font-weight:700">YOUR BUSINESS</div>
<div>JOB</div><div style="color:#0B0B0B;font-weight:700">GOOGLE PROFILE CHECK</div>
<div>EST. TIME</div><div style="color:#0B0B0B;font-weight:700">5 MIN &middot; FROM YOUR PHONE</div></div>
<div style="margin-top:26px">{rows}</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:34px">
<div class=mo style="font-size:22px;color:#6b6352;line-height:1.5">missing a box?<br><b style="color:#0B0B0B">that&rsquo;s where we come in.</b></div>
<div style="text-align:right"><div style="font:700 56px Hw;color:#a5812c;transform:rotate(-4deg)">GroundWerx</div>
<div class=mo style="font-size:18px;color:#6b6352;border-top:1.5px solid #0B0B0B;padding-top:6px;width:260px;margin-left:auto">CHECKED BY</div></div></div>
</div>""", "linear-gradient(160deg,#D9BF72,#BA9941 75%)", "ink", "quick win", "#2a2416")

# 3. RECEIPT — the math on a missed call (example)
zig = "polygon(" + ",".join([f"{i*5}% {100 if i%2==0 else 97.6}%" for i in range(21)]) + ",100% 0,0 0)"
lines = [("missed calls / week", "6"), ("would've booked (1 in 3)", "2"), ("avg job (example)", "$450"), ("per week", "$900"), ("x 4 weeks", "")]
lr = "".join(f'<div style="display:flex;justify-content:space-between;padding:9px 0"><span>{a}</span><span>{b}</span></div>' for a, b in lines)
P["03_receipt"] = page(f"""
<div style="position:absolute;left:80px;top:96px;width:380px">
<div style="font:600 19px In;letter-spacing:.24em;color:var(--gold);text-transform:uppercase">money you're losing</div>
<div style="font:700 86px/0.98 CG;color:var(--paper);margin-top:26px">the receipt nobody hands you.</div>
<div style="font:400 26px/1.5 In;color:#a8a293;margin-top:30px">what a missed call adds up to in a month.</div></div>
<div class=mo style="position:absolute;right:76px;top:70px;width:530px;background:#FBF9F3;color:#1a1814;padding:50px 40px 70px;
font-size:24px;transform:rotate(2.2deg);clip-path:{zig};box-shadow:0 0 0 1px #000">
<div style="text-align:center;font-weight:700;font-size:30px;letter-spacing:.08em">YOUR BUSINESS</div>
<div style="text-align:center;font-size:20px;color:#6b6352;margin-top:6px">EXAMPLE MONTH &middot; MISSED CALLS</div>
<div style="border-top:2px dashed #1a1814;margin:26px 0 14px"></div>{lr}
<div style="border-top:2px dashed #1a1814;margin:16px 0 18px"></div>
<div style="display:flex;justify-content:space-between;font-weight:700;font-size:30px"><span>LEFT ON<br>THE TABLE</span><span style="align-self:flex-end;font-size:46px">$3,600</span></div>
<div style="border-top:2px dashed #1a1814;margin:22px 0 18px"></div>
<div style="text-align:center;font-size:20px;color:#6b6352;line-height:1.6">*example numbers. yours will differ.<br><br>CALL AGAIN SOON?<br>they won't. they called<br>the next guy.</div>
<div style="margin:26px auto 0;height:70px;width:360px;background:repeating-linear-gradient(90deg,#1a1814 0 3px,transparent 3px 6px,#1a1814 6px 10px,transparent 10px 12px,#1a1814 12px 13px,transparent 13px 17px)"></div>
</div>""", "#0B0B0B", "dark")

# 4. (retired) brand-colored lock screen: replaced by 10_iphone_lockscreen (real iPhone look)

# 5. BLUEPRINT — a page for every service
bx = lambda x, y, w, t, hi=False: f'<div class=mo style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:92px;border:2.5px solid {"#D9BF72" if hi else "rgba(217,191,114,.7)"};background:{"rgba(217,191,114,.14)" if hi else "#0d0d0b"};display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;color:#E8DDB8;letter-spacing:.05em">{t}</div>'
svc = ["ROOF REPAIR", "GUTTERS", "SIDING", "STORM DAMAGE"]
xs = [80, 312, 544, 776]
lns = "".join(f'<line x1="540" y1="560" x2="{x+112}" y2="560" stroke="#BA9941" stroke-width="2.5"/><line x1="{x+112}" y1="560" x2="{x+112}" y2="610" stroke="#BA9941" stroke-width="2.5"/>' for x in xs)
P["05_blueprint"] = page(f"""
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(186,153,65,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(186,153,65,.09) 1px,transparent 1px),linear-gradient(rgba(186,153,65,.2) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(186,153,65,.2) 1.5px,transparent 1.5px);background-size:30px 30px,30px 30px,150px 150px,150px 150px"></div>
<div style="position:absolute;left:80px;top:100px">
<div class=mo style="font-size:22px;color:var(--gold);letter-spacing:.2em">SHEET A-1 &middot; WEBSITE LAYOUT</div>
<div class=os style="font-size:120px;color:var(--paper);margin-top:20px">a page for<br><span style="color:var(--gold2)">every service.</span></div></div>
<svg width=1080 height=1350 style="position:absolute;left:0;top:0"><line x1="540" y1="512" x2="540" y2="560" stroke="#BA9941" stroke-width="2.5"/>{lns}
<line x1="80" y1="745" x2="1000" y2="745" stroke="#BA9941" stroke-width="1.5" stroke-dasharray="6 6"/></svg>
{bx(390, 420, 300, "HOME", True)}{"".join(bx(x, 610, 224, t) for x, t in zip(xs, svc))}
<div class=mo style="position:absolute;left:80px;right:80px;top:790px;font-size:25px;line-height:1.75;color:#CFC9BA">
<span style="color:var(--gold2)">01</span>&nbsp; what you do and the towns you cover<br>
<span style="color:var(--gold2)">02</span>&nbsp; photos of those exact jobs<br>
<span style="color:var(--gold2)">03</span>&nbsp; a call button right at the top<br>
<span style="color:#8d8676">// one "services" page with everything crammed in? harder to find.</span></div>
<div class=mo style="position:absolute;right:80px;bottom:62px;width:410px;border:2px solid rgba(217,191,114,.7);font-size:17px;color:#CFC9BA">
<div style="display:flex;border-bottom:1.5px solid rgba(217,191,114,.5)"><div style="padding:10px 14px;flex:1;border-right:1.5px solid rgba(217,191,114,.5)">PROJECT<br><b style="color:#E8DDB8">YOUR WEBSITE</b></div><div style="padding:10px 14px">SCALE<br><b style="color:#E8DDB8">1 PAGE : 1 JOB</b></div></div>
<div style="padding:10px 14px">DRAWN BY <b style="color:#E8DDB8">GROUNDWERX DIGITAL</b></div></div>""", "#0d0d0b", "dark")

# 6. SPLIT POSTER — you run the jobs, we run the rest
P["06_split_poster"] = page("""
<div style="position:absolute;left:0;right:0;top:0;height:675px;background:#D9BF72"></div>
<div style="position:absolute;left:80px;top:150px"><div class=os style="font-size:200px;color:#0B0B0B;line-height:.86">you run<br>the jobs.</div></div>
<div style="position:absolute;left:80px;top:745px"><div class=os style="font-size:200px;color:#D9BF72;line-height:.86">we run<br>the rest.</div>
<div style="font:500 27px In;color:#CFC9BA;margin-top:44px;letter-spacing:.04em">google profile &middot; reviews &middot; missed calls &middot; website</div></div>
<div style="position:absolute;right:80px;top:84px;font:600 22px In;letter-spacing:.3em;color:#0B0B0B">DONE FOR YOU</div>""",
"#0B0B0B", "dark")

# 7. BIG TEXT BUBBLES — text-back mid-job
def bub(t, me, top, meta=""):
    side = "right:70px;" if me else "left:70px;"
    bg = "background:#D9BF72;color:#0B0B0B;border-bottom-right-radius:12px" if me else "background:#2a2823;color:#F2EEE4;border-bottom-left-radius:12px"
    m = f'<div style="font:500 20px In;color:#8d8676;margin-top:12px;{"text-align:right" if me else ""}">{meta}</div>' if meta else ""
    return f'<div style="position:absolute;{side}top:{top}px;max-width:760px"><div style="{bg};border-radius:44px;padding:30px 38px;font:500 36px/1.32 In">{t}</div>{m}</div>'
P["07_text_bubbles"] = page(f"""
<div style="position:absolute;left:70px;top:90px;font:600 22px In;letter-spacing:.3em;color:var(--gold)">ON A ROOF WHEN IT RINGS</div>
<div style="position:absolute;left:0;right:0;top:150px;text-align:center;font:500 20px In;color:#8d8676">Missed call &middot; 11:42 AM</div>
{bub("Hi, this is Example Roofing! Sorry we missed you, we're on a job. What can we help with?", True, 200, "sent automatically &middot; 4 sec later")}
{bub("Leak over the garage after the storm. Can someone look this week?", False, 520)}
{bub("Got it. Mike here, just got off the roof. Calling you in 5.", True, 760)}
<div style="position:absolute;left:70px;right:70px;top:1010px"><div style="font:700 72px/1 CG;color:var(--paper)">the call got missed.<br><i style="color:var(--gold2)">the job didn't.</i></div></div>""",
"#141310", "dark", "example business")

# 8. GIANT SEARCH BAR — the referral that googled you
sug = ["roofer near me <b>open now</b>", "roofer near me <b>reviews</b>", "roofer near me <b>free estimate</b>"]
P["08_search_bar"] = page(f"""
<div style="position:absolute;left:80px;right:80px;top:120px"><div style="font:700 104px/0.98 CG;color:#0B0B0B">someone just<br>recommended you.</div>
<div style="font:700 italic 72px CG;color:#8a6f28;margin-top:26px">then they typed this:</div></div>
<div style="position:absolute;left:60px;right:60px;top:560px;background:#fff;border-radius:60px;box-shadow:0 24px 60px rgba(11,11,11,.16);overflow:hidden">
<div style="display:flex;align-items:center;gap:26px;padding:34px 44px;font:500 50px In;color:#0B0B0B">
<svg width=48 height=48 viewBox="0 0 24 24"><circle cx=10 cy=10 r=7 fill=none stroke="#8a6f28" stroke-width=2.6 /><line x1=15.2 y1=15.2 x2=21 y2=21 stroke="#8a6f28" stroke-width=2.8 stroke-linecap=round /></svg>
<span>roofer near me<span style="display:inline-block;width:4px;height:52px;background:#BA9941;vertical-align:-8px;margin-left:4px"></span></span></div>
<div style="border-top:1.5px solid #ece6d6">{"".join(f'<div style="padding:22px 44px 22px 118px;font:400 34px In;color:#55503f">{s}</div>' for s in sug)}</div></div>
<div style="position:absolute;left:80px;right:80px;top:1040px;font:500 32px/1.45 In;color:#3b382f">word of mouth still runs through a search bar. <b style="color:#0B0B0B">will they find you, or the next guy?</b></div>""",
"#F2EEE4", "ink", "", "#7d776a")

# 9. TEAR-OFF FLYER — free 15-minute call
tabs = "".join(f"""<div style="flex:1 1 0;min-width:0;border-left:2px dashed #b9b09a;{'background:#14120f;border-color:transparent;color:transparent;' if i == 2 else ''}display:flex;align-items:center;justify-content:center">
<div style="transform:rotate(-90deg);white-space:nowrap;font:700 21px Mo;text-align:center;line-height:1.3">GroundWerx<br>(952) 333-8122</div></div>""" for i in range(7))
P["09_tearoff_flyer"] = page(f"""
<div style="position:absolute;inset:0;background:radial-gradient(#2a2620 1.2px,transparent 1.5px) 0 0/14px 14px,linear-gradient(#1b1915,#11100d)"></div>
<div style="position:absolute;left:110px;right:110px;top:80px;height:1120px;background:#F7F3E8;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.6);display:flex;flex-direction:column">
<div style="position:absolute;left:50%;top:-14px;width:46px;height:46px;margin-left:-23px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#f2dc96,#BA9941 55%,#6d5620);box-shadow:0 8px 12px rgba(0,0,0,.5)"></div>
<div style="padding:80px 64px 0;flex:1">
<div class=os style="font-size:150px;color:#0B0B0B">phone<br>too quiet?</div>
<div style="background:#0B0B0B;color:#D9BF72;display:inline-block;font:700 40px Os;letter-spacing:.06em;padding:12px 24px;margin-top:30px;text-transform:uppercase">free 15-minute call</div>
<div style="font:400 30px/1.5 In;color:#2b2820;margin-top:32px">we'll look at your google profile, reviews and website, and tell you what we'd fix first. <b>keep the list, with us or without us.</b></div>
<img src="{LOGO_INK}" style="height:54px;margin-top:40px"></div>
<div style="height:290px;border-top:2px dashed #b9b09a;display:flex;margin:0 0 0 -2px;color:#1a1814">{tabs}</div></div>""",
"#11100d", "none")

# ================= DEVICE MOCKUPS (iPhone look on screens, brand around them) =================
IOS = "font-family:In;-webkit-font-smoothing:antialiased"

def iphone(screen, w=440, extra_style="", edge="right"):
    """iPhone-shaped frame (titanium rim, black bezel, Dynamic Island). Height from real 19.5:9-ish ratio."""
    h = int(w * 2.08)
    r = int(w * 0.165)
    thick = "".join(f"{(-i if edge == 'left' else i)}px {int(i*0.3)}px 0 {'#8f8a80' if i < 4 else '#6e6a62'}," for i in range(1, 15)).rstrip(",")
    return f"""<div style="position:absolute;width:{w}px;height:{h}px;{extra_style}">
<div style="position:absolute;inset:0;border-radius:{r}px;background:linear-gradient(135deg,#d9d5cc,#9c978d 30%,#c9c4ba 55%,#8a857b);box-shadow:{thick},0 50px 90px rgba(0,0,0,.55)"></div>
<div style="position:absolute;left:{-3 if edge=='right' else w-1}px;top:{int(h*.2)}px;width:4px;height:{int(h*.06)}px;background:#a29d93;border-radius:2px"></div>
<div style="position:absolute;inset:5px;border-radius:{r-5}px;background:#000"></div>
<div style="position:absolute;inset:{int(w*0.035)}px;border-radius:{r-int(w*0.035)+4}px;overflow:hidden;background:#fff">{screen}
<div style="position:absolute;left:50%;top:{int(w*0.028)}px;width:{int(w*0.29)}px;height:{int(w*0.085)}px;margin-left:-{int(w*0.145)}px;background:#000;border-radius:999px;z-index:9"></div></div></div>"""

def statusbar(w, color="#fff", time="9:41", left=True):
    fs = int(w * 0.04)
    return f"""<div style="position:absolute;left:0;right:0;top:0;height:{int(w*.12)}px;display:flex;align-items:center;justify-content:space-between;padding:0 {int(w*.09)}px 0 {int(w*.1)}px;color:{color};{IOS};font-weight:600;font-size:{fs}px;z-index:5">
<span>{time if left else ''}</span><span style="display:flex;gap:{int(w*.012)}px;align-items:center">
<svg width="{int(fs*1.1)}" height="{int(fs*.75)}" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1" fill="{color}"/><rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="{color}"/><rect x="10" y="3" width="3" height="9" rx="1" fill="{color}"/><rect x="15" y="0" width="3" height="12" rx="1" fill="{color}"/></svg>
<svg width="{int(fs*1.05)}" height="{int(fs*.78)}" viewBox="0 0 16 12"><path d="M8 11.5 5.6 9.1a3.4 3.4 0 0 1 4.8 0z M3.5 7a6.4 6.4 0 0 1 9 0l-1.4 1.4a4.4 4.4 0 0 0-6.2 0z M1.2 4.7a9.6 9.6 0 0 1 13.6 0l-1.4 1.4a7.6 7.6 0 0 0-10.8 0z" fill="{color}"/></svg>
<span style="display:inline-block;width:{int(fs*1.6)}px;height:{int(fs*.8)}px;border:1.5px solid {color};opacity:.9;border-radius:{int(fs*.25)}px;padding:1.5px"><span style="display:block;height:100%;width:78%;background:{color};border-radius:2px"></span></span></span></div>"""

PHONE_ICON = """<svg viewBox="0 0 24 24" width="62%" height="62%"><path fill="#fff" d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>"""

# ---- A. iPhone lock screen: 3 missed calls overnight ----
W1 = 470
def ios_note(t, title, body, w):
    s = w / 470
    return f"""<div style="margin:0 {int(14*s)}px {int(9*s)}px;padding:{int(14*s)}px {int(15*s)}px;border-radius:{int(22*s)}px;background:rgba(245,245,245,.72);backdrop-filter:blur(30px);display:flex;gap:{int(11*s)}px;align-items:center;{IOS}">
<div style="width:{int(38*s)}px;height:{int(38*s)}px;border-radius:{int(9*s)}px;background:linear-gradient(#5ff777,#28c840);display:flex;align-items:center;justify-content:center;flex:none">{PHONE_ICON}</div>
<div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;font-size:{int(15.5*s)}px;color:#000"><b style="font-weight:600">{title}</b><span style="color:#5d5d62;font-size:{int(13.5*s)}px">{t}</span></div>
<div style="font-size:{int(15.5*s)}px;color:#000;margin-top:{int(1*s)}px">{body}</div></div></div>"""
lock = f"""<div style="position:absolute;inset:0;background:radial-gradient(circle at 25% 20%,#7aa7d9,transparent 55%),radial-gradient(circle at 85% 75%,#e59a6b,transparent 55%),linear-gradient(170deg,#3d5f8c,#2a2b4f 60%,#5b3a4a)"></div>
{statusbar(W1, '#fff', '', left=False)}
<div style="position:absolute;left:0;right:0;top:{int(W1*.17)}px;text-align:center;color:#fff;{IOS}">
<div style="font-weight:600;font-size:{int(W1*.047)}px;opacity:.92">Wednesday, November 4</div>
<div style="font-weight:700;font-size:{int(W1*.235)}px;line-height:1;letter-spacing:-.03em;margin-top:{int(W1*.005)}px;opacity:.95">6:12</div></div>
<div style="position:absolute;left:0;right:0;top:{int(W1*.72)}px">
{ios_note('10:47 PM', 'Missed Call', '(555) 010-2281', W1)}{ios_note('11:32 PM', 'Missed Call', '(555) 010-7714', W1)}{ios_note('6:05 AM', 'Missed Call', '(555) 010-3390', W1)}</div>
<div style="position:absolute;left:{int(W1*.12)}px;right:{int(W1*.12)}px;bottom:{int(W1*.11)}px;display:flex;justify-content:space-between">
<div style="width:{int(W1*.115)}px;height:{int(W1*.115)}px;border-radius:50%;background:rgba(40,40,50,.45);backdrop-filter:blur(20px);display:flex;align-items:center;justify-content:center"><svg width="40%" viewBox="0 0 24 24"><path fill="#fff" d="M8 2h8v3.5l-2 3.5v11.5a1.5 1.5 0 0 1-1.5 1.5h-1A1.5 1.5 0 0 1 10 20.5V9L8 5.5z"/><circle cx="12" cy="13" r="1.3" fill="#3a3a48"/></svg></div>
<div style="width:{int(W1*.115)}px;height:{int(W1*.115)}px;border-radius:50%;background:rgba(40,40,50,.45);backdrop-filter:blur(20px);display:flex;align-items:center;justify-content:center"><svg width="45%" viewBox="0 0 24 24"><path fill="#fff" d="M4 7h3l2-2h6l2 2h3a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1zm8 3a4 4 0 1 0 0 8 4 4 0 0 0 0-8z"/></svg></div></div>
<div style="position:absolute;left:50%;bottom:{int(W1*.025)}px;width:{int(W1*.3)}px;height:{int(W1*.011)}px;margin-left:-{int(W1*.15)}px;background:#fff;border-radius:9px"></div>"""
P["10_iphone_lockscreen"] = page(f"""
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 700px 600px at 80% 40%,rgba(186,153,65,.22),transparent 65%)"></div>
<div style="position:absolute;left:80px;top:110px;width:420px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">AFTER HOURS</div>
<div class=os style="font-size:94px;color:var(--paper);margin-top:26px">3 people<br>needed you<br><span style="color:var(--gold2)">overnight.</span></div>
<div style="font:400 29px/1.5 In;color:#CFC9BA;margin-top:36px">with missed-call text-back, every one of them gets a text back in seconds, even at 10:47pm.</div></div>
{iphone(lock, W1, "left:560px;top:150px;transform:rotate(4deg)")}""", "#0B0B0B", "dark", "example phone")

# ---- B. 3D iPhone: Messages thread (text-back) ----
W2 = 540
def bubble(t, sent, s, tail=True):
    bg = "#34C759" if sent else "#E9E9EB"; col = "#fff" if sent else "#000"
    al = "flex-end" if sent else "flex-start"
    rad = f"{int(19*s)}px"
    tl = (f"border-bottom-right-radius:{int(6*s)}px" if sent else f"border-bottom-left-radius:{int(6*s)}px") if tail else ""
    return f"""<div style="display:flex;justify-content:{al};margin:{int(3*s)}px {int(14*s)}px"><div style="max-width:74%;background:{bg};color:{col};border-radius:{rad};{tl};padding:{int(8*s)}px {int(13*s)}px;font-size:{int(16.5*s)}px;line-height:1.28;{IOS}">{t}</div></div>"""
s2 = W2 / 390
msgs = f"""<div style="position:absolute;inset:0;background:#fff"></div>
{statusbar(W2, '#000', '11:43')}
<div style="position:absolute;left:0;right:0;top:{int(W2*.12)}px;height:{int(98*s2)}px;background:rgba(246,246,246,.94);border-bottom:1px solid #d8d8dc;{IOS}">
<div style="position:absolute;left:{int(10*s2)}px;top:{int(16*s2)}px;color:#007AFF;font-size:{int(30*s2)}px;font-weight:400">&#8249;</div>
<div style="position:absolute;left:0;right:0;top:{int(8*s2)}px;text-align:center">
<div style="width:{int(52*s2)}px;height:{int(52*s2)}px;border-radius:50%;margin:0 auto;background:linear-gradient(#a5a9b3,#858a96);color:#fff;font-weight:600;font-size:{int(21*s2)}px;display:flex;align-items:center;justify-content:center">ER</div>
<div style="font-size:{int(12*s2)}px;color:#000;margin-top:{int(5*s2)}px">Example Roofing &#8250;</div></div></div>
<div style="position:absolute;left:0;right:0;top:{int(W2*.12)+int(112*s2)}px">
<div style="text-align:center;font-size:{int(11.5*s2)}px;color:#8a8a8e;margin-bottom:{int(8*s2)}px;{IOS}"><b style="font-weight:600">Text Message</b><br>Today 11:42 AM</div>
{bubble("Hi, this is Example Roofing! Sorry we missed your call, we're up on a job right now. What can we help you with?", False, s2)}
<div style="height:{int(8*s2)}px"></div>
{bubble("Leak over the garage after the storm last night", True, s2, False)}
{bubble("Can someone look at it this week?", True, s2)}
<div style="text-align:center;font-size:{int(11.5*s2)}px;color:#8a8a8e;margin:{int(12*s2)}px 0 {int(8*s2)}px;{IOS}">11:58 AM</div>
{bubble("Got it. This is Mike, just got off the roof. Calling you in 5.", False, s2)}
<div style="height:{int(8*s2)}px"></div>
{bubble("Perfect, thank you!", True, s2)}
<div style="text-align:right;font-size:{int(11*s2)}px;color:#8a8a8e;margin:{int(3*s2)}px {int(16*s2)}px 0;{IOS}">Delivered</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:{int(90*s2)}px;background:#fff;display:flex;align-items:flex-start;gap:{int(9*s2)}px;padding:{int(8*s2)}px {int(12*s2)}px;{IOS}">
<div style="width:{int(34*s2)}px;height:{int(34*s2)}px;border-radius:50%;background:#e9e9eb;color:#7c7c80;font-size:{int(24*s2)}px;display:flex;align-items:center;justify-content:center">+</div>
<div style="flex:1;height:{int(34*s2)}px;border:1px solid #c8c8cc;border-radius:{int(18*s2)}px;color:#a0a0a5;font-size:{int(16*s2)}px;display:flex;align-items:center;padding-left:{int(12*s2)}px">Text Message &middot; SMS</div></div>"""
P["11_iphone_3d_text"] = page(f"""
<div style="position:absolute;inset:0;background:linear-gradient(160deg,#D9BF72,#BA9941 70%)"></div>
<div style="position:absolute;left:80px;top:100px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:#2a2416">MISSED-CALL TEXT-BACK</div>
<div style="font:700 88px/0.98 CG;color:#0B0B0B;margin-top:22px">on a roof when it rings?<br><i>they still hear back.</i></div></div>
<div style="position:absolute;left:0;right:0;top:0;bottom:0;perspective:1800px">
{iphone(msgs, W2, "left:470px;top:440px;transform:rotateY(-22deg) rotateX(8deg) rotateZ(4deg);transform-style:preserve-3d", edge='left')}</div>
<div style="position:absolute;left:80px;top:520px;width:360px;font:500 30px/1.45 In;color:#1d1a12">you miss the call.<br><b style="color:#0B0B0B">a text goes out in seconds.</b><br><br>you call back when you're off the ladder, and the job's still yours.</div>""",
"#BA9941", "ink", "", "#2a2416")

# ---- C. Laptop on a table: website that books calls ----
site = f"""<div style="position:absolute;inset:0;background:#fff;{IOS}">
<div style="height:46px;background:#ececec;border-bottom:1px solid #d4d4d4;display:flex;align-items:center;padding:0 14px;gap:7px">
<span style="width:11px;height:11px;border-radius:50%;background:#ff5f57"></span><span style="width:11px;height:11px;border-radius:50%;background:#febc2e"></span><span style="width:11px;height:11px;border-radius:50%;background:#28c840"></span>
<div style="margin:0 auto;width:330px;height:26px;border-radius:7px;background:#fff;font-size:13px;color:#444;display:flex;align-items:center;justify-content:center">&#128274;&nbsp; exampleroofing.com</div></div>
<div style="height:54px;display:flex;align-items:center;justify-content:space-between;padding:0 28px;border-bottom:1px solid #eee">
<b style="font-size:19px;color:#1d2a3a;letter-spacing:.02em">EXAMPLE ROOFING</b>
<div style="display:flex;gap:20px;font-size:13px;color:#444"><span>Roof Repair</span><span>Storm Damage</span><span>Gutters</span><span>Reviews</span></div>
<div style="background:#e8742c;color:#fff;font-weight:700;font-size:13px;padding:8px 14px;border-radius:6px">Call (555) 010-4471</div></div>
<div style="position:absolute;left:0;right:0;top:100px;bottom:0;background:linear-gradient(90deg,rgba(18,30,46,.94) 45%,rgba(18,30,46,.55)),repeating-linear-gradient(115deg,#4a5a6a 0 18px,#3c4b5a 18px 36px);padding:46px 34px;color:#fff">
<div style="font-size:12px;letter-spacing:.2em;color:#f2a26b;font-weight:700">ROOF REPAIR &middot; STORM DAMAGE &middot; GUTTERS</div>
<div style="font-size:40px;font-weight:700;line-height:1.08;margin-top:12px;width:420px">Leaky roof? We'll be out this week.</div>
<div style="font-size:15px;color:#cdd5de;margin-top:12px;width:380px">Local, licensed crew. Free inspection and photos of what we find.</div>
<div style="display:flex;gap:12px;margin-top:22px"><div style="background:#e8742c;font-weight:700;font-size:16px;padding:13px 20px;border-radius:7px">&#128222; Call (555) 010-4471</div>
<div style="border:1.5px solid #fff;font-weight:600;font-size:16px;padding:12px 18px;border-radius:7px">Get a free quote</div></div>
<svg style="position:absolute;right:30px;bottom:0" width="300" height="290" viewBox="0 0 300 290"><polygon points="20,140 150,40 280,140" fill="#2e3f52"/><polygon points="20,140 150,40 280,140" fill="none" stroke="#e8742c" stroke-width="5"/><rect x="45" y="140" width="210" height="150" fill="#3a4c60"/><rect x="80" y="175" width="45" height="45" fill="#f2c27a" opacity=".85"/><rect x="175" y="175" width="45" height="45" fill="#f2c27a" opacity=".85"/><rect x="128" y="225" width="44" height="65" fill="#24323f"/><rect x="200" y="62" width="22" height="50" fill="#2e3f52"/></svg>
<div style="font-size:14px;margin-top:18px;color:#ffd27a">&#9733;&#9733;&#9733;&#9733;&#9733; <span style="color:#cdd5de">4.9 from 120+ reviews (example)</span></div></div></div>"""
P["12_laptop_table"] = page(f"""
<div style="position:absolute;inset:0;bottom:400px;background:radial-gradient(ellipse 900px 700px at 70% 30%,#2a2519,#0B0B0B 70%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:400px;overflow:hidden;background:linear-gradient(#7a5536,#5a3c24 30%,#3a2615 75%,#25180c)">
<div style="position:absolute;left:-200px;right:-200px;top:0;bottom:0;transform:perspective(500px) rotateX(55deg);transform-origin:50% 0;opacity:.55;background:repeating-linear-gradient(90deg,rgba(0,0,0,0) 0 37px,rgba(30,16,6,.35) 37px 39px,rgba(0,0,0,0) 39px 61px,rgba(255,220,170,.06) 61px 64px,rgba(0,0,0,0) 64px 90px)"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 700px 160px at 50% 0%,rgba(255,210,150,.18),transparent 70%)"></div></div>
<div style="position:absolute;left:80px;top:100px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">YOUR WEBSITE</div>
<div style="font:700 92px/0.98 CG;color:var(--paper);margin-top:20px">a pretty website is nice.<br><i style="color:var(--gold2)">one that books calls is better.</i></div></div>
<div style="position:absolute;left:150px;top:450px;width:780px;height:500px;border-radius:24px 24px 6px 6px;background:#1a1a1c;padding:16px 16px 22px;box-shadow:0 0 0 2px #8c8c90">
<div style="position:absolute;left:50%;top:0;width:110px;height:16px;margin-left:-55px;background:#1a1a1c;border-radius:0 0 8px 8px;z-index:3"></div>
<div style="position:relative;width:100%;height:100%;border-radius:8px;overflow:hidden">{site}</div></div>
<div style="position:absolute;left:150px;top:948px;width:780px;height:10px;background:linear-gradient(#5a5a5e,#2e2e31)"></div>
<div style="position:absolute;left:90px;top:956px;width:900px;height:22px;clip-path:polygon(2% 0,98% 0,100% 100%,0 100%);background:linear-gradient(#d8d8dc,#a9a9ae 55%,#7d7d82);border-radius:0 0 14px 14px"></div>
<div style="position:absolute;left:470px;top:956px;width:140px;height:9px;background:linear-gradient(#9a9a9f,#c4c4c8);border-radius:0 0 10px 10px"></div>
<div style="position:absolute;left:60px;top:960px;width:960px;height:44px;background:radial-gradient(ellipse at center,rgba(0,0,0,.7),transparent 70%)"></div>
<div style="position:absolute;right:80px;top:1070px;width:300px;font:500 24px/1.45 In;color:#f1e6cf;text-align:right">call button up top.<br>services up front.<br>reviews where they can see them.</div>""",
"#0B0B0B", "dark", "")


# ================= TRUE-3D DEVICES (thickness is real geometry, so the visible side is always correct) =================
SITE_IMG = (ROOT / "brand/site_home_desktop.png").as_uri()  # re-capture if the homepage changes

def iphone3d(screen, w, transform, depth=40):
    """iPhone with real body depth: stacked titanium layers behind the face inside preserve-3d.
    Rotate it however you like; perspective decides which edge shows."""
    h = int(w * 2.08); r = int(w * 0.165)
    layers = "".join(
        f'<div style="position:absolute;inset:0;border-radius:{r}px;transform:translateZ({-i}px);'
        f'background:linear-gradient(90deg,#77736b,#b8b3a8 20%,#d6d2c8 50%,#a8a397 80%,#6d6961)"></div>'
        for i in range(1, depth + 1))
    shadow = f'<div style="position:absolute;inset:0;border-radius:{r}px;transform:translateZ({-depth-1}px);box-shadow:0 60px 90px rgba(0,0,0,.45)"></div>'
    face = f"""<div style="position:absolute;inset:0;border-radius:{r}px;background:linear-gradient(135deg,#e2ded5,#a29d93 35%,#cfcac0 60%,#8f8a80)"></div>
<div style="position:absolute;inset:4px;border-radius:{r-4}px;background:#000"></div>
<div style="position:absolute;inset:{int(w*0.035)}px;border-radius:{r-int(w*0.035)+4}px;overflow:hidden;background:#fff">{screen}
<div style="position:absolute;left:50%;top:{int(w*0.028)}px;width:{int(w*0.29)}px;height:{int(w*0.085)}px;margin-left:-{int(w*0.145)}px;background:#000;border-radius:999px;z-index:9"></div>
<div style="position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.22) 0%,rgba(255,255,255,0) 32%);pointer-events:none;z-index:10"></div></div>"""
    return f"""<div style="position:absolute;width:{w}px;height:{h}px;transform-style:preserve-3d;{transform}">{shadow}{layers}
<div style="position:absolute;inset:0;transform:translateZ(0.5px)">{face}</div></div>"""

P["11_iphone_3d_text"] = page(f"""
<div style="position:absolute;inset:0;background:linear-gradient(160deg,#D9BF72,#BA9941 70%)"></div>
<div style="position:absolute;left:80px;top:100px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:#2a2416">MISSED-CALL TEXT-BACK</div>
<div style="font:700 88px/0.98 CG;color:#0B0B0B;margin-top:22px">on a roof when it rings?<br><i>they still hear back.</i></div></div>
<div style="position:absolute;left:80px;top:470px;width:360px;font:500 30px/1.45 In;color:#1d1a12">you miss the call.<br><b style="color:#0B0B0B">a text goes out in seconds.</b><br><br>you call back when you're off the ladder, and the job's still yours.</div>
<div style="position:absolute;inset:0;perspective:2000px;perspective-origin:30% 40%;transform-style:preserve-3d">
{iphone3d(msgs, W2, "left:470px;top:400px;transform:translateZ(-230px) rotateY(-26deg) rotateX(5deg) rotateZ(3deg)")}</div>""",
"#BA9941", "ink", "", "#2a2416")

# ---- Laptop: real 3D laptop (lid + keyboard deck + trackpad) on a table, showing groundwerxdigital.com ----
LW, LH, LD = 700, 448, 400   # lid width, lid height, base depth
keyrow = lambda n, h, first=0: '<div style="display:flex;gap:5px;margin-bottom:5px">' + (f'<div style="flex:{first} 0 0;height:{h}px;background:#1d1d1f;border-radius:4px"></div>' if first else '') + "".join(f'<div style="flex:1;height:{h}px;background:#1d1d1f;border-radius:4px"></div>' for _ in range(n)) + "</div>"
keys = keyrow(14, 18) + keyrow(13, 34, 1) + keyrow(13, 34, 1.4) + keyrow(12, 34, 1.8) + keyrow(11, 34, 2.4) + \
    '<div style="display:flex;gap:5px"><div style="flex:1;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:1;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:1;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:1.3;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:5.5;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:1.3;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:1;height:34px;background:#1d1d1f;border-radius:4px"></div><div style="flex:3;height:34px;background:#1d1d1f;border-radius:4px"></div></div>'
laptop = f"""
<div style="position:absolute;left:{(1080-LW)//2}px;top:440px;width:{LW}px;height:{LH}px;transform-style:preserve-3d">
  <!-- base deck (lies flat, extends toward viewer from the hinge) -->
  <div style="position:absolute;left:0;top:{LH}px;width:{LW}px;height:{LD}px;transform-origin:50% 0;transform:rotateX(90deg);transform-style:preserve-3d;
       background:linear-gradient(180deg,#b9babe,#d4d5d8 40%,#c3c4c8);border-radius:4px 4px 22px 22px">
    <div style="position:absolute;left:68px;right:68px;top:30px;padding:9px;background:#0f0f10;border-radius:10px">{keys}</div>
    <div style="position:absolute;left:50%;top:{LD-160}px;width:300px;height:132px;margin-left:-150px;border-radius:14px;background:linear-gradient(#c8c9cd,#d9dadd);box-shadow:inset 0 0 0 1.5px #a9aaae"></div>
    <!-- front edge (thickness) -->
    <div style="position:absolute;left:0;bottom:0;width:{LW}px;height:16px;transform-origin:50% 100%;transform:rotateX(-90deg);background:linear-gradient(#a3a4a8,#6f7074);border-radius:0 0 18px 18px"></div>
    <div style="position:absolute;inset:0;transform:translateZ(-17px);border-radius:4px 4px 22px 22px;box-shadow:0 0 80px 30px rgba(0,0,0,.55)"></div>
  </div>
  <!-- lid, tilted back slightly -->
  <div style="position:absolute;left:0;top:0;width:{LW}px;height:{LH}px;transform-origin:50% 100%;transform:rotateX(-12deg);transform-style:preserve-3d">
    <div style="position:absolute;inset:0;transform:translateZ(-7px);border-radius:22px 22px 6px 6px;background:#9fa0a4"></div>
    <div style="position:absolute;inset:0;border-radius:22px 22px 6px 6px;background:#0c0c0d;box-shadow:inset 0 0 0 2px #a6a7ab">
      <div style="position:absolute;left:50%;top:0;width:96px;height:15px;margin-left:-48px;background:#0c0c0d;border-radius:0 0 8px 8px;z-index:3"></div>
      <div style="position:absolute;left:16px;right:16px;top:16px;bottom:16px;border-radius:6px;overflow:hidden;background:#000">
        <img src="{SITE_IMG}" style="width:100%;height:100%;object-fit:cover;object-position:top left;display:block">
        <div style="position:absolute;inset:0;background:linear-gradient(120deg,rgba(255,255,255,.10),rgba(255,255,255,0) 38%)"></div></div>
    </div>
  </div>
</div>"""

P["12_laptop_table"] = page(f"""
<div style="position:absolute;inset:0;bottom:430px;background:radial-gradient(ellipse 900px 700px at 70% 30%,#2a2519,#0B0B0B 70%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:430px;overflow:hidden;background:linear-gradient(#6e4c30,#553a22 35%,#3a2715 75%,#26180c)">
<div style="position:absolute;left:-300px;right:-300px;top:0;height:900px;transform:perspective(600px) rotateX(62deg);transform-origin:50% 0;opacity:.6;background:repeating-linear-gradient(90deg,rgba(0,0,0,0) 0 41px,rgba(30,16,6,.38) 41px 43px,rgba(0,0,0,0) 43px 67px,rgba(255,220,170,.07) 67px 70px,rgba(0,0,0,0) 70px 96px)"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 760px 200px at 50% 0%,rgba(255,210,150,.16),transparent 70%)"></div></div>
<div style="position:absolute;left:80px;top:96px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">YOUR WEBSITE</div>
<div style="font:700 92px/0.98 CG;color:var(--paper);margin-top:20px">a pretty website is nice.<br><i style="color:var(--gold2)">one that books calls is better.</i></div></div>
<div style="position:absolute;inset:0;perspective:1700px;perspective-origin:50% 8%;transform-style:preserve-3d">{laptop}</div>""",
"#0B0B0B", "dark", "")

async def main():
    only = sys.argv[1:]
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, html in P.items():
            if only and name not in only: continue
            f = TMP / f"{name}.html"; f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            png = TMP / f"{name}.png"; await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(OUT / f"{name}.jpg", quality=86); print("wrote", name)
        await b.close()
asyncio.run(main())
