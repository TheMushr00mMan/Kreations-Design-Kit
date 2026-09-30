#!/usr/bin/env python3
"""Add tasteful transitions and click builds to a finished .pptx.

pptxgenjs can't write transitions or animations, so this post-processes the file.
Only calm, purposeful effects are offered (see references/slides.md §5).

Usage:
  python pptx_motion.py in.pptx out.pptx --all fade
  python pptx_motion.py in.pptx out.pptx --all fade --slide 4=morph --slide 7=push:l
  python pptx_motion.py in.pptx out.pptx --build 5=step1,step2,step3 --build 9=!!chart:wipe

Transitions: none | fade | morph | push[:l|r|u|d] | wipe[:l|r|u|d]   (optional @seconds, e.g. morph@1.2)
  morph plays in PowerPoint 2019+/365; other apps get a fade fallback.
  For morph, give matching objects the same name on both slides, starting with "!!"
  (pptxgenjs: objectName: "!!hero").
Builds: comma-separated object names (pptxgenjs objectName) that appear on click, in order.
  Add --auto 250 to make every build play by itself when the slide starts (items 250 ms apart),
  which is the kit's default for pitch and creative decks.
  Add ":wipe" to a name for a left-to-right wipe instead of the default fade.
  Works on text boxes, shapes, pictures and groups. A slide that already has animations is
  refused unless you pass --replace-timing (its old animations are then replaced).
  Existing transitions, animations and extensions are kept unless you change them.

Slide numbers are 1-based. Prints what it changed. Keep the no-motion deck readable:
builds only reveal content that is already correct when shown.
"""
import argparse, re, shutil, sys, tempfile, zipfile, os
import html

P14 = 'xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main"'
P159 = 'xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"'
MC = 'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"'
DIRS = {'l': 'l', 'r': 'r', 'u': 'u', 'd': 'd'}


def transition_xml(spec):
    name, _, dur = spec.partition('@')
    name, _, arg = name.partition(':')
    name = name.strip().lower()
    secs = float(dur) if dur else (1.0 if name == 'morph' else 0.6)
    ms = int(secs * 1000)
    if name in ('none', ''):
        return ''
    if name == 'fade':
        inner = '<p:fade/>'
    elif name == 'push':
        inner = f'<p:push dir="{DIRS.get(arg or "u", "u")}"/>'
    elif name == 'wipe':
        inner = f'<p:wipe dir="{DIRS.get(arg or "r", "r")}"/>'
    elif name == 'morph':
        return (f'<mc:AlternateContent {MC}><mc:Choice {P159} Requires="p159">'
                f'<p:transition spd="slow" {P14} p14:dur="{ms}"><p159:morph option="byObject"/></p:transition>'
                f'</mc:Choice><mc:Fallback><p:transition spd="slow"><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>')
    else:
        sys.exit(f'Unsupported transition "{name}". Use none, fade, morph, push or wipe (see slides.md §5).')
    return (f'<mc:AlternateContent {MC}><mc:Choice {P14} Requires="p14">'
            f'<p:transition spd="med" p14:dur="{ms}">{inner}</p:transition></mc:Choice>'
            f'<mc:Fallback><p:transition spd="med">{inner}</p:transition></mc:Fallback></mc:AlternateContent>')


