# GroundWerx Social: Strategy

This file is the single source of truth for GroundWerx Digital's social content.
Tyler's Claude and Cade's Claude both follow it. Change the strategy here, not in chat.

## Who we are
- GroundWerx Digital: done-for-you marketing for owner-operated businesses.
- Run by two brothers, Tyler and Cade Maas. No account managers, no handoffs.
- Website: groundwerxdigital.com · Phone: (952) 333-8122
- Tagline: "Get Found Online"

## Who we're talking to
- Primary: trades and contractors (roofers, HVAC, plumbers, electricians, landscapers, remodelers, etc.).
- Also: realtors and other local pros.
- They're busy, on job sites, and don't want another dashboard. They care about calls and booked jobs.

## What we sell (talk about these)
1. **Google Business Profile**: built out, optimized weekly, updates posted. (Local SEO and lead-gen ads are part of this and the website, not separate services.)
2. **Review automation**: every finished job triggers a review request.
3. **Missed-call text-back**: if they can't pick up, the caller gets a text within a minute.
4. **Website builds**: fast, mobile-first, built to book calls.

## Offers
- **Free 15-minute consultation** with the brothers. (It's 15 minutes. Not 20.)
- **Referral program**: refer a business, get $100 cash; they get their first month free; existing clients can take a free month instead; unlimited referrals. Link: groundwerxdigital.com/referral
- **Do not post package prices.** Packages are being reworked. Ignore the old FAQ tiers.

## Why us
- Two brothers run every account, start to finish. One point of contact.
- Done-for-you: no dashboards, no weekly homework.
- Month-to-month.
- Straight monthly reports: calls, booked jobs, reviews earned.

## Voice
- Straight-talking, plain, no fluff. Talk like someone who knows a contractor's week.
- Lowercase headlines on graphics. Short sentences.
- Never promise rankings, specific results, or timelines.
- Any example math must be labeled as an example.
- Don't name real competitors. Fake business names must be clearly generic.

## Content pillars (rotate)
1. **Money you're losing**: missed calls, no reviews, invisible profile.
2. **Quick wins**: GBP tips, review tips, "check this today."
3. **Proof**: client results, before/after (only real, approved results).
4. **Behind GroundWerx**: the brothers, how we work.
5. **Offers**: free consult, referral program.
6. **From Tyler / From Cade** (founder posts): first-person posts in one brother's voice.
   - **About once a month.** At most one founder post per calendar month, and at least 4 weeks after the last one. Most weekly batches will have none.
   - **Alternate Cade and Tyler. Never the same founder twice in a row.** Before planning, find the most recent founder post in `calendar/log.md` (pillar "From Tyler" or "From Cade") and use the other brother.
   - The graphic names that founder (e.g. "Cade Maas, co-founder, GroundWerx Digital", corner tag "from cade"). The caption is in his voice, refers to the other brother by name ("that's what Tyler and I do"), and is signed "- Cade" or "- Tyler".
   - Every other pillar is written as GroundWerx ("we"), with no personal sign-off, so it doesn't read as another founder post.
   - Log the pillar as "From Tyler" or "From Cade" so the rotation can be tracked.

## Cadence and channels
- 5 posts/week, weekdays only (no weekends). Metricool free plan = 20 posts/month.
- Stagger times between 10am and 5pm Central. Metricool's data shows weekday peaks around 10am, noon and 5pm.
- Facebook Page now. Instagram and Google Business Profile when connected.
- GBP gets a text update version of the week's best post.

## Design rules
- Black (#0B0B0B), gold (#BA9941 / light #D9BF72), cream (#F2EEE4).
- Fonts (all in `brand/fonts`): Cormorant Garamond (serif headlines), Inter (body), **Oswald** (bold block-letter headlines), **JetBrains Mono** (typewriter text on receipts, work orders, blueprints), **Caveat** (handwritten checkmarks and signatures only).
- Size: 1080x1350 (4:5 portrait). That's the tallest feed size on Instagram and Facebook, so keep it. Instagram's profile grid trims a sliver off each side, so keep text at least 80px from the left and right edges.
- Logo wordmark bottom-left on every graphic (gold on dark, ink on light).

### Make the profile grid look varied (Tyler, Oct 28)
The old posts all looked the same: thin border, small label, lowercase serif headline top-left, logo bottom-left, with only the background color changing. **Every post needs its own silhouette**, so it reads as a different kind of post even as a thumbnail.
- **Approved looks library:** `templates/looks_library.py`, with reference renders in `looks/examples/`. Reuse its helpers and copy the look. Don't approximate it.
  1. Caution tape (two crossed tapes, Oswald headline)
  2. Work order / job ticket (mono font, handwritten checks)
  3. Receipt (thermal receipt, zigzag edge, labeled example math)
  5. Blueprint (gold grid paper, site-map boxes, title block)
  6. Split poster (gold top / black bottom, huge Oswald)
  7. Big chat bubbles (brand-colored, no phone frame)
  8. Giant search bar with autocomplete
  9. Tear-off flyer (pinned paper, phone-number pull tabs, one torn off)
  10. iPhone lock screen with notifications
  11. 3D iPhone with a Messages thread
  12. Laptop on a table showing a website
- The classic layouts (dark editorial, cream, solid gold, giant-number stat, myth vs. fact, this vs. that, quote card) are still allowed, but **use at most 1-2 classic layouts per week**. The rest come from the library above.
- Never repeat a look within the same week, and never use the same look two posts in a row across weeks. Check `calendar/log.md`, and log the look's name in the Layout column.
- You can invent new looks in the same spirit (a real-world object or a bold poster). Show Tyler new ones as mockups before scheduling them.

### Devices (phones, tablets, computers)
- **Anything that imitates a phone screen must look exactly like a real iPhone running iOS. Don't use brand colors on the screen.** Notifications are frosted light-grey rounded cards with the green Phone app icon, a bold title ("Missed Call"), the body text, and the time in grey on the right. Messages uses grey bubbles for incoming texts and green bubbles for the customer's own SMS texts (blue only for iMessage), plus "Text Message / Today 11:42 AM", "Delivered", and an iOS status bar. Brand colors go around the phone, never inside it.
- Phones and tablets are always drawn as a **real device shape**: titanium rim, black bezel, Dynamic Island, rounded corners. Never a bare floating screen. No Apple logo.
- **3D must be physically correct.** Use `iphone3d()`, which gives the phone real depth inside a CSS 3D scene, so the side you see is always the side turned toward the viewer. Never fake thickness with a flat shadow or offset on one side. (Oct 28 mistake: the phone was tilted one way and the "thickness" showed on the wrong side.) Zoom in on the render and check the visible edge is on the side closer to the viewer.
- Use a **laptop on a table** sometimes, especially for website topics. It's a real 3D laptop (lid, keyboard, trackpad, aluminum front edge) sitting on the table surface, never floating above it.
- Business names and numbers on screens are examples ("Example Roofing", 555-010-xxxx) and say so somewhere on the post, unless the screen shows GroundWerx itself.

### Showing our own website (groundwerxdigital.com)
- When a post shows our own site, use the real homepage (`brand/site_home_desktop.png`). Re-capture it if the homepage has changed.
- **Only point to things that are actually visible in the screenshot.** The homepage hero shows: the phone number and a "Get in touch" button in the header, "more calls. more booked jobs. we handle the rest.", a one-line description of what we do, a "Call (952) 333-8122" button, and the "talk to one of the brothers" contact form. Services are not listed above the fold (each service has its own page elsewhere on the site).
- Never pair our site with advice it doesn't visibly follow (for example "list every service on your homepage"). That looks hypocritical. If a tip doesn't match our homepage, use an example business site instead.

### Copy lessons
- "Example" labels go only on specific made-up numbers, businesses or math. Don't stamp "example profile" on generic descriptions (Oct 28: removed from the caution-tape post).
- Checklists and tips should leave room for GroundWerx. Show the reader mostly done with one item left, and close with "that's where we come in" or a similar line, never "fix it this week" DIY homework that suggests they don't need us.
- Every visual metaphor should make sense at a glance. A receipt, work order or flyer should hold content that belongs on that object.
- Before scheduling, look at every render at full size and as a 360px thumbnail. Check for clipped headlines, text hidden behind devices, labels touching the logo, and devices covering the logo.

## Rules for Claude
- Before planning: read this file and `calendar/log.md`, and check Metricool's scheduled posts.
- Weekly batch runs every Wednesday morning in VETO MODE: schedule next week's posts as live posts, then send Tyler a summary with every image and caption. He replies only to change or cancel. Cancel = set the post back to draft.
- One-off or ad-hoc posts outside the weekly batch still need explicit approval in chat first.
- Tyler and Cade don't use the Metricool app. Everything goes through Claude.
- After scheduling: add a row to `calendar/log.md` with who made it.
