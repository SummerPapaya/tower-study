# SPDX-License-Identifier: MIT AND PolyForm-Noncommercial-1.0.0 (code MIT, drawing data PolyForm Noncommercial; see LICENSE)
"""Generate assets/hero.svg — the animated README banner for The Tower Study.
Pure CSS animations (no SMIL, no script) so it plays inside GitHub's <img> sandbox
and stops under prefers-reduced-motion.

Usage: python3 assets/make_hero.py [output.svg]        (defaults to assets/hero.svg)
       python3 assets/make_hero.py --og [output.svg]   1200x630 social-card variant (defaults to assets/og.svg)"""
import math, os, random, sys

W, H = 1200, 520
OG = "--og" in sys.argv       # social card: 1200x630, square corners, 55px more sky above and cloud below
Y0, VH = (-55, 630) if OG else (0, H)
CX = 880                      # tower centre line
rng = random.Random(7)
f = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")
out = []
o = out.append

def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u**3*a + 3*u*u*t*b + 3*u*t*t*c + t**3*d for a, b, c, d in zip(p0, p1, p2, p3))

def quad(p0, p1, p2, t):
    u = 1 - t
    return tuple(u*u*a + 2*u*t*b + t*t*c for a, b, c in zip(p0, p1, p2))

STAR4 = "M0-1L.25-.25 1 0 .25.25 0 1-.25.25-1 0-.25-.25z"   # unit 4-point sparkle

