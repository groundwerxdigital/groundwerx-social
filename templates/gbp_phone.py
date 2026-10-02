"""Render the 'roofer near me' post: a phone showing a business profile in local search.
Usage: python3 templates/gbp_phone.py  -> images/2026-10-w1/p2_gbp_phone.jpg
"""
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = (ROOT / "brand/fonts").as_uri()
LOGO = (ROOT / "brand/logo-wordmark.png").as_uri()
OUT = ROOT / "images/2026-10-w1/p2_gbp_phone.jpg"

def roof(sky1, sky2, wall, roofc, x=0):
    return f"""<svg viewBox="0 0 160 120" preserveAspectRatio="xMidYMid slice" width="100%" height="100%">
<defs><linearGradient id="g{x}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky1}"/><stop offset="1" stop-color="{sky2}"/></linearGradient></defs>
<rect width="160" height="120" fill="url(#g{x})"/>
<rect x="0" y="96" width="160" height="24" fill="#5d7a4a"/>
<rect x="34" y="62" width="92" height="40" fill="{wall}"/>
<polygon points="24,64 80,26 136,64" fill="{roofc}"/>
<g stroke="rgba(0,0,0,.18)" stroke-width="1.2">
<line x1="38" y1="57" x2="122" y2="57"/><line x1="50" y1="49" x2="110" y2="49"/><line x1="62" y1="41" x2="98" y2="41"/></g>
<rect x="70" y="78" width="18" height="24" fill="#3b3b3b"/>
<rect x="44" y="72" width="16" height="13" fill="#cfe3f2"/><rect x="100" y="72" width="16" height="13" fill="#cfe3f2"/>
</svg>"""

ICON = {
 "call": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/>',
 "dir": '<path d="M21.7 11.3l-9-9a1 1 0 0 0-1.4 0l-9 9a1 1 0 0 0 0 1.4l9 9a1 1 0 0 0 1.4 0l9-9a1 1 0 0 0 0-1.4zM14 14.5V12h-4v3H8v-4a1 1 0 0 1 1-1h5V7.5l3.5 3.5z"/>',
 "web": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm6.9 6h-2.9a15.6 15.6 0 0 0-1.4-3.6A8 8 0 0 1 18.9 8zM12 4c.8 1.2 1.5 2.5 1.9 4h-3.8c.4-1.4 1.1-2.8 1.9-4zM4.3 14a8.2 8.2 0 0 1 0-4h3.4a16.5 16.5 0 0 0 0 4zm.8 2h2.9c.3 1.3.8 2.5 1.4 3.6A8 8 0 0 1 5.1 16zM8 8H5.1a8 8 0 0 1 4.3-3.6C8.8 5.5 8.3 6.7 8 8zm4 12c-.8-1.2-1.5-2.5-1.9-4h3.8c-.4 1.4-1.1 2.8-1.9 4zm2.3-6H9.7a14.7 14.7 0 0 1 0-4h4.6a14.7 14.7 0 0 1 0 4zm.3 5.6c.6-1.1 1.1-2.3 1.4-3.6h2.9a8 8 0 0 1-4.3 3.6zm1.7-5.6a16.5 16.5 0 0 0 0-4h3.4a8.2 8.2 0 0 1 0 4z"/>',
 "save": '<path d="M17 3H7a2 2 0 0 0-2 2v16l7-3 7 3V5a2 2 0 0 0-2-2z"/>',
}
def btn(k, label):
    return f"""<div class="ab"><div class="ac"><svg viewBox="0 0 24 24" width="26" height="26" fill="#1f6fd1">{ICON[k]}</svg></div><div class="al">{label}</div></div>"""

