"""Render GroundWerx posts for the week of Nov 23-27, 2026 (Thanksgiving week).
Usage: python3 templates/week8_build.py [file.jpg ...]
Outputs 1080x1350 JPGs to images/2026-11-w4/.
"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "templates"))
_argv = sys.argv; sys.argv = [_argv[0], "__import_only__"]   # looks_library renders on import; render nothing
import looks_library as L
sys.argv = _argv
page, LOGO_INK, IOS = L.page, L.LOGO_INK, L.IOS

OUT = ROOT / "images/2026-11-w4"; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / "templates/_tmp_w8"; TMP.mkdir(exist_ok=True)
POSTS = {}

# ---------- Mon Nov 23 · Money you're losing · look 1 CAUTION TAPE: where does your Website button go? ----------
POSTS["p1_caution_website_button.jpg"] = page(L.tape(95, -7, "CAUTION") + L.tape(165, 6, "DEAD END") + """
<div style="position:absolute;left:80px;right:80px;top:350px">
<div style="font:600 24px In;letter-spacing:.3em;color:var(--gold);text-transform:uppercase">quick check &middot; google profile</div>
<div class=os style="font-size:118px;color:var(--paper);margin-top:24px">where does your<br>&ldquo;website&rdquo; button<br><span style="color:var(--gold2)">actually go?</span></div>
<div style="margin-top:46px;display:flex;gap:16px;flex-wrap:wrap">
""" + "".join(f'<div style="border:2px solid rgba(217,191,114,.55);color:#CFC9BA;font:500 27px In;padding:14px 22px">{x}</div>' for x in
["a facebook page nobody updates", "a site that won't load", "a domain you stopped paying for"]) + """</div>
<div style="font:400 29px/1.5 In;color:#a8a293;margin-top:44px;width:860px">it's one of the last things they tap before they call.<br><b style="color:var(--paper)">a dead end sends them to the next guy.</b></div>
<div style="font:700 50px/1.1 CG;color:var(--gold2);margin-top:60px"><i>hit a dead end? send us a message.</i></div>
</div>""",
"radial-gradient(ellipse at 50% 45%,#1d1a12,#0B0B0B 70%)", "dark")

# ---------- Tue Nov 24 · Behind GroundWerx · look 11 3D iPHONE MESSAGES: the "#1 on Google, guaranteed" text ----------
W2 = 520; s = W2 / 390
person = f"""<svg width="{int(30*s)}" height="{int(30*s)}" viewBox="0 0 24 24"><circle cx="12" cy="8.5" r="4.3" fill="#fff"/><path d="M3.5 21a8.5 8.5 0 0 1 17 0z" fill="#fff"/></svg>"""
spam = f"""<div style="position:absolute;inset:0;background:#fff"></div>
{L.statusbar(W2, '#000', '9:14')}
<div style="position:absolute;left:0;right:0;top:{int(W2*.12)}px;height:{int(98*s)}px;background:rgba(246,246,246,.94);border-bottom:1px solid #d8d8dc;{IOS}">
<div style="position:absolute;left:{int(10*s)}px;top:{int(16*s)}px;color:#007AFF;font-size:{int(30*s)}px;font-weight:400">&#8249;</div>
<div style="position:absolute;left:0;right:0;top:{int(8*s)}px;text-align:center">
<div style="width:{int(52*s)}px;height:{int(52*s)}px;border-radius:50%;margin:0 auto;background:linear-gradient(#a5a9b3,#858a96);display:flex;align-items:flex-end;justify-content:center;overflow:hidden">{person}</div>
<div style="font-size:{int(12*s)}px;color:#000;margin-top:{int(5*s)}px">+1 (555) 010-8834 &#8250;</div></div></div>
<div style="position:absolute;left:0;right:0;top:{int(W2*.12)+int(112*s)}px">
<div style="text-align:center;font-size:{int(11.5*s)}px;color:#8a8a8e;margin-bottom:{int(8*s)}px;{IOS}"><b style="font-weight:600">Text Message</b><br>Today 9:12 AM</div>
{L.bubble("Hi! Is this the owner? We can get your business to #1 on Google in 30 days. GUARANTEED!!", False, s, False)}
{L.bubble("Only 3 spots left in your area. Reply YES to claim yours", False, s)}
<div style="text-align:center;font-size:{int(11.5*s)}px;color:#8a8a8e;margin:{int(18*s)}px {int(30*s)}px 0;line-height:1.35;{IOS}">The sender is not in your contact list.<br><span style="color:#007AFF">Report Junk</span></div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:{int(90*s)}px;background:#fff;display:flex;align-items:flex-start;gap:{int(9*s)}px;padding:{int(8*s)}px {int(12*s)}px;{IOS}">
<div style="width:{int(34*s)}px;height:{int(34*s)}px;border-radius:50%;background:#e9e9eb;color:#7c7c80;font-size:{int(24*s)}px;display:flex;align-items:center;justify-content:center">+</div>
<div style="flex:1;height:{int(34*s)}px;border:1px solid #c8c8cc;border-radius:{int(18*s)}px;color:#a0a0a5;font-size:{int(16*s)}px;display:flex;align-items:center;padding-left:{int(12*s)}px">Text Message &middot; SMS</div></div>"""
POSTS["p2_iphone_guarantee_text.jpg"] = page(f"""
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 760px 700px at 78% 62%,rgba(186,153,65,.28),transparent 70%)"></div>
<div style="position:absolute;left:80px;top:100px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:#8a6f28">HOW WE WORK</div>
<div style="font:700 92px/0.98 CG;color:#0B0B0B;margin-top:22px">got this text?<br><i style="color:#8a6f28">here's the truth.</i></div></div>
<div style="position:absolute;left:80px;top:470px;width:370px;font:500 30px/1.45 In;color:#3b382f">nobody controls google's rankings.<br><b style="color:#0B0B0B">anyone who guarantees #1 is guessing.</b><br><br>we do the work, and every month you see the calls, booked jobs and reviews. straight numbers. no guarantees.</div>
<div style="position:absolute;left:80px;top:1010px;font:600 18px In;letter-spacing:.24em;color:#7d776a">EXAMPLE TEXT</div>
<div style="position:absolute;inset:0;perspective:2000px;perspective-origin:30% 40%;transform-style:preserve-3d">
{L.iphone3d(spam, W2, "left:490px;top:410px;transform:translateZ(-200px) rotateY(-24deg) rotateX(5deg) rotateZ(3deg)", depth=38)}</div>""",
"#F2EEE4", "ink")

# ---------- Wed Nov 25 · Offers (free online presence review) · look 6 SPLIT POSTER carousel (6): they check 4 things ----------
def split(top_html, bottom_html, corner="BEFORE THEY CALL", n=""):
    return page(f"""
