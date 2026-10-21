"""Render GroundWerx posts for the week of Oct 26-30, 2026.
Usage: python3 templates/week4_build.py
Outputs 1080x1350 JPGs to images/2026-10-w4/.
"""
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
TMP = ROOT / "templates/_tmp"; TMP.mkdir(exist_ok=True)
W4 = ROOT / "images/2026-10-w4"; W4.mkdir(parents=True, exist_ok=True)

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

CTA = """<div style="margin-top:50px;display:inline-block;border:2px solid var(--gold);padding:28px 40px">
<div style="font-weight:700;font-size:44px;color:var(--gold2)">(952) 333-8122</div>
<div style="font-size:28px;color:#CFC9BA;margin-top:8px;letter-spacing:.04em">groundwerxdigital.com</div></div>"""

# ---------- Mon Oct 26: dark editorial carousel (6), the referral that googled you ----------
N = 6
POSTS[W4 / "p1_referral_search_1.jpg"] = page("""<div class=kicker style="margin-top:130px">money you're losing</div>
<div class=h style="font-size:128px;margin-top:60px">someone just<br>recommended you.<br><em>then they<br>googled you.</em></div>
<div class=rule></div>
<div class=body style="max-width:820px">word of mouth still runs through a search bar.</div>""", "dark", "<span class=swipe>swipe &rarr;</span>")
slides = [
 ("the handoff", "&ldquo;call these<br>guys.&rdquo;", "your customer tells a neighbor about you. the neighbor doesn't write your number down. <b>they search your name.</b>"),
 ("what they see", "your profile is the<br><em>second impression.</em>",
  "<div style='margin-top:-6px'>" + "".join(f"<div style='display:flex;gap:22px;padding:16px 0;border-top:1.5px solid var(--line)'><span style='color:var(--gold);font-weight:700'>&mdash;</span><span>{t}</span></div>" for t in ["your reviews: how many, how recent", "photos of real jobs", "hours and a phone number that work", "a website that loads on a phone"]) + "</div>"),
 ("where it slips", "thin profile?<br><em>they keep<br>scrolling.</em>", "a few old reviews, no photos, a site that won't load. the referral was yours. <b>the call goes to whoever looks ready.</b>"),
 ("make it stick", "check this<br><em>today.</em>",
  "<div style='margin-top:-6px'>" + "".join(f"<div style='display:flex;gap:22px;padding:16px 0;border-top:1.5px solid var(--line)'><span style='color:var(--gold);font-weight:700'>{i}</span><span>{t}</span></div>" for i, t in enumerate(["search your business name like a customer would", "ask every happy customer for a review", "add photos from this month's jobs", "make sure your phone and hours are right"], 1)) + "</div>"),
]
for i, (k, h, b) in enumerate(slides, 2):
    POSTS[W4 / f"p1_referral_search_{i}.jpg"] = page(f"""<div class=kicker style="margin-top:110px">{k}</div>
<div class=h style="font-size:124px;margin-top:40px">{h}</div>
<div class=rule></div>
<div class=body style="max-width:860px;font-size:40px">{b}</div>""", "dark", f"{i} / {N}")
POSTS[W4 / "p1_referral_search_6.jpg"] = page(f"""<div class=kicker style="margin-top:120px">want us to look with you?</div>
<div class=h style="font-size:120px;margin-top:40px">free 15-minute call<br><em>with tyler and cade.</em></div>
<div class=rule></div>
<div class=body style="max-width:820px">we'll pull up your business the way a customer would and walk through it with you.</div>
{CTA}""", "dark", "6 / 6")

