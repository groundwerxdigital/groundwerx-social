"""Render GroundWerx posts for the week of Nov 16-20, 2026.
Usage: python3 templates/week7_build.py [file.jpg ...]
Outputs 1080x1350 JPGs to images/2026-11-w3/.
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

OUT = ROOT / "images/2026-11-w3"; OUT.mkdir(parents=True, exist_ok=True)
TMP = ROOT / "templates/_tmp_w7"; TMP.mkdir(exist_ok=True)
POSTS = {}

# ---------- Mon Nov 16 · Money you're losing · look 10 iPHONE LOCK SCREEN: weekend missed calls ----------
W1 = 470
lock = f"""<div style="position:absolute;inset:0;background:radial-gradient(circle at 25% 20%,#7aa7d9,transparent 55%),radial-gradient(circle at 85% 75%,#e59a6b,transparent 55%),linear-gradient(170deg,#3d5f8c,#2a2b4f 60%,#5b3a4a)"></div>
{L.statusbar(W1, '#fff', '', left=False)}
<div style="position:absolute;left:0;right:0;top:{int(W1*.17)}px;text-align:center;color:#fff;{IOS}">
<div style="font-weight:600;font-size:{int(W1*.047)}px;opacity:.92">Monday, November 16</div>
<div style="font-weight:700;font-size:{int(W1*.235)}px;line-height:1;letter-spacing:-.03em;margin-top:{int(W1*.005)}px;opacity:.95">7:02</div></div>
<div style="position:absolute;left:0;right:0;top:{int(W1*.66)}px">
{L.ios_note('Sat 9:14 AM', 'Missed Call', '(555) 010-4418', W1)}{L.ios_note('Sat 2:37 PM', 'Missed Call', '(555) 010-6602', W1)}{L.ios_note('Sun 11:05 AM', 'Missed Call', '(555) 010-1957', W1)}{L.ios_note('Sun 4:48 PM', 'Missed Call', '(555) 010-3320', W1)}</div>
<div style="position:absolute;left:{int(W1*.12)}px;right:{int(W1*.12)}px;bottom:{int(W1*.11)}px;display:flex;justify-content:space-between">
<div style="width:{int(W1*.115)}px;height:{int(W1*.115)}px;border-radius:50%;background:rgba(40,40,50,.45);display:flex;align-items:center;justify-content:center"><svg width="40%" viewBox="0 0 24 24"><path fill="#fff" d="M8 2h8v3.5l-2 3.5v11.5a1.5 1.5 0 0 1-1.5 1.5h-1A1.5 1.5 0 0 1 10 20.5V9L8 5.5z"/><circle cx="12" cy="13" r="1.3" fill="#3a3a48"/></svg></div>
<div style="width:{int(W1*.115)}px;height:{int(W1*.115)}px;border-radius:50%;background:rgba(40,40,50,.45);display:flex;align-items:center;justify-content:center"><svg width="45%" viewBox="0 0 24 24"><path fill="#fff" d="M4 7h3l2-2h6l2 2h3a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1zm8 3a4 4 0 1 0 0 8 4 4 0 0 0 0-8z"/></svg></div></div>
<div style="position:absolute;left:50%;bottom:{int(W1*.025)}px;width:{int(W1*.3)}px;height:{int(W1*.011)}px;margin-left:-{int(W1*.15)}px;background:#fff;border-radius:9px"></div>"""
POSTS["p1_lockscreen_weekend.jpg"] = page(f"""
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 700px 600px at 80% 40%,rgba(186,153,65,.22),transparent 65%)"></div>
<div style="position:absolute;left:80px;top:110px;width:430px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">MONDAY MORNING</div>
<div class=os style="font-size:92px;color:var(--paper);margin-top:26px">your weekend<br>calls didn't<br><span style="color:var(--gold2)">wait for<br>monday.</span></div>
<div style="font:400 28px/1.5 In;color:#CFC9BA;margin-top:36px">with missed-call text-back, every caller gets a text within a minute, even on a saturday.</div></div>
<div style="position:absolute;inset:0;perspective:2000px;perspective-origin:30% 40%;transform-style:preserve-3d">
{L.iphone3d(lock, W1, "left:560px;top:170px;transform:translateZ(-120px) rotateY(-20deg) rotateX(4deg) rotateZ(3deg)", depth=34)}</div>""",
"#0B0B0B", "dark", "example phone")

# ---------- Tue Nov 17 · Quick wins · look 8 GIANT SEARCH BAR: they search the problem ----------
sug = ["furnace making <b>a loud banging noise</b>", "furnace making <b>a burning smell</b>", "furnace making <b>a clicking sound</b>", "furnace <b>not turning on</b>"]
POSTS["p2_search_furnace.jpg"] = page(f"""
<div style="position:absolute;left:80px;right:80px;top:110px"><div style="font:600 21px In;letter-spacing:.3em;color:#8a6f28">QUICK WIN &middot; GOOGLE PROFILE</div>
<div style="font:700 100px/0.98 CG;color:#0B0B0B;margin-top:22px">they don't search<br>your name.</div>
<div style="font:700 italic 70px CG;color:#8a6f28;margin-top:22px">they search the problem.</div></div>
<div style="position:absolute;left:60px;right:60px;top:530px;background:#fff;border-radius:60px;box-shadow:0 24px 60px rgba(11,11,11,.16);overflow:hidden">
<div style="display:flex;align-items:center;gap:26px;padding:34px 44px;font:500 50px In;color:#0B0B0B">
<svg width=48 height=48 viewBox="0 0 24 24"><circle cx=10 cy=10 r=7 fill=none stroke="#8a6f28" stroke-width=2.6 /><line x1=15.2 y1=15.2 x2=21 y2=21 stroke="#8a6f28" stroke-width=2.8 stroke-linecap=round /></svg>
<span>furnace making<span style="display:inline-block;width:4px;height:52px;background:#BA9941;vertical-align:-8px;margin-left:4px"></span></span></div>
<div style="border-top:1.5px solid #ece6d6">{"".join(f'<div style="padding:20px 44px 20px 118px;font:400 33px In;color:#55503f">{s}</div>' for s in sug)}</div></div>
<div style="position:absolute;left:80px;right:80px;top:1035px;font:500 30px/1.45 In;color:#3b382f">list every job you do on your google profile, in plain words: <b style="color:#0B0B0B">&ldquo;furnace repair,&rdquo; not just &ldquo;HVAC.&rdquo;</b></div>""",
"#F2EEE4", "ink", "quick win", "#7d776a")

# ---------- Wed Nov 18 · Behind GroundWerx · look 2 WORK ORDER carousel (5): how we build a website ----------
def check(t, c=1):
    mark = '<div style="position:absolute;left:-4px;top:-26px;font:700 64px Hw;color:#a5812c">&#10003;</div>' if c else ''
    return f"""<div style="display:flex;align-items:center;gap:22px;padding:24px 0;border-bottom:1.5px solid #cfc6b0">
