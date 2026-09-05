from fmproof import compare


def test_core_precedence():
    assert compare("1.0.0", "2.0.0") == -1
    assert compare("2.0.0", "2.0.0") == 0


def test_prerelease_below_release():
    assert compare("1.0.0-alpha", "1.0.0") == -1
    assert compare("1.0.0-alpha.1", "1.0.0-alpha.2") == -1