<div style="position:absolute;left:0;right:0;top:0;height:675px;background:#D9BF72"></div>
<div style="position:absolute;right:80px;top:84px;font:600 22px In;letter-spacing:.3em;color:#0B0B0B">{corner}</div>
{f'<div style="position:absolute;left:80px;top:84px;font:600 22px In;letter-spacing:.3em;color:#0B0B0B">{n}</div>' if n else ''}
<div style="position:absolute;left:80px;right:80px;bottom:715px">{top_html}</div>
<div style="position:absolute;left:80px;right:80px;top:745px">{bottom_html}</div>""", "#0B0B0B", "dark")
BIG = lambda t, sz=180: f'<div class=os style="font-size:{sz}px;color:#0B0B0B;line-height:.86">{t}</div>'
LOW = lambda t: f'<div style="font:500 54px/1.3 In;color:#F2EEE4">{t}</div>'
SUB = lambda t: f'<div style="font:400 30px/1.5 In;color:#a8a293;margin-top:30px">{t}</div>'
POSTS["p3_split_1.jpg"] = split(BIG("they check<br>you out<br>first.", 170),
    f'<div class=os style="font-size:120px;color:#D9BF72;line-height:.9">4 things they<br>look at.</div>{SUB("before anyone calls you. swipe &rarr;")}')
cards = [("01", "your<br>reviews.", "how many.<br>how recent.<br><span style='color:#D9BF72'>whether you replied.</span>"),
         ("02", "your<br>photos.", "real jobs, from this year.<br><span style='color:#D9BF72'>not stock photos.</span>"),
         ("03", "your hours<br>&amp; phone.", "does google say you're open?<br><span style='color:#D9BF72'>does the number ring through?</span>"),
         ("04", "your<br>website.", "does it load on their phone?<br><span style='color:#D9BF72'>can they call in one tap?</span>")]
for i, (n, top, low) in enumerate(cards):
    POSTS[f"p3_split_{i+2}.jpg"] = split(BIG(top), LOW(low), n=f"{n} / 04")
POSTS["p3_split_6.jpg"] = split(BIG("want us<br>to check<br>all 4?", 170),
    f'<div style="font:700 62px/1.08 CG;color:#F2EEE4">send us a message with<br>your business name.</div>'
    f'<div style="font:400 30px/1.5 In;color:#CFC9BA;margin-top:30px">we look you up and send back the few fixes we&rsquo;d make first.<br><b style="color:#D9BF72">free. yours to keep, with us or without us.</b></div>',
    corner="FREE LOOK")

# ---------- Thu Nov 26 · Thanksgiving · text only (no graphic) ----------

# ---------- Fri Nov 27 · Quick wins · look 12 LAPTOP ON A TABLE: the 5-second website test (example business site) ----------
SW, SH = L.LW - 32, L.LH - 32
site = f"""<div style="position:absolute;inset:0;background:#fff;{IOS}">
<div style="height:34px;background:#ececec;border-bottom:1px solid #d4d4d4;display:flex;align-items:center;padding:0 12px;gap:6px">
<span style="width:9px;height:9px;border-radius:50%;background:#ff5f57"></span><span style="width:9px;height:9px;border-radius:50%;background:#febc2e"></span><span style="width:9px;height:9px;border-radius:50%;background:#28c840"></span>
<div style="margin:0 auto;width:270px;height:20px;border-radius:6px;background:#fff;font-size:11px;color:#444;display:flex;align-items:center;justify-content:center">exampleroofing.com</div></div>
<div style="height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 22px;border-bottom:1px solid #eee">
<b style="font-size:16px;color:#1d2a3a;letter-spacing:.02em">EXAMPLE ROOFING</b>
<div style="display:flex;gap:16px;font-size:11px;color:#444"><span>Roof Repair</span><span>Storm Damage</span><span>Gutters</span><span>Reviews</span></div>
<div style="background:#e8742c;color:#fff;font-weight:700;font-size:11px;padding:7px 11px;border-radius:5px">Call (555) 010-4471</div></div>
<div style="position:absolute;left:0;right:0;top:78px;bottom:0;background:linear-gradient(90deg,rgba(18,30,46,.95) 50%,rgba(18,30,46,.6)),repeating-linear-gradient(115deg,#4a5a6a 0 16px,#3c4b5a 16px 32px);padding:38px 28px;color:#fff;overflow:hidden">
<div style="font-size:11px;letter-spacing:.2em;color:#f2a26b;font-weight:700">SERVING ALL OF EXAMPLE COUNTY</div>
<div style="font-size:36px;font-weight:700;line-height:1.08;margin-top:10px;width:380px">Roof repair &amp; storm damage. Out this week.</div>
<div style="font-size:13px;color:#cdd5de;margin-top:10px;width:330px">Local, licensed crew. Free inspection and photos of what we find.</div>
<div style="display:flex;gap:10px;margin-top:20px"><div style="background:#e8742c;font-weight:700;font-size:14px;padding:11px 16px;border-radius:6px">Call (555) 010-4471</div>
<div style="border:1.5px solid #fff;font-weight:600;font-size:14px;padding:10px 14px;border-radius:6px">Get a free quote</div></div>
<svg style="position:absolute;right:24px;bottom:0" width="230" height="230" viewBox="0 0 300 290"><polygon points="20,140 150,40 280,140" fill="#2e3f52"/><polygon points="20,140 150,40 280,140" fill="none" stroke="#e8742c" stroke-width="5"/><rect x="45" y="140" width="210" height="150" fill="#3a4c60"/><rect x="80" y="175" width="45" height="45" fill="#f2c27a" opacity=".85"/><rect x="175" y="175" width="45" height="45" fill="#f2c27a" opacity=".85"/><rect x="128" y="225" width="44" height="65" fill="#24323f"/><rect x="200" y="62" width="22" height="50" fill="#2e3f52"/></svg>
</div></div>"""
laptop = L.laptop.replace(
    f'<img src="{L.SITE_IMG}" style="width:100%;height:100%;object-fit:cover;object-position:top left;display:block">', site)
assert laptop != L.laptop
POSTS["p5_laptop_5_second_test.jpg"] = page(f"""
<div style="position:absolute;inset:0;bottom:430px;background:radial-gradient(ellipse 900px 700px at 70% 30%,#2a2519,#0B0B0B 70%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:430px;overflow:hidden;background:linear-gradient(#6e4c30,#553a22 35%,#3a2715 75%,#26180c)">
<div style="position:absolute;left:-300px;right:-300px;top:0;height:900px;transform:perspective(600px) rotateX(62deg);transform-origin:50% 0;opacity:.6;background:repeating-linear-gradient(90deg,rgba(0,0,0,0) 0 41px,rgba(30,16,6,.38) 41px 43px,rgba(0,0,0,0) 43px 67px,rgba(255,220,170,.07) 67px 70px,rgba(0,0,0,0) 70px 96px)"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 760px 200px at 50% 0%,rgba(255,210,150,.16),transparent 70%)"></div></div>
<div style="position:absolute;left:80px;top:96px;width:920px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">QUICK WIN &middot; YOUR WEBSITE</div>
<div style="font:700 92px/0.98 CG;color:var(--paper);margin-top:20px">the 5-second test.<br><i style="color:var(--gold2)">can a stranger tell&hellip;</i></div></div>
<div style="position:absolute;inset:0;perspective:1700px;perspective-origin:50% 8%;transform-style:preserve-3d">{laptop}</div>
<div style="position:absolute;left:80px;right:80px;top:350px;display:flex;gap:16px">""" + "".join(f'<div class=mo style="border:2px solid rgba(217,191,114,.6);color:#f1e6cf;font-size:25px;padding:12px 18px;white-space:nowrap"><span style="color:var(--gold2)">{n}</span> {t}</div>' for n, t in [("01", "what you do"), ("02", "where you work"), ("03", "how to call you")]) + f"""</div>
<div style="position:absolute;right:80px;top:1270px;font:600 18px In;letter-spacing:.24em;color:#b89a6a">EXAMPLE SITE</div>""",
"#0B0B0B", "dark", "")

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