# ---------- Tue Oct 27: cream + phone mock (example profile), holiday hours ----------
HOURS_CSS = """
.hr{margin-top:12px;font-size:17px;line-height:1.55;color:#3c4043}
.hr .row{display:flex;justify-content:space-between;padding:3px 0}
.hr .hol{background:#fff4dc;margin:0 -10px;padding:6px 10px;border-radius:8px}
.hr .cl{color:#c5221f;font-weight:600}
.btns{display:flex;gap:10px;margin-top:14px}
.btns span{flex:1;text-align:center;border:1px solid #dadce0;border-radius:20px;padding:9px 0;font-size:15px;color:#1a5fb4;font-weight:600}
"""
POSTS[W4 / "p2_phone_holiday_hours.jpg"] = page(f"""<style>{PHONE_CSS}{HOURS_CSS}</style>
<div class=kicker style="margin-top:0">quick win &middot; do it this week</div>
<div class=h style="font-size:90px;margin-top:24px">closed thanksgiving?<br><em>tell google first.</em></div>
<div class=phone><div class=scr><div class=isl></div>
 <div class=sb><span>9:41</span><span>&#9679;&#9679;&#9679; &#9646;</span></div>
 <div class=srch><svg viewBox="0 0 24 24" width="22" height="22" fill="#5f6368"><path d="M15.5 14h-.8l-.3-.3A6.5 6.5 0 1 0 14 15.5l.3.3v.8l5 5 1.5-1.5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>furnace repair near me</div>
 <div class=tabs><span class=on>All</span><span>Maps</span><span>Images</span><span>Reviews</span></div>
 <div class=card>
  <div class=nm>Example Heating &amp; Air</div>
  <div class=rt><b>4.8</b><span class=st>&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>(64) &middot; HVAC contractor</span></div>
  <div class=btns><span>Call</span><span>Directions</span><span>Website</span></div>
  <div class=sec><span>Hours</span><span class=bd>1</span></div>
  <div class=hr>
   <div class="row hol"><span>Thu, Nov 26 (Thanksgiving)</span><span class=cl>Closed</span></div>
   <div class=row><span>Fri, Nov 27</span><span>8 AM&ndash;5 PM</span></div>
   <div class=row><span>Thu, Dec 24</span><span>8 AM&ndash;12 PM</span></div>
   <div class="row hol"><span>Fri, Dec 25 (Christmas)</span><span class=cl>Closed</span></div>
  </div>
  <div class=sec><span>Updates from the business</span><span class=bd>2</span></div>
  <div class=upd><div class=when>Posted 2 days ago</div>Closed Thanksgiving Day. Our emergency line is open for no-heat calls.</div>
  <div class=sec><span>Regular hours</span><span class=bd>3</span></div>
  <div class=upd style="background:#fff;padding:6px 16px 0;margin-top:4px">Mon&ndash;Fri 7 AM&ndash;5 PM &middot; Sat&ndash;Sun closed</div>
 </div>
</div></div>
{co(470, 1, "set holiday hours", "thanksgiving, christmas, new year's. set them ahead of time.")}
{co(700, 2, "post an update", "if you run an emergency line over the holiday, say so.")}
{co(930, 3, "check your regular hours", "switching to winter hours? fix those while you're in there.")}
""", "cream", "example profile")

# ---------- Wed Oct 28: solid gold giant-number, one business / three phone numbers ----------
rows = [("your google profile", "(555) 010-4471"), ("your facebook page", "(555) 010-2289"), ("an old directory listing", "(555) 010-9036")]
rl = "".join(f"""<div style="display:flex;justify-content:space-between;align-items:baseline;padding:22px 0;border-top:1.5px solid rgba(11,11,11,.35)">
<div style="font-size:32px;font-weight:500;color:#1d1a12">{a}</div><div style="font-size:34px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums">{b}</div></div>""" for a, b in rows)
POSTS[W4 / "p3_bignumber_three_numbers.jpg"] = page(f"""<div class=kicker style="margin-top:0">money you're losing</div>
<div style="display:flex;align-items:flex-end;gap:34px;margin-top:10px">
<div class=h style="font-size:360px;line-height:.78;letter-spacing:-.03em">3</div>
<div class=h style="font-size:84px;line-height:1;padding-bottom:6px">phone numbers.<br><em>one business.</em></div></div>
<div style="margin-top:56px">{rl}<div style="border-top:1.5px solid rgba(11,11,11,.35)"></div></div>
<div class=body style="margin-top:44px;font-size:34px;max-width:860px">customers call whichever one they find first. <b>make sure your name, address and phone match everywhere.</b></div>""",
"goldbg", "example numbers")

# ---------- Thu Oct 29: myth vs. fact single (split dark / cream), job photos ----------
POSTS[W4 / "p4_myth_job_photos.jpg"] = f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}
.top{{position:absolute;left:0;top:0;width:1080px;height:520px;background:var(--ink);color:var(--paper);padding:84px 96px 0}}
.bot{{position:absolute;left:0;top:520px;width:1080px;height:830px;background:var(--paper);color:var(--ink);padding:56px 96px 0}}
.tag{{display:inline-block;font-weight:700;font-size:22px;letter-spacing:.3em;text-transform:uppercase;padding:10px 18px}}
.li{{display:flex;gap:22px;padding:11px 0;border-top:1.5px solid rgba(11,11,11,.14);font-size:30px;color:#3b382f}}
.li span:first-child{{color:#8a6f28;font-weight:700;width:30px}}
</style></head><body><div class="page cream" style="padding:0">
<div class=top><div class=tag style="border:2px solid #6d675a;color:#9A9483">myth</div>
<div class=h style="font-size:96px;margin-top:36px;color:#b9b3a4">&ldquo;nobody looks at<br>the photos on my<br>google profile.&rdquo;</div></div>
<div class=bot><div class=tag style="background:var(--gold);color:var(--ink)">fact</div>
<div class=h style="font-size:78px;margin-top:22px">photos show you're<br><em style="color:#8a6f28">a real outfit.</em></div>
<div style="font-size:28px;color:#3b382f;margin-top:18px;margin-bottom:10px">snap a few on every job. post some each month:</div>
<div class=li><span>&#10003;</span><span>before and after</span></div>
<div class=li><span>&#10003;</span><span>the crew at work</span></div>
<div class=li><span>&#10003;</span><span>the truck with your name on it</span></div>
<div class=li><span>&#10003;</span><span>the finished job, cleaned up</span></div>
<div style="font-size:24px;color:#7d776a;margin-top:12px">get the homeowner's ok before posting their place.</div>
</div>
<div class=foot><img src="{LOGO_INK}"><div class=r>quick win</div></div></div></body></html>"""

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
