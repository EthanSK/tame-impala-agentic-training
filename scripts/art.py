#!/usr/bin/env python3
"""Deterministic original SVG illustration for the site.

Every drawing is an abstraction of one Tame Impala album cover; the mapping and
credits are in ART_DIRECTION.md. Nothing is traced or copied from the artwork.
Each piece is generated from a handful of parameters with a fixed random seed so
that `python3 scripts/build.py` produces byte-identical output every run.
"""
import math, random

AUTUMN = ['#c9441f', '#e0602a', '#ef8a34', '#f3b04a', '#8e2c14', '#d6a44a', '#b8401c']
GREENS = ['#2d6b3c', '#3e7f3a', '#1f4d30', '#5d8f3a', '#27593a']


def n1(v):
    s = f'{v:.1f}'
    s = s[:-2] if s.endswith('.0') else s
    return '0' if s == '-0' else s


def n3(v):
    s = f'{v:.3f}'.rstrip('0').rstrip('.')
    return s or '0'


def mix(a, b, t):
    """Linear blend of two hex colours."""
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(round(x + (y - x) * t) for x, y in zip(ca, cb))


def innerspeaker():
    """Hero cover: turquoise sky, a cloud row repeated into a receding V, dark ridge, autumn foliage at the edges."""
    rng = random.Random(2010)
    H = 560  # horizon
    o = []
    a = o.append
    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">')
    a('<defs>'
      '<linearGradient id="is-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b8fa3"/><stop offset=".6" stop-color="#22b5bc"/><stop offset="1" stop-color="#a8e6d8"/></linearGradient>'
      '<linearGradient id="is-ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f8a67"/><stop offset=".45" stop-color="#1c5c43"/><stop offset="1" stop-color="#0d2e20"/></linearGradient>'
      '<linearGradient id="is-valley" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fe0ac" stop-opacity=".95"/><stop offset="1" stop-color="#3f9a63" stop-opacity="0"/></linearGradient>'
      '<radialGradient id="is-vig" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#03202a" stop-opacity="0"/><stop offset="1" stop-color="#03202a" stop-opacity=".5"/></radialGradient>'
      '<filter id="is-soft" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur stdDeviation="14"/></filter>'
      '<filter id="is-puff" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="2.5"/></filter>'
      '<filter id="is-leaf" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency=".04" numOctaves="3" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="38" xChannelSelector="R" yChannelSelector="G"/></filter>'
      '<filter id="is-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .28 0"/></filter>')
    # One cloud row, reused at every depth of the recursion.
    a('<g id="is-row" filter="url(#is-puff)">')
    x = -470.0
    while x < 470:
        rx = rng.uniform(34, 70)
        ry = rng.uniform(13, 24)
        a(f'<ellipse cx="{n1(x + rx)}" cy="{n1(rng.uniform(-6, 6))}" rx="{n1(rx)}" ry="{n1(ry)}" fill="#f7f2dc" opacity="{n1(rng.uniform(.75, .95))}"/>')
        x += rx * 1.35
    a('</g></defs>')
    a('<rect width="1000" height="1000" fill="url(#is-sky)"/>')
    a('<g filter="url(#is-soft)" fill="#f9f4e0">')
    for cx, cy, rx, ry, op in [(180, 250, 170, 62, .85), (470, 205, 230, 80, .9), (760, 260, 190, 66, .85), (330, 330, 150, 44, .7), (640, 330, 160, 46, .7)]:
        a(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" opacity="{op}"/>')
    a('</g>')
    for i in range(12):
        s = 0.8 ** i
        y = H - 420 * s
        flip = -1 if i % 2 else 1
        a(f'<use href="#is-row" transform="translate(500 {n1(y)}) scale({n3(s)} {n3(s * flip)})" opacity="{n3(max(.35, .95 - .045 * i))}"/>')
    a(f'<rect y="{H}" width="1000" height="440" fill="url(#is-ground)"/>')
    a(f'<path d="M500 {H}L120 1000H880Z" fill="url(#is-valley)"/>')
    a(f'<path d="M0 {H - 40}C120 {H - 70} 230 {H + 10} 330 {H + 18}C400 {H + 24} 460 {H + 8} 500 {H + 6}C540 {H + 8} 600 {H + 24} 670 {H + 18}C770 {H + 10} 880 {H - 70} 1000 {H - 40}V{H + 90}H0Z" fill="#165047"/>')
    # Forest floor: greens in the middle, autumn colour towards the edges.
    a('<g filter="url(#is-leaf)">')
    for _ in range(110):
        cx = rng.uniform(-20, 1020)
        cy = 1000 - 260 * rng.random() ** 1.4
        r = rng.uniform(22, 66)
        edge = min(cx, 1000 - cx) / 1000
        autumn = rng.random() < (0.72 if edge < .18 else 0.3)
        col = rng.choice(AUTUMN if autumn else GREENS)
        a(f'<circle cx="{n1(cx)}" cy="{n1(cy)}" r="{n1(r)}" fill="{col}" opacity="{n1(rng.uniform(.85, 1))}"/>')
    a('</g>')
    # Autumn trees hugging both edges.
    for side in (0, 1):
        a('<g filter="url(#is-leaf)">')
        for _ in range(70):
            off = 250 * rng.random() ** 1.7
            cx = off - 30 if side == 0 else 1030 - off
            cy = rng.uniform(-30, 740)
            r = rng.uniform(18, 62) * (1 - off / 420) + 10
            a(f'<circle cx="{n1(cx)}" cy="{n1(cy)}" r="{n1(r)}" fill="{rng.choice(AUTUMN)}" opacity="{n1(rng.uniform(.88, 1))}"/>')
        a('</g>')
    a('<rect width="1000" height="1000" fill="url(#is-vig)"/>')
    a('<rect width="1000" height="1000" filter="url(#is-grain)" opacity=".55"/>')
    a('</svg>')
    return ''.join(o)


def vinyl():
    """A black record with an orange label, sliding out of the sleeve."""
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" aria-hidden="true" focusable="false">',
         '<defs><radialGradient id="vn-sheen" cx=".3" cy=".25" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".5" stop-color="#fff" stop-opacity=".04"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>',
         '<circle cx="200" cy="200" r="198" fill="#0d0d10"/>']
    for r in range(78, 196, 4):
        o.append(f'<circle cx="200" cy="200" r="{r}" fill="none" stroke="#1d1d22" stroke-width="1.2"/>')
    o += ['<circle cx="200" cy="200" r="198" fill="url(#vn-sheen)"/>',
          '<circle cx="200" cy="200" r="66" fill="#f7931e"/>',
          '<circle cx="200" cy="200" r="60" fill="none" stroke="#c9741a" stroke-width=".8" opacity=".7"/>',
          '<circle cx="200" cy="200" r="4" fill="#0d0d10"/>',
          '</svg>']
    return ''.join(o)