def build_xml(spids, auto=0):
    """Main-sequence click builds: each item appears on its own click.
    spids: list of (spid, effect, kind); kind is 'sp', 'pic', 'grp' or 'frame'.
    Only plain shapes/text boxes get a p:bldP entry."""
    n = [2]

    def nid():
        n[0] += 1
        return n[0]

    clicks = []
    autos = []
    for i, (spid, effect, _kind) in enumerate(spids):
        a, b, c, d = nid(), nid(), nid(), nid()
        if effect == 'wipe':
            preset, sub, filt = 22, 8, 'wipe(left)'
        else:
            preset, sub, filt = 10, 0, 'fade'
        if auto:
            autos.append(
                f'<p:par><p:cTn id="{b}" fill="hold"><p:stCondLst><p:cond delay="{i * auto}"/></p:stCondLst><p:childTnLst>'
                f'<p:par><p:cTn id="{c}" presetID="{preset}" presetClass="entr" presetSubtype="{sub}" fill="hold" grpId="0" nodeType="afterEffect">'
                f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                f'<p:set><p:cBhvr><p:cTn id="{d}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
                f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
                f'<p:to><p:strVal val="visible"/></p:to></p:set>'
                f'<p:animEffect transition="in" filter="{filt}"><p:cBhvr><p:cTn id="{nid()}" dur="500"/>'
                f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
                f'</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
            continue
        clicks.append(
            f'<p:par><p:cTn id="{a}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{b}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{c}" presetID="{preset}" presetClass="entr" presetSubtype="{sub}" fill="hold" grpId="0" nodeType="clickEffect">'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'<p:set><p:cBhvr><p:cTn id="{d}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            f'<p:to><p:strVal val="visible"/></p:to></p:set>'
            f'<p:animEffect transition="in" filter="{filt}"><p:cBhvr><p:cTn id="{nid()}" dur="500"/>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
            f'</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    if auto and autos:
        # one group that starts by itself when the slide begins; items follow each other with a short stagger
        clicks = ['<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/>'
                  '<p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond></p:stCondLst><p:childTnLst>'
                  + ''.join(autos) + '</p:childTnLst></p:cTn></p:par>']
    shapes = [sp for sp, _e, kind in spids if kind == 'sp']
    bld = ('<p:bldLst>' + ''.join(f'<p:bldP spid="{sp}" grpId="0" animBg="1"/>' for sp in shapes) + '</p:bldLst>') if shapes else ''
    return ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
            '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
            + ''.join(clicks) +
            '</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
            '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
            '</p:childTnLst></p:cTn></p:par></p:tnLst>'
            + bld + '</p:timing>')


TAG = re.compile(r'(<!--.*?-->|<\?.*?\?>|<!\[CDATA\[.*?\]\]>)|<(/?)([A-Za-z_][\w.:-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*?)(/?)>', re.S)


def top_children(xml):
    """Return (root_open_end, root_close_start, [(name, start, end), ...]) for the
    direct children of the root element, by counting element depth (no regex guessing)."""
    depth = 0
    kids = []
    root_open_end = root_close = None
    cur = None
    for m in TAG.finditer(xml):
        if m.group(1):          # comment, processing instruction, CDATA
            continue
        closing, name, selfclose = m.group(2) == '/', m.group(3), m.group(5) == '/'
        if closing:
            depth -= 1
            if depth == 1 and cur:
                kids.append((cur[0], cur[1], m.end())); cur = None
            elif depth == 0:
                root_close = m.start()
        else:
            if depth == 0:
                root_open_end = m.end()
            elif depth == 1:
                if selfclose:
                    kids.append((name, m.start(), m.end()))
                else:
                    cur = (name, m.start())
            if not selfclose:
                depth += 1
    return root_open_end, root_close, kids


def shape_kinds(xml):
    """Map object name -> (id, kind) using the non-visual property block each cNvPr sits in."""
    out = {}
    for m in re.finditer(r'<p:(nvSpPr|nvPicPr|nvGrpSpPr|nvGraphicFramePr|nvCxnSpPr)>\s*<p:cNvPr\b([^>]*)>', xml):
        attrs = m.group(2)
        i = re.search(r'\bid="(\d+)"', attrs); n = re.search(r'\bname="([^"]*)"', attrs)
        if i and n:
            kind = {'nvSpPr': 'sp', 'nvPicPr': 'pic', 'nvGrpSpPr': 'grp', 'nvGraphicFramePr': 'frame', 'nvCxnSpPr': 'cxn'}[m.group(1)]
            out[html.unescape(n.group(1))] = (i.group(1), kind)
    return out


def slide_order(z):
    pres = z.read('ppt/presentation.xml').decode('utf8')
    rels = z.read('ppt/_rels/presentation.xml.rels').decode('utf8')
    rmap = dict(re.findall(r'<Relationship[^>]*Id="([^"]+)"[^>]*Target="([^"]+)"', rels))
    rmap.update({k: v for v, k in re.findall(r'<Relationship[^>]*Target="([^"]+)"[^>]*Id="([^"]+)"', rels)})
    ids = re.findall(r'<p:sldId [^>]*r:id="([^"]+)"', pres)
    return ['ppt/' + rmap[i].lstrip('/').replace('ppt/', '') for i in ids]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('src'); ap.add_argument('dst')
    ap.add_argument('--all', default=None, help='transition for every slide (e.g. fade)')
    ap.add_argument('--slide', action='append', default=[], help='N=transition, overrides --all')
    ap.add_argument('--build', action='append', default=[], help='N=name1,name2[:wipe],...')
    ap.add_argument('--auto', type=int, default=0, metavar='MS', help='builds play by themselves when the slide starts, MS apart (e.g. 250); default is on click')
    ap.add_argument('--replace-timing', action='store_true', help='allow --build to replace animations a slide already has')
    a = ap.parse_args()

    per = {}
    for s in a.slide:
        k, _, v = s.partition('='); per[int(k)] = v
    builds = {}
    for s in a.build:
        k, _, v = s.partition('='); builds[int(k)] = [x for x in v.split(',') if x]

    zin = zipfile.ZipFile(a.src)
    order = slide_order(zin)
    tmp = tempfile.mktemp(suffix='.pptx')
    zout = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
    report = []
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename in order:
            num = order.index(item.filename) + 1
            xml = data.decode('utf8')
            spec = per.get(num, a.all)
            if spec is None and num not in builds:
                zout.writestr(item, data); continue
            open_end, close_start, kids = top_children(xml)
            parts = {'cSld': [], 'clrMapOvr': [], 'transition': [], 'timing': [], 'extLst': [], 'other': []}
            for name, a0, a1 in kids:
                frag = xml[a0:a1]
                if name == 'p:cSld': parts['cSld'].append(frag)
                elif name == 'p:clrMapOvr': parts['clrMapOvr'].append(frag)
                elif name == 'p:transition' or (name == 'mc:AlternateContent' and '<p:transition' in frag): parts['transition'].append(frag)
                elif name == 'p:timing': parts['timing'].append(frag)
                elif name == 'p:extLst': parts['extLst'].append(frag)
                else: parts['other'].append(frag)
            trans = ''.join(parts['transition'])
            timing = ''.join(parts['timing'])
            if spec is not None:
                trans = transition_xml(spec)
                report.append(f'slide {num}: transition {spec}')
            if num in builds:
                if timing and not a.replace_timing:
                    sys.exit(f'slide {num} already has animations. Re-run with --replace-timing to replace them '
                             f'(they will be lost), or leave this slide out of --build.')
                names = shape_kinds(xml[:open_end] + ''.join(parts['cSld']))
                items = []
                for raw in builds[num]:
                    nm, _, eff = raw.partition(':')
                    if nm not in names:
                        sys.exit(f'slide {num}: no object named "{nm}". Found: {sorted(names)}')
                    items.append((names[nm][0], eff or 'fade', names[nm][1]))
                timing = build_xml(items, a.auto)
                report.append(f'slide {num}: builds {builds[num]}' + (' (replaced existing animations)' if parts['timing'] else ''))
            xml = (xml[:open_end] + ''.join(parts['cSld']) + ''.join(parts['clrMapOvr']) + trans + timing
                   + ''.join(parts['other']) + ''.join(parts['extLst']) + xml[close_start:])
            data = xml.encode('utf8')
        zout.writestr(item, data)
    zout.close(); zin.close()
    shutil.move(tmp, a.dst)
    print('\n'.join(report) or 'nothing changed')


if __name__ == '__main__':
    main()
