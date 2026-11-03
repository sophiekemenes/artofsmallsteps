# Builds the final logo SVGs (text outlined) for Art of Small Steps (S2) and RECHART (W2).
# python -I brand_logo.py <scratchpad> <outdir>
import sys, os, json, math, subprocess

SP, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
INK, SEA, COP, DCOP, PAPER = '#142230', '#1C4F6B', '#B87345', '#8A5129', '#FBF1E3'
COP_ON_DARK = '#E0A67C'
PHI = (1 + 5 ** .5) / 2
B = math.log(PHI) / (math.pi / 2)

# ---------- outlined text ----------
CORM, LORA = os.path.join(SP, 'fonts', 'cormorant600.woff2'), os.path.join(SP, 'fonts', 'lora400.woff2')
specs = [
    dict(key='aoss', font=CORM, text='Art of Small Steps', size=40, tracking=0.01),
    dict(key='capA', font=CORM, text='A', size=40, tracking=0),
    dict(key='rechart', font=CORM, text='RECHART', size=56, tracking=0.16),
    dict(key='twm', font=LORA, text='THE WAYFINDER METHOD', size=12.5, tracking=0.34),
    dict(key='endorse', font=LORA, text='an Art of Small Steps programme', size=13, tracking=0.04),
]
sf = os.path.join(SP, 'textspecs.json')
json.dump(specs, open(sf, 'w', encoding='utf-8'))
T = json.loads(subprocess.run(['node', os.path.join(SP, 'textpath.mjs'), sf], capture_output=True, text=True, check=True).stdout)

def text(key, x, y, fill):
    return f'<path transform="translate({x:.2f} {y:.2f})" fill="{fill}" d="{T[key]["d"]}"/>'

# ---------- S2: stepping stones along a golden spiral ----------
def stones_geo(n=13, step_deg=38, t0=2.0, size=0.17):
    ts = [t0 + k * math.radians(step_deg) for k in range(n)]
    pts = []
    for t in ts:
        r = math.exp(B * t)
        pts.append((r * math.cos(t), -r * math.sin(t), size * r))
    xs = [x - rr for x, y, rr in pts] + [x + rr for x, y, rr in pts]
    ys = [y - rr for x, y, rr in pts] + [y + rr for x, y, rr in pts]
    return pts, (min(xs), min(ys), max(xs), max(ys))

def stones(box, fill, n=13, step_deg=38, t0=2.0, size=0.17, minr=0.0, ox=0, oy=0):
    pts, (x0, y0, x1, y1) = stones_geo(n, step_deg, t0, size)
    s = box / max(x1 - x0, y1 - y0)
    dx = ox + (box - (x1 - x0) * s) / 2 - x0 * s
    dy = oy + (box - (y1 - y0) * s) / 2 - y0 * s
    return ''.join(f'<circle cx="{x*s+dx:.2f}" cy="{y*s+dy:.2f}" r="{max(r*s, minr):.2f}" fill="{fill}"/>' for x, y, r in pts)

# favicon: fewer, chunkier stones so it survives 16px
FAV = dict(n=7, step_deg=62, t0=2.6, size=0.24)

# ---------- W2: dot, a route with one loop, an X ----------
def cubic(p0, p1, p2, p3, n=24):
    out = []
    for i in range(1, n + 1):
        u = i / n; v = 1 - u
        out.append((v**3*p0[0] + 3*v*v*u*p1[0] + 3*v*u*u*p2[0] + u**3*p3[0],
                    v**3*p0[1] + 3*v*v*u*p1[1] + 3*v*u*u*p2[1] + u**3*p3[1]))
    return out

def route_pts(W=250, k=3.5, b=3.1, rise=10):
    # horizontal frame: start (0,0), loop around x=0.5W, end (W,-rise); y grows downward
    cx = W * 0.5; cy = -k * b
    loop = []
    for i in range(61):
        t = -math.pi + 2 * math.pi * i / 60
        loop.append((cx + k * (t - b * math.sin(t)), cy - k * b * math.cos(t)))
    a, z = loop[0], loop[-1]
    lead_in = cubic((0, 0), (a[0] * .45, 0), (a[0] * .8, a[1]), a)
    lead_out = cubic(z, (z[0] + (W - z[0]) * .35, z[1]), (W - (W - z[0]) * .3, -rise), (W, -rise))
    return [(0, 0)] + lead_in + loop[1:] + lead_out

def poly(pts):
    return 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x, y in pts)

def route_svg(pts, ox, oy, fill_line, fill_ink, dash, sw, dot_r, x_size, x_sw, start_fill):
    p = [(x + ox, y + oy) for x, y in pts]
    (sx, sy), (ex, ey) = p[0], p[-1]
    h = x_size / 2
    ex2 = ex + h + 3  # X sits just past the end of the line
    return (f'<path d="{poly(p)}" fill="none" stroke="{fill_line}" stroke-width="{sw}" stroke-dasharray="{dash}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="{dot_r}" fill="{start_fill}"/>'
            f'<path d="M{ex2-h:.2f} {ey-h:.2f} L{ex2+h:.2f} {ey+h:.2f} M{ex2+h:.2f} {ey-h:.2f} L{ex2-h:.2f} {ey+h:.2f}" stroke="{fill_ink}" stroke-width="{x_sw}" stroke-linecap="round"/>')

