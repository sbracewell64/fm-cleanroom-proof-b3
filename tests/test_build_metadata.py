"""The ONLY test of build-metadata precedence behavior. The ruled option's
byte-pinned patch fully owns this file; no other test asserts this behavior,
so the consumed artifact requalifies cleanly at its head."""
import pytest
from fmproof import compare


def test_build_metadata_precedence_unresolved_at_baseline():
    with pytest.raises(NotImplementedError):
        compare("1.0.0+a", "1.0.0+b")
