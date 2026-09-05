"""The ONLY test of build-metadata precedence. The ruled option's byte-pinned
patch fully owns this file. Decision pending a Browser Sol fm-sol-control/v2 ruling."""
import pytest
from fmproof import compare


@pytest.mark.xfail(reason="build-metadata precedence decision pending fm-sol-control/v2 ruling",
                   raises=NotImplementedError, strict=True)
def test_build_metadata_precedence_decided():
    compare("1.0.0+a", "1.0.0+b")