# ---------------------------------------------------------------- header + style
o(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 {Y0} {W} {VH}" width="{W}" height="{VH}" role="img" aria-labelledby="t d">
<title id="t">塔楼书房 · The Tower Study</title>
<desc id="d">A two-storey fairytale tower floating above a sea of clouds at dusk: a warm study upstairs, a witch's bedroom with a glowing moon lamp downstairs, a broom circling the tower, and petals, fireflies, leaves and snow drifting past as the seasons turn.</desc>
<style>
.a{{animation-timing-function:ease-in-out;animation-iteration-count:infinite}}
.tw{{animation:tw 4s ease-in-out infinite}}
@keyframes tw{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
.pulse{{animation:pulse 5s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
.drift1{{animation:drift 95s linear infinite}}
.drift2{{animation:drift 60s linear infinite}}
@keyframes drift{{to{{transform:translateX(-1200px)}}}}
.wisp{{animation:wisp 16s ease-in-out infinite alternate}}
@keyframes wisp{{to{{transform:translateX(46px)}}}}
.float{{animation:float 8s ease-in-out infinite}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-7px)}}}}
.bx{{animation:bx 6s cubic-bezier(.37,0,.63,1) infinite alternate}}
.by{{animation:by 6s cubic-bezier(.37,0,.63,1) infinite alternate}}
@keyframes bx{{from{{transform:translateX(-196px)}}to{{transform:translateX(196px)}}}}
@keyframes by{{from{{transform:translateY(-34px)}}to{{transform:translateY(34px)}}}}
.front{{animation:front 12s linear infinite}}
.back{{opacity:0;animation:back 12s linear infinite}}
@keyframes front{{0%,49.9%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes back{{0%,49.9%{{opacity:0}}50%,100%{{opacity:1}}}}
.wob{{animation:wob 1.7s ease-in-out infinite alternate}}
@keyframes wob{{from{{transform:rotate(-9deg)}}to{{transform:rotate(-2deg)}}}}
.bob{{animation:bob 4.6s ease-in-out infinite alternate}}
@keyframes bob{{from{{transform:translateY(-4px) rotate(-7deg)}}to{{transform:translateY(5px) rotate(6deg)}}}}
.tail{{animation:tail 2.8s ease-in-out infinite alternate}}
@keyframes tail{{from{{transform:rotate(-14deg)}}to{{transform:rotate(12deg)}}}}
.blink{{animation:blink 5s linear infinite}}
@keyframes blink{{0%,93%,100%{{transform:scaleY(1)}}95%{{transform:scaleY(.1)}}}}
.spin{{animation:spin 14s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.shoot{{opacity:0;animation:shoot 11s ease-in infinite 2s}}
@keyframes shoot{{0%{{transform:translate(0,0);opacity:0}}1.5%{{opacity:1}}8%{{transform:translate(250px,82px);opacity:0}}100%{{transform:translate(250px,82px);opacity:0}}}}
.season{{opacity:0;animation:season 24s linear infinite}}
.sp{{opacity:1}}
.su{{animation-delay:-18s}}.au{{animation-delay:-12s}}.wi{{animation-delay:-6s}}
@keyframes season{{0%,21%{{opacity:1}}25%,96%{{opacity:0}}100%{{opacity:1}}}}
.ia{{fill:#8cc46a;animation:ivyA 24s linear infinite}}
.ib{{fill:#9fd07a;animation:ivyB 24s linear infinite}}
@keyframes ivyA{{0%,21%{{fill:#8cc46a}}25%,46%{{fill:#4f8a47}}50%,71%{{fill:#c8472d}}75%,96%{{fill:#b9a898}}100%{{fill:#8cc46a}}}}
@keyframes ivyB{{0%,21%{{fill:#9fd07a}}25%,46%{{fill:#3f7a3f}}50%,71%{{fill:#e39a3b}}75%,96%{{fill:#cdbfb2}}100%{{fill:#9fd07a}}}}
.pill{{animation:pill 24s ease-in-out infinite}}
@keyframes pill{{0%,21%{{transform:translateX(0)}}25%,46%{{transform:translateX(70px)}}50%,71%{{transform:translateX(140px)}}75%,96%{{transform:translateX(210px)}}100%{{transform:translateX(0)}}}}
.fall{{animation:fall 9s linear infinite}}
@keyframes fall{{from{{transform:translateY(-30px)}}to{{transform:translateY(560px)}}}}
.sway{{animation:sway 2.6s ease-in-out infinite alternate}}
@keyframes sway{{from{{transform:translateX(-16px)}}to{{transform:translateX(16px)}}}}
.roll{{animation:spin 5s linear infinite}}
.ffly{{animation:ffly 7s ease-in-out infinite}}
@keyframes ffly{{0%,100%{{transform:translate(0,0);opacity:.2}}30%{{opacity:1}}50%{{transform:translate(14px,-26px);opacity:.35}}75%{{transform:translate(-10px,-44px);opacity:1}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
text{{font-kerning:normal}}
.zh{{font-family:"Songti SC","STSong","Noto Serif CJK SC","Source Han Serif SC","Noto Serif SC","SimSun",serif}}
.en{{font-family:"Cormorant Garamond","Cormorant",Georgia,"Times New Roman",serif}}
</style>
<defs>
<clipPath id="frame"><rect y="{Y0}" width="{W}" height="{VH}" rx="{0 if OG else 24}"/></clipPath>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="{H}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#0b1026"/><stop offset=".34" stop-color="#1c2254"/><stop offset=".6" stop-color="#453c7c"/><stop offset=".8" stop-color="#b9829a"/><stop offset="1" stop-color="#f5c79d"/></linearGradient>
<radialGradient id="vig" cx="600" cy="250" r="760" gradientUnits="userSpaceOnUse"><stop offset=".55" stop-color="#0b1026" stop-opacity="0"/><stop offset="1" stop-color="#0b1026" stop-opacity=".55"/></radialGradient>
<radialGradient id="halo"><stop offset="0" stop-color="#ffd9a0" stop-opacity=".42"/><stop offset=".55" stop-color="#ffc7a0" stop-opacity=".12"/><stop offset="1" stop-color="#ffc7a0" stop-opacity="0"/></radialGradient>
<radialGradient id="moonHalo"><stop offset="0" stop-color="#fff1cf" stop-opacity=".45"/><stop offset="1" stop-color="#fff1cf" stop-opacity="0"/></radialGradient>
<linearGradient id="wall" x1="762" x2="998" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ead6b5"/><stop offset=".28" stop-color="#f8ecd6"/><stop offset=".62" stop-color="#ecd8b9"/><stop offset="1" stop-color="#c7a984"/></linearGradient>
<linearGradient id="base" x1="762" x2="998" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#cbb08b"/><stop offset=".3" stop-color="#dcc3a0"/><stop offset="1" stop-color="#a88a67"/></linearGradient>
<linearGradient id="roof" x1="728" x2="1032" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#5a64a6"/><stop offset=".45" stop-color="#3c4582"/><stop offset="1" stop-color="#232957"/></linearGradient>
<radialGradient id="study" cx="880" cy="262" r="62" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff4c9"/><stop offset=".55" stop-color="#ffd27e"/><stop offset="1" stop-color="#e88f47"/></radialGradient>
<radialGradient id="studySide" cx=".5" cy=".6" r=".7"><stop offset="0" stop-color="#ffe6a8"/><stop offset="1" stop-color="#d98a4c"/></radialGradient>
<radialGradient id="bedroom" cx="874" cy="386" r="44" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ffe0a3"/><stop offset=".35" stop-color="#b996c8"/><stop offset="1" stop-color="#57478a"/></radialGradient>
<radialGradient id="bedSide" cx=".5" cy=".6" r=".75"><stop offset="0" stop-color="#d9c6f0"/><stop offset="1" stop-color="#7f68b4"/></radialGradient>
<linearGradient id="moonFill" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff0b0"/><stop offset="1" stop-color="#f2b44c"/></linearGradient>
<linearGradient id="cBackLit" x1="0" y1="400" x2="0" y2="540" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fdeadb"/><stop offset="1" stop-color="#eec3bb"/></linearGradient>
<linearGradient id="cBackSh" x1="0" y1="400" x2="0" y2="540" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#c9a6c8"/><stop offset="1" stop-color="#9c85b9"/></linearGradient>
<linearGradient id="cFrontLit" x1="0" y1="440" x2="0" y2="560" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff6ec"/><stop offset="1" stop-color="#f6d7cb"/></linearGradient>
<linearGradient id="cFrontSh" x1="0" y1="440" x2="0" y2="560" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#dcc2dc"/><stop offset="1" stop-color="#ae98c9"/></linearGradient>
<linearGradient id="streak" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<linearGradient id="rule" x1="0" x2="1"><stop offset="0" stop-color="#d8b05c" stop-opacity="0"/><stop offset=".25" stop-color="#d8b05c"/><stop offset=".75" stop-color="#d8b05c"/><stop offset="1" stop-color="#d8b05c" stop-opacity="0"/></linearGradient>
<filter id="blur6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="blur4" x="-20%" y="-200%" width="140%" height="500%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="blur2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2"/></filter>
<mask id="crescent"><circle cx="1112" cy="84" r="30" fill="#fff"/><circle cx="1125" cy="75" r="27" fill="#000"/></mask>
<clipPath id="roofClip"><path id="roofPath" d="M728 170C790 140 840 95 868 52C880 34 900 24 924 22C908 34 900 50 902 70C912 110 960 146 1032 170Q880 196 728 170Z"/></clipPath>
<clipPath id="roundWin"><circle cx="{CX}" cy="384" r="31"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect y="{Y0}" width="{W}" height="{VH}" fill="url(#sky)"/>''')

# ---------------------------------------------------------------- stars
o('<g fill="#fff6dc">')
n = 0
while n < 64:
    x, y = rng.uniform(10, W - 10), 10 + (rng.random() ** 1.6) * 330
    if math.hypot(x - 1112, y - 84) < 48: continue
    d = rng.uniform(2.5, 6.5)
    o(f'<circle class="tw" cx="{f(x)}" cy="{f(y)}" r="{f(rng.uniform(.6, 1.7))}" style="animation-duration:{f(d)}s;animation-delay:-{f(rng.uniform(0, d))}s"/>')
    n += 1
for x, y, s in [(612, 70, 6), (356, 38, 5), (1010, 150, 5.5), (1170, 190, 4.5), (520, 214, 4), (40, 250, 5), (700, 120, 4.5), (250, 22, 4)]:
    d = rng.uniform(3, 5.5)
    o(f'<g transform="translate({x} {y}) scale({s})"><path class="tw" fill="#f6dd98" d="{STAR4}" style="animation-duration:{f(d)}s;animation-delay:-{f(rng.uniform(0, d))}s"/></g>')
o('</g>')

# shooting star + crescent moon
o('<g transform="translate(420 34) rotate(18)"><g class="shoot"><rect x="-90" y="-1" width="90" height="2" rx="1" fill="url(#streak)"/><circle r="1.8" fill="#fff"/></g></g>')
o('<circle class="pulse" cx="1112" cy="84" r="74" fill="url(#moonHalo)"/>')
o('<rect x="1070" y="40" width="80" height="80" fill="#fff1cf" mask="url(#crescent)"/>')

# sky wisps
for x, y, s, op in [(120, 58, 1.1, .16), (590, 160, .9, .13), (1040, 262, 1.0, .12)]:
    o(f'<g transform="translate({x} {y}) scale({s} 1)" opacity="{op}" filter="url(#blur4)"><g class="wisp" style="animation-delay:-{f(rng.uniform(0, 16))}s">'
      '<ellipse cx="0" cy="0" rx="96" ry="4" fill="#f3e6ff"/><ellipse cx="40" cy="-5" rx="44" ry="3.5" fill="#f3e6ff"/><ellipse cx="-44" cy="5" rx="50" ry="3" fill="#f3e6ff"/></g></g>')

# ---------------------------------------------------------------- cloud sea
def cloud_layer(gid, rows, lit, sh, hi_op, og_rows=()):
    puffs = []
    for rows_, g in ((rows, rng), (og_rows if OG else (), random.Random(99))):   # OG rows use their own RNG so hero.svg stays identical
        for cy, rmin, rmax, jitter, step in rows_:
            x = g.uniform(0, step)
            while x < W:
                r = g.uniform(rmin, rmax)
                puffs.append((x, cy + g.uniform(-jitter, jitter), r))
                x += step * g.uniform(.75, 1.2)
    wrapped = list(puffs)
    for x, y, r in puffs:                     # make the tile seamless
        if x < r + 8: wrapped.append((x + W, y, r))
        if x > W - r - 8: wrapped.append((x - W, y, r))
    o(f'<g id="{gid}">')
    o(f'<g fill="url(#{sh})">' + "".join(f'<circle cx="{f(x + 5)}" cy="{f(y + 7)}" r="{f(r)}"/>' for x, y, r in wrapped) + '</g>')
    o(f'<g fill="url(#{lit})">' + "".join(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * .95)}"/>' for x, y, r in wrapped) + '</g>')
    o('</g>')

o('<g class="drift1">')
cloud_layer("cb", [(480, 42, 62, 9, 78), (528, 52, 70, 6, 90)], "cBackLit", "cBackSh", .45)
o(f'<use href="#cb" xlink:href="#cb" x="{W}"/></g>')

# ---------------------------------------------------------------- floating tower
o('<g class="float">')
o(f'<circle class="pulse" cx="{CX}" cy="290" r="290" fill="url(#halo)" style="animation-duration:7s"/>')

BROOM = ('<g class="wob">'
         '<path d="M-31-5C-41-9-53-11-62-10L-59-4-64 0-59 4-62 10C-53 11-41 9-31 5Z" fill="#e6b95f"/>'
         '<path d="M-33-3-58-6M-33 0-61 0M-33 3-58 6" stroke="#b58434" stroke-width="1.1" fill="none"/>'
         '<line x1="-34" y1="0" x2="30" y2="0" stroke="#7a4b2e" stroke-width="3.4" stroke-linecap="round"/>'
         '<rect x="-35" y="-6" width="6" height="12" rx="1.5" fill="#9a4b2c"/>'
         '<path d="M12-1.5 9-7M12-1.5 15-7" stroke="#b9a3dd" stroke-width="2" stroke-linecap="round"/>'
         '<line x1="26" y1="1" x2="26" y2="8" stroke="#d8b05c" stroke-width="1"/>'
         f'<g transform="translate(26 11) scale(3.4)"><path d="{STAR4}" fill="#f6dd98"/></g></g>')

def broom_copy(layer):
    mirror = ' transform="scale(-1 1)"' if layer == "back" else ""
    parts = [(0, BROOM)]
    for lag, s, op in [(.22, 4.2, .9), (.46, 3.2, .7), (.72, 2.4, .5), (.98, 1.8, .35)]:
        parts.append((lag, f'<g transform="translate(-64 {f(rng.uniform(-3, 3))}) scale({s})" opacity="{op}"><path d="{STAR4}" fill="#fff3c4"/></g>'))
    o(f'<g transform="translate({CX} 268)">')
    for lag, body in parts:
        o(f'<g class="{layer}" style="animation-delay:{f(lag - 12)}s"><g class="bx" style="animation-delay:{f(lag - 12)}s">'
          f'<g class="by" style="animation-delay:{f(lag - 15)}s"><g{mirror}>{body}</g></g></g></g>')
    o('</g>')

broom_copy("back")

# base drum under the bedroom
o(f'<path d="M762 440C762 482 820 510 {CX} 512C940 510 998 482 998 440Q{CX} 458 762 440Z" fill="url(#base)"/>')
o(f'<path d="M{CX - 6} 510l6 16 6-16z" fill="#d8b05c"/>')
# wall
o(f'<path d="M762 176V446Q{CX} 462 998 446V176Z" fill="url(#wall)"/>')
# brick marks
holes = [(832, 204, 928, 318), (776, 220, 810, 298), (950, 220, 984, 298), (838, 342, 922, 426), (776, 346, 810, 424), (950, 346, 984, 424)]
marks = []
while len(marks) < 26:
    x, y = rng.uniform(770, 980), rng.uniform(204, 436)
    if 306 < y < 340 or any(a - 6 < x < c + 6 and b - 6 < y < d + 6 for a, b, c, d in holes): continue
    marks.append((x, y))
o('<g stroke="#caa97f" stroke-width="1.6" stroke-linecap="round" opacity=".55" fill="none">'
  + "".join(f'<path d="M{f(x)} {f(y)}h{f(rng.uniform(9, 16))}m-{f(rng.uniform(4, 9))} 6h{f(rng.uniform(8, 14))}"/>' for x, y in marks) + '</g>')
# shading bands
o(f'<path d="M762 184Q{CX} 202 998 184" stroke="#4b2f1f" stroke-width="6" fill="none"/>')
o(f'<path d="M762 318Q{CX} 336 998 318" stroke="#4b2f1f" stroke-width="9" fill="none"/>')
o(f'<path d="M762 312Q{CX} 330 998 312" stroke="#d8b05c" stroke-width="2" fill="none"/>')
o(f'<path d="M762 440Q{CX} 458 998 440" stroke="#d8b05c" stroke-width="5" fill="none"/>')
o(f'<path d="M762 446Q{CX} 464 998 446" stroke="#4b2f1f" stroke-width="3" fill="none" opacity=".6"/>')

# window light spill on the wall
o(f'<g opacity=".32"><ellipse class="pulse" cx="{CX}" cy="262" rx="78" ry="70" fill="#ffd98a" filter="url(#blur6)" style="animation-duration:4.5s"/></g>')
o(f'<g opacity=".24"><ellipse class="pulse" cx="{CX}" cy="386" rx="56" ry="50" fill="#ffd98a" filter="url(#blur6)" style="animation-duration:6s"/></g>')

# --- study: main arched window
o(f'<path d="M838 300V246A42 42 0 0 1 922 246V300Z" fill="#5a3a26"/>')
o(f'<path d="M845 298V246A35 35 0 0 1 915 246V298Z" fill="url(#study)"/>')
books = []
for shelf in (268, 284, 298):
    x = 848.5
    while x < 869:
        w, h = rng.uniform(2.2, 3.8), rng.uniform(8, 12.5)
        lean = rng.random() < .15
        books.append(f'<rect x="{f(x)}" y="{f(shelf - h)}" width="{f(w)}" height="{f(h)}" rx=".4" fill="{rng.choice(["#9a4b2c", "#b86a35", "#6d5a9c", "#3f6d8c", "#8a5a2c"])}"'
                     + (f' transform="rotate(-12 {f(x + w)} {shelf})"' if lean else '') + '/>')
        x += w + rng.uniform(.3, 1.2)
o('<g opacity=".55">' + "".join(books) + '<path d="M848 268.5h23M848 284.5h23" stroke="#7a3f1c" stroke-width="1.6"/></g>')
o('<path d="M898 298v-6h10v6zM903 292l-6-14 3-1 6 14zM896 278l8-5 4 6-8 5z" fill="#9a5226" opacity=".5"/>')
o('<circle class="pulse" cx="903" cy="281" r="9" fill="#fff8d8" opacity=".8" filter="url(#blur2)" style="animation-duration:3.2s"/>')
o(f'<g stroke="#5a3a26" stroke-width="3.4" fill="none"><path d="M{CX} 211V298M845 246H915M863 246A17 17 0 0 1 897 246"/></g>')
o('<rect x="832" y="297" width="96" height="7" rx="2" fill="#6b4630"/>')
# flower box
o('<rect x="836" y="305" width="88" height="12" rx="2" fill="#7a4b2e"/><rect x="836" y="305" width="88" height="3" fill="#8f5d3b"/>')
flowers = []
for i in range(30):
    x = rng.uniform(839, 921)
    flowers.append(f'<circle cx="{f(x)}" cy="{f(rng.uniform(299, 306))}" r="{f(rng.uniform(2.2, 3.8))}" fill="{rng.choice(["#6f9a5a", "#7ea866"])}"/>')
for i in range(26):
    x = rng.uniform(840, 920)
    flowers.append(f'<circle cx="{f(x)}" cy="{f(rng.uniform(297, 304))}" r="{f(rng.uniform(1.6, 2.6))}" fill="{rng.choice(["#f3a7b8", "#f7c9d4", "#fff0f3", "#c7a4de", "#f3a7b8"])}"/>')
for x0 in (840, 846, 916):
    for k in range(5):
        flowers.append(f'<circle cx="{f(x0 + rng.uniform(-2, 2))}" cy="{f(312 + k * 4.2)}" r="{f(2.3 - k * .25)}" fill="{"#6f9a5a" if k % 2 else "#f7c9d4"}"/>')
o("<g>" + "".join(flowers) + "</g>")

# --- study side windows (narrower: they sit on the curve)
def side_window(x0, x1, top, sill, fill, curtain_left):
    r = (x1 - x0) / 2; cx = (x0 + x1) / 2; ri = r - 4
    o(f'<path d="M{x0} {sill}V{top}A{f(r)} {f(r)} 0 0 1 {x1} {top}V{sill}Z" fill="#5a3a26"/>')
    o(f'<path d="M{x0 + 4} {sill - 2}V{top}A{f(ri)} {f(ri)} 0 0 1 {x1 - 4} {top}V{sill - 2}Z" fill="url(#{fill})"/>')
    cx0 = x0 + 4 if curtain_left else x1 - 4
    dx = 1 if curtain_left else -1
    o(f'<path d="M{cx0} {top - ri + 3}Q{f(cx0 + dx * 9)} {top + 18} {f(cx0 + dx * 4)} {sill - 2}H{cx0}Z" fill="#f2e9dc" opacity=".92"/>')
    o(f'<path d="M{f(cx)} {top - ri}V{sill - 2}M{x0 + 4} {top + 18}H{x1 - 4}" stroke="#5a3a26" stroke-width="2" fill="none"/>')
    o(f'<rect x="{x0 - 4}" y="{sill}" width="{x1 - x0 + 8}" height="5" rx="1.5" fill="#6b4630"/>')

side_window(780, 806, 238, 294, "studySide", True)
side_window(954, 980, 238, 294, "studySide", False)

# --- bedroom: round window with the moon lamp
o(f'<circle cx="{CX}" cy="384" r="39" fill="#5a3a26"/><circle cx="{CX}" cy="384" r="31" fill="url(#bedroom)"/>')
o('<g clip-path="url(#roundWin)">')
MC = dict(T=(.02, 1.82), P1=(-.95, 1.4), P2=(-.45, -.42), S=(1.05, .52), Q1=(.25, .22), Q2=(-.45, .85))
P = {k: (872 + x * 22, 402 - y * 22) for k, (x, y) in MC.items()}
pt = lambda k: f"{f(P[k][0])} {f(P[k][1])}"
moon_d = f"M{pt('T')}C{pt('P1')} {pt('P2')} {pt('S')}C{pt('Q1')} {pt('Q2')} {pt('T')}Z"
o(f'<path class="pulse" d="{moon_d}" fill="#ffd36e" filter="url(#blur6)" style="animation-duration:3.6s"/>')
o(f'<path d="{moon_d}" fill="url(#moonFill)" stroke="#e6a33e" stroke-width=".8"/>')
seat = min((bez(P["S"], P["Q1"], P["Q2"], P["T"], i / 60) for i in range(61)), key=lambda p: -p[1])
o('<g fill="#f7f3fd">' + "".join(f'<circle cx="{f(seat[0] + dx)}" cy="{f(seat[1] - 2 + dy)}" r="{r}"/>' for dx, dy, r in [(-5, 0, 3.4), (0, -1.5, 3.8), (5, 0, 3.2)]) + '</g>')
o('<g fill="#f4f1fb">' + "".join(f'<ellipse cx="{f(CX + dx)}" cy="{f(410 + dy)}" rx="{rx}" ry="{f(rx * .45)}"/>' for dx, dy, rx in [(-22, 1, 9), (-11, -1, 11), (2, 0, 12), (15, -1, 10), (26, 1, 8)]) + '</g>')
for x, y, s in [(900, 364, 3.2), (866, 358, 2.6), (908, 382, 2.2), (889, 372, 1.8)]:
    o(f'<g transform="translate({x} {y}) scale({s})"><path class="tw" d="{STAR4}" fill="#fff3c4" style="animation-duration:{f(rng.uniform(2, 3.5))}s;animation-delay:-{f(rng.uniform(0, 3))}s"/></g>')
o(f'<path d="M849 350C858 368 851 392 855 420H846V350Z" fill="#efe6da"/><path d="M911 350C902 368 909 392 905 420H914V350Z" fill="#efe6da"/>')
o('<path d="M851 360C853 376 850 394 852 416M909 360C907 376 910 394 908 416" stroke="#d6c8b6" stroke-width="1" fill="none"/>')
o('<rect x="846" y="386" width="10" height="3" rx="1" fill="#b9a3dd"/><rect x="904" y="386" width="10" height="3" rx="1" fill="#b9a3dd"/>')
o('</g>')
o(f'<circle cx="{CX}" cy="384" r="32" fill="none" stroke="#d8b05c" stroke-width="2"/>')
side_window(780, 806, 366, 422, "bedSide", True)
side_window(954, 980, 366, 422, "bedSide", False)

# --- ivy (leaf colours follow the seasons)
vines = [
    [((770, 318), (778, 295), (758, 262), (768, 238)), ((768, 238), (776, 214), (800, 204), (828, 198))],
    [((992, 192), (1000, 214), (984, 236), (994, 262))],
    [((958, 194), (952, 206), (946, 214), (942, 228))],
    [((766, 452), (770, 430), (760, 410), (768, 384))],
    [((996, 452), (990, 430), (1000, 404), (992, 378))],
]
leaves, stems = [], []
for vine in vines:
    d = f"M{vine[0][0][0]} {vine[0][0][1]}" + "".join(f"C{s[1][0]} {s[1][1]} {s[2][0]} {s[2][1]} {s[3][0]} {s[3][1]}" for s in vine)
    stems.append(f'<path d="{d}"/>')
    side = 1
    for seg in vine:
        for i in range(1, 9):
            t = i / 9
            x, y = bez(*seg, t)
            x2, y2 = bez(*seg, min(1, t + .02))
            ang = math.degrees(math.atan2(y2 - y, x2 - x))
            nx, ny = -(y2 - y), (x2 - x); ln = math.hypot(nx, ny) or 1
            px, py = x + side * 4 * nx / ln, y + side * 4 * ny / ln
            cls = rng.choice(["ia", "ib"])
            leaves.append(f'<path class="{cls}" transform="translate({f(px)} {f(py)}) rotate({f(ang + side * 55)}) scale({f(rng.uniform(.9, 1.3))})" d="M0-4.5C3.2-2.5 3.2 2.5 0 4.5-3.2 2.5-3.2-2.5 0-4.5z"/>')
            side = -side
o('<g stroke="#5d6b3e" stroke-width="1.5" fill="none">' + "".join(stems) + '</g>')
o("<g>" + "".join(leaves) + "</g>")

# --- black cat on the right study sill
o('<g fill="#1d1622">'
  '<path d="M959 294C957 284 961 276 967 276C973 276 977 284 975 294Z"/>'
  '<circle cx="967" cy="273" r="7"/><path d="M961 270l-1-8 5 4zM973 270l1-8-5 4z"/>'
  '<g transform="translate(975 291)"><g class="tail"><path d="M0 0C8 2 11 11 8 20C6 26 9 30 13 28" stroke="#1d1622" stroke-width="3.2" stroke-linecap="round" fill="none"/></g></g></g>')
for ex in (964.2, 969.8):
    o(f'<g transform="translate({ex} 272.5)"><g class="blink"><ellipse rx="1.5" ry="1.9" fill="#f6dd98"/></g></g>')

# --- roof
o('<path d="M728 170C790 140 840 95 868 52C880 34 900 24 924 22C908 34 900 50 902 70C912 110 960 146 1032 170Q880 196 728 170Z" fill="url(#roof)"/>')
sc = []
for y0, xl, xr in [(154, 752, 996), (132, 786, 958), (110, 812, 934), (88, 836, 914), (66, 856, 904)]:
    x = xl
    while x < xr:
        dip = 9 * (1 - ((x - CX) / 150) ** 2) * (y0 / 154)
        sc.append(f"M{f(x)} {f(y0 + dip)}a8 7 0 0 0 16 0")
        x += 16
o(f'<g clip-path="url(#roofClip)"><path d="{"".join(sc)}" stroke="#1d2350" stroke-width="1.4" fill="none" opacity=".5"/>'
  '<path d="M760 150C810 120 846 80 872 48" stroke="#8b95d0" stroke-width="5" opacity=".25" fill="none" stroke-linecap="round"/></g>')
o('<path d="M728 170Q880 196 1032 170" stroke="#d8b05c" stroke-width="4" fill="none"/>')
o('<circle cx="872" cy="124" r="10" fill="#4b2f1f"/><circle class="pulse" cx="872" cy="124" r="7" fill="#ffd98a" style="animation-duration:4s"/><path d="M865 124h14M872 117v14" stroke="#4b2f1f" stroke-width="1.6"/>')
o('<circle class="pulse" cx="924" cy="22" r="16" fill="#ffe7a0" opacity=".5" filter="url(#blur6)"/>')
o(f'<g transform="translate(924 22)"><g class="spin"><path d="{STAR4}" transform="scale(10)" fill="#f6dd98"/><path d="{STAR4}" transform="rotate(45) scale(6)" fill="#fff4cc"/></g></g>')

# --- winter only: snow on eaves, sills and ledges, plus icicles
snow = []
snow.append('<path d="M731 166Q880 191 1029 166" stroke="#fbfdff" stroke-width="9" stroke-linecap="round" fill="none"/>')
for i in range(1, 44):
    x, y = quad((731, 169), (880, 195), (1029, 169), i / 44)
    snow.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rng.uniform(3.5, 6))}" ry="{f(rng.uniform(2.2, 3.6))}"/>')
for i in range(3, 21, 2):
    x, y = quad((730, 170), (880, 196), (1030, 170), i / 22)
    snow.append(f'<path d="M{f(x - 2.2)} {f(y + 2)}L{f(x)} {f(y + rng.uniform(8, 14))}L{f(x + 2.2)} {f(y + 2)}Z" fill="#e3f0fa"/>')
for x, y, w in [(832, 294, 96), (836, 301, 88), (776, 291, 34), (950, 291, 34), (776, 419, 34), (950, 419, 34)]:
    snow.append(f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2.5"/>')
snow.append(f'<path d="M762 309Q{CX} 327 998 309" stroke="#fbfdff" stroke-width="4" fill="none" stroke-linecap="round"/>')
snow.append(f'<path d="M762 436Q{CX} 454 998 436" stroke="#fbfdff" stroke-width="4" fill="none" stroke-linecap="round"/>')
o('<g class="season wi" fill="#fbfdff">' + "".join(snow) + '</g>')

# --- levitating books
for x, y, col, rot, d in [(700, 186, "#9a4b2c", -14, 4.6), (672, 224, "#3f6d8c", 10, 5.4), (724, 238, "#6d5a9c", -6, 3.9)]:
    o(f'<g transform="translate({x} {y}) rotate({rot})"><g class="bob" style="animation-duration:{d}s;animation-delay:-{f(rng.uniform(0, d))}s">'
      f'<rect x="-11" y="-7.5" width="22" height="15" rx="1.8" fill="{col}"/><rect x="-8.5" y="-6" width="18.5" height="12" fill="#f7ecd6"/>'
      f'<rect x="-11" y="-7.5" width="19" height="15" rx="1.8" fill="{col}"/><rect x="-9.5" y="-3" width="3" height="6" fill="#d8b05c"/>'
      f'<g transform="translate(14 -10) scale(3)"><path class="tw" d="{STAR4}" fill="#fff3c4" style="animation-duration:2.4s"/></g></g></g>')

broom_copy("front")
o('</g>')   # /float

# ---------------------------------------------------------------- seasonal particles
PETAL = "M0-4C3-3 3 2 0 4-3 2-3-3 0-4z"
LEAF = "M0-6C4-3 4 3 0 6-4 3-4-3 0-6z"

def fallers(cls, n, shape, colors, dur, spin, scale=(0.9, 1.4)):
    o(f'<g class="season {cls}">')
    for _ in range(n):
        x = rng.uniform(560, 1190)
        d = rng.uniform(*dur)
        body = shape(rng.choice(colors), rng.uniform(*scale))
        rot = (f'<g class="roll" style="animation-duration:{f(rng.uniform(3, 7))}s;animation-direction:{rng.choice(["normal", "reverse"])}">{body}</g>'
               if spin else body)
        o(f'<g transform="translate({f(x)} 0)"><g class="fall" style="animation-duration:{f(d)}s;animation-delay:-{f(rng.uniform(0, d))}s">'
          f'<g class="sway" style="animation-duration:{f(rng.uniform(1.8, 3.4))}s;animation-delay:-{f(rng.uniform(0, 3))}s">{rot}</g></g></g>')
    o('</g>')

fallers("sp", 16, lambda c, s: f'<path d="{PETAL}" transform="scale({f(s)})" fill="{c}"/>', ["#f7b6c8", "#fbd3de", "#fff0f4", "#f3a0b6"], (8, 12), True)
o('<g class="season su">')
for _ in range(18):
    x, y, d = rng.uniform(600, 1180), rng.uniform(150, 470), rng.uniform(5, 9)
    o(f'<g transform="translate({f(x)} {f(y)})"><g class="ffly" style="animation-duration:{f(d)}s;animation-delay:-{f(rng.uniform(0, d))}s">'
      '<circle r="5.5" fill="#fff6a8" opacity=".28"/><circle r="1.8" fill="#fffbd6"/></g></g>')
o('</g>')
fallers("au", 16, lambda c, s: f'<g transform="scale({f(s)})"><path d="{LEAF}" fill="{c}"/><path d="M0-5V5" stroke="#8a3c1c" stroke-width=".6"/></g>',
        ["#d9642f", "#e9a03b", "#b8432a", "#f0b957"], (7, 10), True, (1, 1.5))
fallers("wi", 30, lambda c, s: f'<circle r="{f(s)}" fill="{c}"/>', ["#ffffff", "#f3f7ff", "#e8f0ff"], (10, 16), False, (1.3, 3))

# front cloud layer (drawn over the tower foot)
o('<g class="drift2">')
cloud_layer("cf", [(502, 30, 48, 8, 62), (548, 44, 60, 5, 76)], "cFrontLit", "cFrontSh", .6, og_rows=[(590, 44, 58, 4, 60)])
o(f'<use href="#cf" xlink:href="#cf" x="{W}"/></g>')

# ---------------------------------------------------------------- title block
TX = 80
o(f'<rect y="{Y0}" width="{W}" height="{VH}" fill="url(#vig)"/>')
o(f'<g transform="translate({TX} 112)">'
  f'<g transform="translate(5 -4.5) scale(5)"><path d="{STAR4}" fill="#d8b05c"/></g>'
  '<text class="en" x="18" y="0" font-size="13.5" font-weight="600" letter-spacing="3.4" fill="#d8b05c">A SINGLE-FILE THREE.JS FAIRYTALE</text></g>')
o(f'<text class="zh" x="{TX + 2}" y="199" font-size="70" font-weight="700" letter-spacing="12" fill="#0b1026" opacity=".5">塔楼书房</text>')
o(f'<text class="zh" x="{TX}" y="196" font-size="70" font-weight="700" letter-spacing="12" fill="#f7ecd6">塔楼书房</text>')
o(f'<text class="en" x="{TX + 2}" y="244" font-size="38" font-style="italic" font-weight="600" fill="#f6dd98">The Tower Study</text>')
o(f'<rect x="{TX}" y="266" width="170" height="1.4" fill="url(#rule)"/><rect x="{TX + 212}" y="266" width="170" height="1.4" fill="url(#rule)"/>'
  f'<g transform="translate({TX + 191} 267)"><circle r="8" fill="#d8b05c"/><circle cx="3.6" cy="-3" r="7" fill="#262458"/>'
  f'<g transform="translate(-14 0) scale(3)"><path d="{STAR4}" fill="#d8b05c"/></g><g transform="translate(16 0) scale(3)"><path d="{STAR4}" fill="#d8b05c"/></g></g>')
o(f'<text class="zh" x="{TX + 2}" y="303" font-size="18" letter-spacing="2.5" fill="#f7ecd6" opacity=".9">两层楼 · 四季流转 · 十八个小发现</text>')
o(f'<text class="en" x="{TX + 2}" y="330" font-size="18" font-style="italic" fill="#f7ecd6" opacity=".78">Two floors · Four seasons · Eighteen little discoveries</text>')

# season switcher, echoing the page's own 春 夏 秋 冬 tabs
SY = 356
o(f'<g transform="translate({TX} {SY})">'
  '<rect width="290" height="48" rx="24" fill="#f4e9d2" stroke="#d8b05c" stroke-width="1.5"/>'
  '<g class="pill"><rect x="5" y="5" width="70" height="38" rx="19" fill="#4b2f1f"/></g>')
for i, (zh, en, cls) in enumerate([("春", "SPRING", "sp"), ("夏", "SUMMER", "su"), ("秋", "AUTUMN", "au"), ("冬", "WINTER", "wi")]):
    cx = 40 + i * 70
    for fill, extra in [("#3a2a1f", ""), ("#f6dd98", f' class="season {cls}"')]:
        o(f'<g{extra}><text class="zh" x="{cx}" y="25" font-size="17" text-anchor="middle" fill="{fill}">{zh}</text>'
          f'<text class="en" x="{cx}" y="37.5" font-size="8.5" font-weight="600" letter-spacing="1.6" text-anchor="middle" fill="{fill}">{en}</text></g>')
o('</g>')

o('</g>' if OG else f'</g><rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="23.5" fill="none" stroke="#d8b05c" stroke-opacity=".45" stroke-width="1.5"/>')
o('</svg>')

svg = "\n".join(out)
args = [a for a in sys.argv[1:] if a != "--og"]
dest = args[0] if args else os.path.join(os.path.dirname(os.path.abspath(__file__)), "og.svg" if OG else "hero.svg")
open(dest, "w", encoding="utf-8").write(svg)
print(len(svg.encode()), "bytes")