<div style="width:40px;height:40px;border:2.5px solid #0B0B0B;position:relative;flex:none">{mark}</div>
<div class=mo style="font-size:31px;color:#1a1814;line-height:1.3">{t}</div></div>"""
def work_order(no, fields, body, foot, rot=-1.8, tag="how we work"):
    fl = "".join(f'<div>{a}</div><div style="color:#0B0B0B;font-weight:700">{b}</div>' for a, b in fields)
    return page(f"""
<div style="position:absolute;left:96px;right:96px;top:84px;transform:rotate({rot}deg);background:#F7F3E8;padding:54px 56px 48px;
box-shadow:0 30px 60px rgba(0,0,0,.35),0 2px 0 #ddd3bb">
<div style="position:absolute;left:50%;top:-34px;width:230px;height:70px;margin-left:-115px;background:linear-gradient(#3a3a3a,#111);border-radius:14px"></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:4px solid #0B0B0B;padding-bottom:18px">
<div class=os style="font-size:78px;color:#0B0B0B">work order</div><div class=mo style="font-size:26px;color:#6b6352">{no}</div></div>
<div class=mo style="display:grid;grid-template-columns:auto 1fr;gap:12px 26px;margin-top:28px;font-size:25px;color:#6b6352">{fl}</div>
<div style="margin-top:22px">{body}</div>
{foot}
</div>""", "linear-gradient(160deg,#D9BF72,#BA9941 75%)", "ink", tag, "#2a2416")
sig = lambda label: f"""<div style="text-align:right;margin-top:30px"><div style="font:700 56px Hw;color:#a5812c;transform:rotate(-4deg)">Tyler &amp; Cade</div>
<div class=mo style="font-size:18px;color:#6b6352;border-top:1.5px solid #0B0B0B;padding-top:6px;width:300px;margin-left:auto">{label}</div></div>"""
F_BASE = [("CUSTOMER", "YOUR BUSINESS"), ("JOB", "NEW WEBSITE")]
POSTS["p3_workorder_1_v2.jpg"] = work_order("No. 0018", F_BASE + [("CREW", "TYLER &amp; CADE")], f"""
<div class=os style="font-size:112px;color:#0B0B0B;margin-top:26px;line-height:.9">how we<br>build your<br><span style="color:#a5812c">website.</span></div>
<div class=mo style="font-size:26px;color:#2b2820;line-height:1.55;margin-top:30px">3 steps. one point of contact.<br>and no blank-page questionnaire.</div>""",
"""<div class=mo style="font-size:24px;color:#a5812c;margin-top:40px;font-weight:700">SWIPE FOR THE JOB SHEET &rarr;</div>""")
steps = [  # revised Nov 12 per Tyler: step 1 is a mock-up built from what's already online, then a call to finalize
 ("STEP 1 OF 3", "WE BUILD A MOCK-UP", ["you sign up. no forms to fill out", "we pull what's online about you", "google profile, reviews, photos", "we build a mock-up of your site"],
  "you don't start from a blank page."),
 ("STEP 2 OF 3", "WE WALK THROUGH IT TOGETHER", ["a call to walk through the mock-up", "fix anything we got wrong", "add anything we missed", "you sign off before it goes live"],
  "nothing goes live until you've seen it."),
 ("STEP 3 OF 3", "LAUNCH, THEN KEEP IT CURRENT", ["linked from your google profile", "new service or photo? text it to us", "we make the change for you", "month-to-month. no long contract"],
  "you don't log in to anything."),
]
for i, (st, job, items, note) in enumerate(steps):
    POSTS[f"p3_workorder_{i+2}_v2.jpg"] = work_order(f"{st}", F_BASE + [("TASK", job)],
        "".join(check(t) for t in items),
        f"""<div class=mo style="font-size:27px;color:#2b2820;margin-top:40px;font-weight:700">{note}</div>{sig("DONE BY")}""",
        rot=[1.4, -1.2, 1.6][i])
POSTS["p3_workorder_5_v2.jpg"] = work_order("No. 0018", F_BASE + [("STATUS", "READY WHEN YOU ARE")], f"""
<div class=os style="font-size:104px;color:#0B0B0B;margin-top:26px;line-height:.9">need a<br>new website?</div>
<div style="font:700 54px/1.08 CG;color:#0B0B0B;margin-top:30px">send us a message.<br><i style="color:#8a6f28">we'll get it started for you.</i></div>
<div class=mo style="font-size:24px;color:#2b2820;line-height:1.55;margin-top:26px">we start with what's already<br>online about you.</div>""",
sig("SIGNED"), rot=-1.4)

