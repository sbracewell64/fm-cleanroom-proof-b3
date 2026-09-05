"""The ONLY test of build-metadata precedence. Resolved: Option A — ignored (SemVer 2.0.0 s10)."""
from fmproof import compare


def test_build_metadata_ignored_in_precedence():
    assert compare("1.0.0+a", "1.0.0+b") == 0
    assert compare("1.0.0+build.9", "1.0.0") == 0
