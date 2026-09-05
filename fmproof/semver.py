"""Minimal SemVer 2.0.0 parse + precedence compare.

Build-metadata precedence is DELIBERATELY unresolved at baseline: compare() raises
for versions differing only in build metadata, so the reversible engineering
decision (ignore vs compare) is a real open choice routed to Browser Sol.
"""
import re

_RE = re.compile(
    r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?(?:\+(?P<build>[0-9A-Za-z.-]+))?$")


def parse(text):
    m = _RE.match(text)
    if not m:
        raise ValueError(f"not a semver: {text!r}")
    d = m.groupdict()
    return {"major": int(d["major"]), "minor": int(d["minor"]), "patch": int(d["patch"]),
            "prerelease": d["prerelease"], "build": d["build"]}


def _pre_key(pre):
    if pre is None:
        return (1,)
    out = [0]
    for ident in pre.split("."):
        out.append((0, int(ident)) if ident.isdigit() else (1, ident))
    return tuple(out)


def compare(a, b):
    pa, pb = parse(a), parse(b)
    for k in ("major", "minor", "patch"):
        if pa[k] != pb[k]:
            return -1 if pa[k] < pb[k] else 1
    ka, kb = _pre_key(pa["prerelease"]), _pre_key(pb["prerelease"])
    if ka != kb:
        return -1 if ka < kb else 1
    # Option A (SemVer 2.0.0 s10): build metadata is IGNORED for precedence.
    return 0