def currents():
    """Agent section background: violet streamlines bending around a chrome sphere, with one red-to-orange streak."""
    W, H = 1200, 600
    cx, cy, R = 900, 300, 86
    Re = R + 26
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMaxYMid slice">')
    a('<defs>'
      '<radialGradient id="cu-glow" cx=".8" cy=".08" r=".8"><stop offset="0" stop-color="#5a3d8f" stop-opacity=".75"/><stop offset="1" stop-color="#0c0813" stop-opacity="0"/></radialGradient>'
      '<radialGradient id="cu-chrome" cx=".36" cy=".3" r=".75"><stop offset="0" stop-color="#fff"/><stop offset=".22" stop-color="#d9d9e0"/><stop offset=".55" stop-color="#6d6c78"/><stop offset=".85" stop-color="#1b1a22"/><stop offset="1" stop-color="#3a3944"/></radialGradient>'
      '<linearGradient id="cu-streak" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8302c"/><stop offset=".6" stop-color="#f0552c"/><stop offset="1" stop-color="#f9b120"/></linearGradient>'
      '</defs>')
    a(f'<rect width="{W}" height="{H}" fill="#0c0813"/><rect width="{W}" height="{H}" fill="url(#cu-glow)"/>')

    def warp(x, y, row):
        dx, dy = x - cx, y - cy
        d = math.hypot(dx, dy)
        near = math.exp(-(d / 240) ** 2)
        behind = 1 / (1 + math.exp(-(x - cx) / 50)) * math.exp(-max(0.0, x - cx) / 380) * math.exp(-((y - cy) / 150) ** 2)
        # A smooth displacement keeps each streamline on its side of the orb.
        # The earlier hard circle boundary produced sharp corners and crossings.
        side = 1 if dy >= 0 else -1
        clearance = Re * Re * math.exp(-(dx / (Re * 1.2)) ** 2)
        return cy + side * math.sqrt(dy * dy + clearance) + (8 * near + 12 * behind) * math.sin(x / 42 + row * .25)

    def path(fn, row):
        pts = []
        x = 0.0
        while x <= W:
            pts.append((x, warp(x, fn(x), row)))
            x += 8 if abs(x - cx) < Re + 140 else 40
        if pts[-1][0] < W:
            pts.append((W, warp(W, fn(W), row)))
        d = f'M0 {n1(pts[0][1])}'
        for i in range(len(pts) - 1):
            p0, p1 = pts[max(0, i - 1)], pts[i]
            p2, p3 = pts[i + 1], pts[min(len(pts) - 1, i + 2)]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f'C{n1(c1[0])} {n1(c1[1])} {n1(c2[0])} {n1(c2[1])} {n1(p2[0])} {n1(p2[1])}'
        return d

    for row, y0 in enumerate(range(6, H, 16)):
        t = math.exp(-((y0 - cy) / 240) ** 2)
        d = path(lambda x, y0=y0: y0, row)
        a(f'<path d="{d}" fill="none" stroke="{mix("#5a4a8a", "#d3c3f5", t)}" stroke-width="1.5" opacity=".9"/>')
    k = (cy + R + 10 - 30) / (cx + 20)
    d = path(lambda x: 30 + (x + 20) * k, 0)
    a(f'<path d="{d}" fill="none" stroke="url(#cu-streak)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    a(f'<ellipse cx="{cx}" cy="{cy + R - 8}" rx="{R * .95:.0f}" ry="16" fill="#000" opacity=".45"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#cu-chrome)"/>')
    a(f'<ellipse cx="{cx - 28}" cy="{cy - 36}" rx="22" ry="12" fill="#fff" opacity=".55"/>')
    a('</svg>')
    return ''.join(o)


# Sources section and 404: an arched window opening onto turquoise sky, sand rising through the lower panes.
ARCH = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" aria-hidden="true" focusable="false">'
        '<defs><linearGradient id="sr-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2fb3c1"/><stop offset="1" stop-color="#d7f0f1"/></linearGradient>'
        '<linearGradient id="sr-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ecc59a"/><stop offset="1" stop-color="#c48a57"/></linearGradient>'
        '<clipPath id="sr-clip"><path d="M34 300V112a66 66 0 0 1 132 0v188Z"/></clipPath></defs>'
        '<path d="M22 300V112a78 78 0 0 1 156 0v188Z" fill="#f2b59b"/>'
        '<path d="M34 300V112a66 66 0 0 1 132 0v188Z" fill="url(#sr-sky)"/>'
        '<g clip-path="url(#sr-clip)"><g fill="#fff" opacity=".85"><ellipse cx="82" cy="128" rx="34" ry="10"/><ellipse cx="128" cy="168" rx="28" ry="8"/><ellipse cx="70" cy="196" rx="24" ry="7"/></g>'
        '<path d="M78 46V300M122 46V300M34 150h132M34 214h132" stroke="#f7d3c2" stroke-width="3"/>'
        '<path d="M0 300C40 252 92 268 122 242c30-26 54-14 78-24v82Z" fill="url(#sr-sand)"/></g></svg>')

# Sand rising to meet the source shelf. Colour comes from CSS via currentColor.
DUNE = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 96" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
        '<path d="M0 96V64C160 22 300 74 470 44 620 18 740 66 940 38 1100 16 1260 58 1440 30V96Z" fill="currentColor"/>'
        '<path d="M0 96V80C200 52 330 88 520 66 690 46 820 86 1010 62 1180 42 1300 74 1440 56V96Z" fill="#000" opacity=".07"/></svg>')
