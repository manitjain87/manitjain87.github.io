#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the four-part Ninety-Six Cents series.

The three .md files are the SOURCE OF TRUTH — edit them directly and re-run this.
The one-off splitter that carved them out of the monolith is archived at
~/Documents/ai-capex-note-2026Q2/ninety-six-cents.split-generator.py; do not re-run it,
it would clobber later edits. Fact coverage/novelty harness:
~/Documents/ai-capex-note-2026Q2/fact_inventory_check.py <base> <parts...>

Edit the markdown, run this. One renderer, three per-part configs (PARTS).
Handles: bold-before-italics, 4-column table cap (dropped columns are
re-inserted as jony-label prose), the in-body part label, a stat strip, prev/next
series nav, and stripping the in-content disclaimer (the template footer owns it).

Markdown rules this enforces by assertion: no HTML entities, no comments.
"""
import re, os, html as H

ONE, TWO, THREE = 'ninety-six-cents.html', 'ninety-six-cents-part-two.html', 'ninety-six-cents-part-three.html'
FOUR = 'ninety-six-cents-part-four.html'

def stat_strip(items):
    return ('<div class="jony-stat-strip">\n                '
            + '\n                '.join(
                '<div class="jony-stat-item"><div class="jony-stat-value">%s</div>'
                '<div class="jony-stat-label">%s</div></div>' % (v, l) for v, l in items)
            + '\n            </div>')

PARTS = [
 dict(md='ninety-six-cents.md', out=ONE, h1='Ninety-Six Cents', title='Ninety-Six Cents',
      part='Part one of four', prev=None, nxt=(TWO, 'The Counterparty'),
      desc=("Ten companies along the AI compute chain reported between 22 July and 30 September 2026. The four "
            "hyperscalers spent 96 cents of every operating dollar on capital expenditure, Micron 25 and NVIDIA 11, "
            "while Samsung made chips its entire profit and lost money on phones because memory got too expensive."),
      anchor='<p>That is the post. The capex debate is being argued on the wrong line of the P&amp;L.</p>',
      stats=[('$171.8bn', 'Operating cash flow'), ('$164.9bn', 'Capex'),
             ('$6.9bn', 'Free cash flow'), ('96.0%', 'Capex / OCF')],
      tables=[('<td>Microsoft (FQ4 FY26)</td>',
               '<p><span class="jony-label">Capex as a share of operating cash flow</span> Microsoft 64.6% '
               '&middot; Meta 97.5% &middot; Alphabet 115.0% &middot; Amazon 116.9% &middot; '
               '<strong>combined 96.0%</strong>.</p>'),
              ('<td><strong>Micron (FQ4 FY26)</strong></td>',
               '<p><span class="jony-label">Capex as a share of operating cash flow</span> Micron 25.3% '
               '&middot; NVIDIA 11.1% &middot; <strong>four hyperscalers 96.0%</strong>.</p>')]),

 dict(md='ninety-six-cents-part-two.md', out=TWO, h1='The Counterparty', title='The Counterparty',
      part='Part two of four', prev=(ONE, 'Ninety-Six Cents'), nxt=(THREE, 'What Survives the Counterparty'),
      desc=("A material, named slice of Microsoft's, Alphabet's and Amazon's cloud backlogs is one counterparty. "
            "Anthropic has committed at least $518 billion, about 80% of it non-cancelable, and its share of "
            "production spend on Vercel's AI Gateway broke an eleven-month floor in September."),
      anchor='This part is about whether that revenue is collectible.</p>',
      stats=[('$518bn', 'Committed, per Reuters'), ('~80%', 'Non-cancelable, per Reuters'),
             ('45.8%', 'Sept gateway spend share'), ('+143%', 'Q1 to Q2, on a stated floor')],
      tables=[('<td>Microsoft</td><td>Commercial RPO</td>',
               '<p><span class="jony-label">Conversion disclosed</span> Microsoft, about 30% in the next twelve '
               'months on a weighted-average duration of 2.3 years &middot; Alphabet, <em>"just over 50%"</em> '
               'over the next 24 months &middot; Amazon, not quantified.</p>')]),

 dict(md='ninety-six-cents-part-three.md', out=THREE, h1='What Survives the Counterparty',
      title='What Survives the Counterparty', part='Part three of four',
      prev=(TWO, 'The Counterparty'), nxt=(FOUR, 'The Credit Layer'),
      desc=("The infrastructure gets used even if the company that underwrote it does not survive. NVIDIA has "
            "agreed to pay a headline $12.93 billion for Hugging Face, open-weight models now run a majority of "
            "gateway tokens on 14 cents "
            "of every dollar, and the real risk is timing: the commitments mature in 2027."),
      anchor='does not have to be the thing that underwrote it.</p>',
      stats=[('56%', 'Of gateway tokens'), ('14%', 'Of gateway spend'),
             ('$12.93bn', 'NVIDIA\u2013Hugging Face, announced'), ('2027', 'When commitments mature')],
      tables=[]),
 dict(md='ninety-six-cents-part-four.md', out=FOUR, h1='The Credit Layer',
      title='The Credit Layer', part='Part four of four',
      prev=(THREE, 'What Survives the Counterparty'), nxt=None,
      desc=("The risk in the AI buildout has moved from the equity layer to the credit layer, and the credit "
            "layer is the least disclosed part of the chain. NVIDIA's guaranty is filed with its loss formula "
            "redacted. Three of the four largest buyers became net raisers of capital in the first half of 2026; "
            "the fourth carries $329.1 billion of datacentre leases that have not yet commenced."),
      anchor='<strong>Who holds the credit risk, and can you see it?</strong></p>',
      stats=[('$108.5bn', 'NVIDIA guarantees, maximum gross'), ('$329.1bn', 'Microsoft leases not yet commenced'),
             ('$46.03bn', 'Meta maximum exposure, one VIE'), ('+$86.3bn', 'Alphabet H1 2026 net financing')],
      tables=[('<td>Future commitments</td>',
               '<p><span class="jony-label">Disclosed separately; NVIDIA states no combined total</span></p>'),
              ('<td>2025 Q1</td>',
               '<p><span class="jony-label">Computed from EDGAR quarterly form indexes</span></p>')]),
]

# ------------------------------------------------------------------ renderer
def _drop_last(block):
    return '\n'.join(('|' + '|'.join(l.split('|')[1:-1][:-1]) + '|') if l.startswith('|') else l
                     for l in block.split('\n'))

def cap_tables(text):
    lines, res, i = text.split('\n'), [], 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1]):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            blk = '\n'.join(lines[i:j])
            if len(lines[i].split('|')[1:-1]) > 4:
                blk = _drop_last(blk)
            res.append(blk); i = j
        else:
            res.append(lines[i]); i += 1
    return '\n'.join(res)

def inline(s):
    s = H.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)           # BOLD BEFORE ITALICS
    s = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+?)\]\(([^)]+?)\)', r'<a href="\2">\1</a>', s)
    return s

def nocode(s):
    """Strip <code> spans before the stray-** check: [***] redaction markers are legitimate."""
    return re.sub(r'<code>.*?</code>', '', s, flags=re.S)

PARTLBL = {'ONE': 'Part one of four', 'TWO': 'Part two of four', 'THREE': 'Part three of four',
           'FOUR': 'Part four of four'}

def to_blocks(md):
    blocks, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.strip() == '---': blocks.append('<hr>'); i += 1; continue
        if l.lstrip().startswith('<!--'):       # comments must never reach the page
            while i < len(lines) and '-->' not in lines[i]: i += 1
            i += 1; continue
        m = re.match(r'\*\*PART (ONE|TWO|THREE) — (.+?)\*\*', l)
        if m:
            blocks.append('<p><span class="jony-label">%s &middot; %s</span></p>'
                          % (PARTLBL[m.group(1)], m.group(2))); i += 1; continue
        if l.startswith('### '): blocks.append('<h4>%s</h4>' % inline(l[4:].strip())); i += 1; continue
        if l.startswith('## '):  blocks.append('<h3>%s</h3>' % inline(l[3:].strip())); i += 1; continue
        if l.startswith('- '):
            it = []
            while i < len(lines) and lines[i].startswith('- '):
                it.append('<li>%s</li>' % inline(lines[i][2:].strip())); i += 1
            blocks.append('<ul>\n                ' + '\n                '.join(it) + '\n            </ul>')
            continue
        if l.startswith('> '):
            q = []
            while i < len(lines) and lines[i].startswith('> '):
                q.append(lines[i][2:].strip()); i += 1
            blocks.append('<blockquote>\n' + inline(' '.join(q)).replace('<em>', '').replace('</em>', '')
                          + '\n            </blockquote>')
            continue
        if l.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1]):
            hdr = [c.strip() for c in l.split('|')[1:-1]]; i += 2; rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].split('|')[1:-1]]); i += 1
            t = '<table class="jony-data-table">\n<tr>' + ''.join('<th>%s</th>' % inline(c) for c in hdr) + '</tr>\n'
            for r in rows:
                t += '<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>\n'
            blocks.append(t + '</table>'); continue
        para = [l]; i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('|', '#', '>', '- ', '---', '**PART')):
            para.append(lines[i]); i += 1
        blocks.append('<p>%s</p>' % inline(' '.join(x.strip() for x in para)))
    return blocks

def after_table(b, needle, add):
    i = b.find(needle); assert i > 0, 'table anchor missing: %s' % needle[:50]
    e = b.find('</table>', i) + len('</table>')
    return b[:e] + '\n\n            ' + add + b[e:]

def nav(p, where):
    bits = []
    if p['prev']: bits.append('<a href="%s">&larr; %s</a>' % p['prev'])
    if p['nxt']:  bits.append('<a href="%s">%s &rarr;</a>' % p['nxt'])
    if not bits: return ''
    style = ('margin: %s; padding-top: 24px; border-top: 1px solid var(--color-border); '
             'display: flex; justify-content: space-between; gap: 24px; font-size: 0.9rem;'
             % ('0 0 40px' if where == 'top' else '48px 0 0'))
    return '<div style="%s">%s</div>' % (style, ''.join('<span>%s</span>' % b for b in bits))

TPL = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%(title)s &mdash; Manit Jain</title>
    <meta name="description" content="%(desc)s">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <nav>
        <div class="container">
            <a href="../index.html" class="logo">Manit Jain</a>
            <ul>
                <li><a href="../index.html#experience">Experience</a></li>
                <li><a href="../index.html#investing">Investing</a></li>
                <li><a href="../index.html#projects">Projects</a></li>
                <li><a href="../index.html#writing">Writing</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <article class="blog-post">
        <a href="../index.html#writing" class="back-link">&larr; Back to all posts</a>

        <header class="blog-post-header">
            <div class="blog-category">Strategic Finance &middot; Ninety-Six Cents</div>
            <h1 class="blog-post-title">%(h1)s</h1>
            <div class="blog-post-meta">October 15, 2026 &middot; %(rt)d min read &middot; %(part)s</div>
        </header>

        <div class="blog-post-content">

            %(navtop)s%(body)s

        </div>

        %(navbot)s

        <div style="margin-top: 60px; padding-top: 40px; border-top: 1px solid var(--color-border); text-align: center;">
            <a href="../index.html#contact" class="btn btn-primary">Get in touch</a>
        </div>
    </article>

    <footer>
        <div class="container">
            <p><em>Disclaimer: The views and opinions expressed in this article are solely my own personal research and analysis. They do not represent, reflect, or relate to the views of any past, current, or future employer, client, or affiliated organization.</em></p>
            <p>&copy; 2026 Manit Jain. All rights reserved.</p>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>
'''

def build(p):
    md = open(p['md'], encoding='utf-8').read()
    assert '&mdash;' not in md and '&amp;' not in md, '%s: HTML entity in markdown' % p['md']
    assert '<!--' not in md, '%s: comment in markdown' % p['md']
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    md = re.sub(r'\A\s*#\s+' + re.escape(p['h1']) + r'\s*\n', '', md.lstrip('\n'))
    assert not md.lstrip().startswith('# '), '%s: H1 not stripped' % p['md']
    body = '\n\n            '.join(to_blocks(cap_tables(md)))

    a = p['anchor']
    assert body.count(a) == 1, '%s: stat-strip anchor count=%d' % (p['md'], body.count(a))
    e = body.find(a) + len(a)
    if not a.endswith('</p>'):
        e = body.find('</p>', e) + 4
    body = body[:e] + '\n\n            ' + stat_strip(p['stats']) + body[e:]

    for needle, add in p['tables']:
        body = after_table(body, needle, add)

    body = re.sub(r'\n\s*<p><em>Disclaimer: The views and opinions[^<]*</em></p>', '', body)

    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    page = TPL % dict(title=p['title'], desc=p['desc'], h1=p['h1'], part=p['part'],
                      rt=max(1, round(words / 206)), body=body,
                      navtop=nav(p, 'top') + ('\n\n            ' if nav(p, 'top') else ''),
                      navbot=nav(p, 'bot'))
    open(p['out'], 'w', encoding='utf-8').write(page)
    return page, words

# ------------------------------------------------------------------ validate
def validate(name, page, words):
    tags = re.findall(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*?(/?)>', page)
    void = {'meta', 'link', 'br', 'hr', 'img', 'input', 'source'}
    st, er = [], 0
    for c, n, s in tags:
        n = n.lower()
        if n in void or s: continue
        if c:
            if st and st[-1] == n: st.pop()
            else: er += 1
        else: st.append(n)
    tbl = re.findall(r'<table.*?</table>', page, re.S)
    mx = max((max(len(re.findall(r'<t[hd][ >]', r)) for r in re.findall(r'<tr>.*?</tr>', t, re.S))
              for t in tbl), default=0)
    ok = (not st and er == 0 and mx <= 4
          and len(re.findall(r'<p(?:\s[^>]*)?>', page)) == page.count('</p>')
          and page.count('<strong>') == page.count('</strong>')
          and page.count('<em>') == page.count('</em>')
          and page.count('Disclaimer:') == 1 and nocode(page).count('**') == 0
          and len(re.findall(r'#[0-9a-fA-F]{6}', page)) == 0)
    print('%-34s %s  unclosed=%s mism=%d maxcols=%d tables=%d p=%d/%d strong=%d/%d em=%d/%d '
          'discl=%d stray**=%d hex=%d words=%d read=%dmin %dKB'
          % (name, 'PASS' if ok else 'FAIL', st, er, mx, len(tbl),
             len(re.findall(r'<p(?:\s[^>]*)?>', page)), page.count('</p>'),
             page.count('<strong>'), page.count('</strong>'), page.count('<em>'), page.count('</em>'),
             page.count('Disclaimer:'), nocode(page).count('**'), len(re.findall(r'#[0-9a-fA-F]{6}', page)),
             words, max(1, round(words / 206)), len(page.encode()) // 1024))
    return ok

if __name__ == '__main__':
    allok, built = True, {}
    for p in PARTS:
        page, words = build(p)
        built[p['out']] = page
        allok &= validate(p['out'], page, words)
    # every internal series link must resolve to a file that now exists
    for out, page in built.items():
        for href in set(re.findall(r'href="(ninety-six-cents[^"#]*\.html)"', page)):
            assert os.path.exists(href), '%s -> missing %s' % (out, href)
    print('series links resolve: OK' if allok else 'SERIES BUILD HAS FAILURES')