CSS = f"""
@font-face{{font-family:CG;font-weight:700;src:url({F}/cormorant-garamond-latin-700-normal.woff2)}}
@font-face{{font-family:CG;font-weight:700;font-style:italic;src:url({F}/cormorant-garamond-latin-700-italic.woff2)}}
@font-face{{font-family:In;font-weight:400;src:url({F}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:In;font-weight:500;src:url({F}/inter-latin-500-normal.woff2)}}
@font-face{{font-family:In;font-weight:600;src:url({F}/inter-latin-600-normal.woff2)}}
@font-face{{font-family:In;font-weight:700;src:url({F}/inter-latin-700-normal.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#0B0B0B}}
.page{{position:relative;width:1080px;height:1350px;font-family:In;color:#F2EEE4;
 background:radial-gradient(ellipse 800px 600px at 80% 30%,rgba(186,153,65,.16),transparent 65%),#0B0B0B}}
.page::before{{content:"";position:absolute;inset:36px;border:1.5px solid rgba(186,153,65,.35)}}
.kick{{position:absolute;left:96px;top:96px;font-weight:600;font-size:22px;letter-spacing:.32em;text-transform:uppercase;color:#BA9941}}
.h{{position:absolute;left:96px;top:138px;width:900px;font-family:CG;font-weight:700;font-size:92px;line-height:.98;color:#F2EEE4}}
.h em{{font-style:italic;color:#D9BF72}}
/* phone */
.phone{{position:absolute;left:96px;top:340px;width:520px;height:830px;border-radius:66px;background:#1b1b1b;padding:16px;
 box-shadow:0 0 0 2px #3a3a3a,0 40px 80px rgba(0,0,0,.6)}}
.scr{{position:relative;width:100%;height:100%;border-radius:52px;background:#fff;overflow:hidden;color:#1f1f1f}}
.isl{{position:absolute;top:14px;left:50%;transform:translateX(-50%);width:120px;height:34px;border-radius:20px;background:#111}}
.sb{{display:flex;justify-content:space-between;padding:20px 34px 0;font-weight:600;font-size:19px}}
.srch{{margin:26px 18px 0;height:58px;border-radius:30px;background:#f1f3f4;display:flex;align-items:center;gap:14px;padding:0 22px;font-size:21px;color:#1f1f1f}}
.tabs{{display:flex;gap:26px;padding:16px 26px 0;font-size:17px;color:#5f6368;border-bottom:1px solid #e3e3e3}}
.tabs span{{padding-bottom:12px}} .tabs .on{{color:#1f1f1f;font-weight:600;border-bottom:3px solid #1f1f1f}}
.card{{padding:20px 24px 0}}
.nm{{font-size:31px;font-weight:600;letter-spacing:-.01em}}
.rt{{margin-top:8px;font-size:18px;color:#5f6368;display:flex;align-items:center;gap:6px}}
.rt b{{color:#1f1f1f;font-weight:500}} .st{{color:#f2a400;letter-spacing:1px;font-size:19px}}
.op{{display:flex;align-items:center;gap:4px;margin-top:6px;font-size:18px;color:#5f6368}} .op .g{{margin-right:2px;color:#188038;font-weight:600}}
.acts{{display:flex;justify-content:space-between;margin-top:20px;padding:0 6px}}
.ab{{display:flex;flex-direction:column;align-items:center;gap:8px;width:92px}}
.ac{{width:62px;height:62px;border-radius:50%;background:#e8f0fe;display:flex;align-items:center;justify-content:center}}
.ab:first-child .ac{{background:#1f6fd1}} .ab:first-child svg{{fill:#fff}}
.al{{font-size:16px;color:#1f6fd1;font-weight:500}}
.photos{{display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:96px 96px;gap:5px;margin-top:22px;border-radius:14px;overflow:hidden}}
.photos div:first-child{{grid-row:1/3}}
.rv{{margin-top:20px;display:flex;gap:14px}}
.av{{flex:none;width:40px;height:40px;border-radius:50%;background:#7b5bd6;color:#fff;font-weight:600;display:flex;align-items:center;justify-content:center;font-size:18px}}
.rv .t{{font-size:17px;line-height:1.4;color:#3c4043}} .rv .t .st{{font-size:16px}}
.hrs{{margin-top:16px;padding-top:14px;border-top:1px solid #e3e3e3;font-size:17px;color:#3c4043;display:flex;justify-content:space-between}}
/* numbered markers */
.bd{{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:#BA9941;color:#0B0B0B;font-weight:700;font-size:17px;box-shadow:0 0 0 3px #fff;flex:none}}
.ab{{position:relative}} .ab .bd{{position:absolute;top:-8px;right:4px}}
.photos{{position:relative}} .pbd{{position:absolute;right:10px;bottom:10px}}
/* callouts */
.co{{position:absolute;left:656px;width:330px}}
.co{{display:flex;gap:18px}} .co .bd{{width:44px;height:44px;font-size:22px;box-shadow:none;margin-top:-2px}}
.co .k{{font-weight:600;font-size:28px;color:#F2EEE4}}
.co .d{{margin-top:6px;font-size:22px;line-height:1.4;color:#B9B2A2}}
.foot{{position:absolute;left:96px;right:96px;bottom:70px;display:flex;justify-content:space-between;align-items:center}}
.foot img{{height:54px;mix-blend-mode:lighten}}
.foot .r{{font-size:18px;letter-spacing:.2em;text-transform:uppercase;color:#8d8778}}
"""