# ---------- Thu Nov 19 · Offers · look 7 BIG CHAT BUBBLES: we look you up first (revised Nov 12 per Tyler: no 15-minute-call pitch) ----------
POSTS["p4_bubbles_lookup.jpg"] = page(f"""
<div style="position:absolute;left:70px;top:90px;font:600 22px In;letter-spacing:.3em;color:var(--gold)">BEFORE WE EVER TALK</div>
<div style="position:absolute;left:0;right:0;top:150px;text-align:center;font:500 20px In;color:#8d8676">questions we get a lot</div>
{L.bub("So what happens if I reach out?", False, 200)}
{L.bub("We look you up first. Your Google profile, reviews, website and social pages.", True, 340, "Tyler &amp; Cade")}
{L.bub("Then a sales pitch?", False, 590)}
{L.bub("Nope. The few fixes we think would move the needle most for you. Keep the list, with us or without us.", True, 740)}
<div style="position:absolute;left:70px;right:70px;top:990px"><div style="font:700 70px/1 CG;color:var(--paper)">we do our homework<br><i style="color:var(--gold2)">before we call.</i></div></div>""",
"#141310", "dark", "free look")

# ---------- Fri Nov 20 · Quick wins · classic THIS VS. THAT: reply to the 5-star reviews too ----------
star = '<span style="color:#FBBC04">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
def rcard(top, label, lab_col, reply, border, op=1):
    return f"""<div style="position:absolute;left:80px;right:80px;top:{top}px;opacity:{op}">
<div style="font:700 30px Os;letter-spacing:.14em;color:{lab_col};text-transform:uppercase">{label}</div>
<div style="margin-top:14px;background:#1b1a16;border:2.5px solid {border};border-radius:22px;padding:28px 32px">
<div style="font:500 24px In;color:#a8a293">{star}&nbsp; new 5-star review about a furnace repair</div>
<div style="margin-top:18px;padding-left:22px;border-left:3px solid #4a463b;font:500 30px/1.45 In;color:#F2EEE4">
<div style="font:600 20px In;letter-spacing:.12em;color:#8d8676;margin-bottom:8px">REPLY FROM THE OWNER</div>{reply}</div></div></div>"""
POSTS["p5_thisvsthat_replies.jpg"] = page(f"""
<div style="position:absolute;left:80px;top:96px;right:80px">
<div style="font:600 21px In;letter-spacing:.3em;color:var(--gold)">QUICK WIN &middot; REVIEWS</div>
<div style="font:700 88px/0.98 CG;color:var(--paper);margin-top:20px">reply to the<br><i style="color:var(--gold2)">5-star ones too.</i></div></div>
{rcard(400, "this", "#8d8676", "Thanks!", "#3a372f", .8)}
{rcard(720, "that", "#D9BF72", "Thanks for calling us when your furnace quit. Glad we got the heat back on in Lakeview. Stay warm! &ndash; Mike, Example Heating", "#D9BF72")}
<div style="position:absolute;left:80px;right:80px;top:1090px;font:500 28px/1.45 In;color:#CFC9BA">the next customer reads your replies too. <b style="color:var(--gold2)">a real reply shows a real person runs the place.</b></div>""",
"#0B0B0B", "dark", "example review")

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