def rot(pts, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [(x * c - y * s, x * s + y * c) for x, y in pts]

def rechart_mark(box, line, ink, start):
    pts = rot(route_pts(W=40, k=2.0, b=2.9, rise=0), math.radians(-40))
    xs = [x for x, y in pts]; ys = [y for x, y in pts]
    pad = box * 0.16
    s = (box - 2 * pad) / max(max(xs) - min(xs), max(ys) - min(ys))
    pts = [((x - min(xs)) * s + pad, (y - min(ys)) * s + pad + (box - 2*pad - (max(ys)-min(ys))*s) / 2) for x, y in pts]
    u = box / 40
    return route_svg(pts, -u * 1.5, u * 1.5, line, ink, f'{2.1*u:.2f} {2.3*u:.2f}', f'{1.9*u:.2f}', f'{3*u:.2f}', 7 * u, f'{2.4*u:.2f}', start)

# ---------- writers ----------
def svg(w, h, body, bg=None, title=''):
    bgr = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{bgr}{body}</svg>\n')

def save(name, content):
    open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(content)

# umbrella mark (square)
for name, fill in [('aoss-mark.svg', COP), ('aoss-mark-ink.svg', INK), ('aoss-mark-white.svg', '#FFFFFF'), ('aoss-mark-light.svg', COP_ON_DARK)]:
    save(name, svg(100, 100, stones(84, fill, ox=8, oy=8), title='Art of Small Steps'))
save('aoss-favicon.svg', svg(32, 32, stones(30, COP, ox=1, oy=1, **FAV), title='Art of Small Steps'))

# umbrella horizontal lockup
capH = -T['capA']['top']
MARK = 58; GAP = 18; PAD = 6
tw = T['aoss']['width']
W = PAD + MARK + GAP + tw + PAD; H = PAD + MARK + PAD
base = PAD + MARK / 2 + capH / 2
def aoss_h(mark_fill, text_fill):
    return stones(MARK, mark_fill, ox=PAD, oy=PAD) + text('aoss', PAD + MARK + GAP, base, text_fill)
for name, mf, tf in [('aoss-horizontal.svg', COP, INK), ('aoss-horizontal-reversed.svg', COP_ON_DARK, PAPER),
                     ('aoss-horizontal-ink.svg', INK, INK), ('aoss-horizontal-white.svg', '#FFFFFF', '#FFFFFF')]:
    save(name, svg(W, H, aoss_h(mf, tf), title='Art of Small Steps'))

# endorsement line (products carry the umbrella only like this)
ew = T['endorse']['width']; EM = 16
save('aoss-endorsement.svg', svg(EM + 7 + ew + 4, 22, stones(EM, COP, ox=1, oy=3) + text('endorse', EM + 8, 15.5, '#4A5560'), title='an Art of Small Steps programme'))

# RECHART mark
for name, line, ink, start in [('rechart-mark.svg', COP, INK, COP), ('rechart-mark-reversed.svg', COP_ON_DARK, PAPER, COP_ON_DARK),
                               ('rechart-mark-ink.svg', INK, INK, INK), ('rechart-mark-white.svg', '#FFFFFF', '#FFFFFF', '#FFFFFF')]:
    save(name, svg(100, 100, rechart_mark(100, line, ink, start), title='RECHART'))

# RECHART stacked lockup
rw = T['rechart']['width']; tw2 = T['twm']['width']
RW = 260
rp = route_pts(W=RW)
ry0 = min(y for x, y in rp); ry1 = max(y for x, y in rp)
SW = max(rw, RW + 20, tw2) + 24
rcap = -T['rechart']['top']
y_rc = 12 + rcap
y_route = y_rc + 16 - ry0
y_twm = y_route + ry1 + 30
SH = y_twm + 10
def rechart_stack(ink, line, sub, start):
    return (text('rechart', (SW - rw) / 2, y_rc, ink)
            + route_svg(rp, (SW - RW) / 2 - 6, y_route, line, ink, '4 4.6', 2.2, 3.8, 10, 2.6, start)
            + text('twm', (SW - tw2) / 2, y_twm, sub))
for name, ink, line, sub, start in [('rechart-stacked.svg', INK, COP, DCOP, COP), ('rechart-stacked-reversed.svg', PAPER, COP_ON_DARK, COP_ON_DARK, COP_ON_DARK),
                                    ('rechart-stacked-ink.svg', INK, INK, INK, INK), ('rechart-stacked-white.svg', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF')]:
    save(name, svg(SW, SH, rechart_stack(ink, line, sub, start), title='RECHART · The Wayfinder Method'))

# avatars (square, background baked in; platforms crop to a circle)
save('aoss-avatar.svg', svg(1024, 1024, stones(600, COP, ox=212, oy=212), bg=PAPER, title='Art of Small Steps'))
save('rechart-avatar.svg', svg(1024, 1024, rechart_mark(640, COP_ON_DARK, PAPER, COP_ON_DARK).replace('', '') , bg=SEA, title='RECHART').replace('<rect width="1024" height="1024" fill="#1C4F6B"/>', '<rect width="1024" height="1024" fill="#1C4F6B"/><g transform="translate(192 192)">', 1).replace('</svg>', '</g></svg>'))
print('ok', sorted(os.listdir(OUT)))

# RECHART favicon: solid route, no dashes, so it still reads at 16px
fav = rechart_mark(32, COP, INK, COP)
fav = fav.replace('stroke-dasharray="1.68 1.84"', '').replace('stroke-width="1.52"', 'stroke-width="2.2"', 1)
save('rechart-favicon.svg', svg(32, 32, fav, title='RECHART'))