def co(top, n, k, d):
    return f'<div class="co" style="top:{top}px"><div class="bd">{n}</div><div><div class="k">{k}</div><div class="d">{d}</div></div></div>'

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=page>
<div class=kick>this is what they see first</div>
<div class=h>your google<br><em>business profile.</em></div>
<div class=phone><div class=scr><div class=isl></div>
 <div class=sb><span>9:41</span><span>&#9679;&#9679;&#9679; &#9646;</span></div>
 <div class=srch><svg viewBox="0 0 24 24" width="24" height="24" fill="#5f6368"><path d="M15.5 14h-.8l-.3-.3A6.5 6.5 0 1 0 14 15.5l.3.3v.8l5 5 1.5-1.5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>roofer near me</div>
 <div class=tabs><span class=on>All</span><span>Maps</span><span>Images</span><span>Reviews</span></div>
 <div class=card>
  <div class=nm>Summit Roofing Co.</div>
  <div class=rt><b>4.9</b><span class=st>&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>(214) &middot; Roofing contractor</span>&nbsp;<span class=bd>1</span></div>
  <div class=op><span class=g>Open</span> &middot; Closes 6 PM &middot; Serves your area&nbsp; <span class=bd>2</span></div>
  <div class=acts>{btn("call","Call").replace('<div class="ab">','<div class="ab"><span class=bd>3</span>',1)}{btn("dir","Directions")}{btn("web","Website")}{btn("save","Save")}</div>
  <div class=photos><div>{roof("#9cc6ea","#e7f1fa","#e8dccb","#3f4a57",1)}</div><div>{roof("#f4c99a","#fbe7d2","#d7c3a8","#6b3f2a",2)}</div><div>{roof("#b9d3e8","#eef4f9","#c9c9c9","#2f3a44",3)}</div><span class="bd pbd">4</span></div>
  <div class=rv><div class=av>J</div><div class=t><span class=st>&#9733;&#9733;&#9733;&#9733;&#9733;</span> &nbsp;2 days ago<br>Came out the next morning and fixed the leak. Fair price, cleaned up after.</div></div>
  <div class=hrs><span>Hours</span><span>Mon&ndash;Sat &middot; 7 AM&ndash;6 PM</span></div>
 </div>
</div></div>
{co(560, 1, "5-star reviews", "what people check first.")}
{co(700, 2, "right hours", "wrong hours lose the call.")}
{co(840, 3, "one-tap call", "they call straight from search.")}
{co(980, 4, "real job photos", "your crew, your work.")}
<div class=foot><img src="{LOGO}"><div class=r>example profile</div></div>
</div></body></html>"""

async def main():
    tmp = ROOT / "templates/_gbp_phone.html"; tmp.write_text(HTML)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1350})
        await pg.goto(tmp.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
        png = ROOT / "templates/_gbp_phone.png"; await pg.screenshot(path=str(png)); await b.close()
    Image.open(png).convert("RGB").save(OUT, quality=88); png.unlink(); tmp.unlink(); print("wrote", OUT)
asyncio.run(main())
