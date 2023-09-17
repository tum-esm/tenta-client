"""Test whether the automatically generated documentation is up to date.

This is necessary because the documentation build script does not generate
the documentation pages automatically. Otherwise we would have to set up
the full Python environment on the CI server for the documentation build."""

import hashlib
import os
from typing import List
import pytest

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PAGES_DIR = os.path.join(PROJECT_DIR, "docs", "pages")
FILENAMES = ["index.mdx", "examples.mdx", "api.mdx"]


@pytest.mark.order(4)
def test_documentation_sync() -> None:
    checksums_before: List[str] = []
    for filename in FILENAMES:
        with open(os.path.join(DOCS_PAGES_DIR, filename), "r") as f:
            checksums_before.append(hashlib.md5(f.read().encode()).hexdigest())

    assert (
        os.system(f"python {os.path.join(PROJECT_DIR, 'scripts', 'generate_docs.py')}")
        == 0
    )

    checksums_after: List[str] = []
    for filename in FILENAMES:
        with open(os.path.join(DOCS_PAGES_DIR, filename), "r") as f:
            checksums_after.append(hashlib.md5(f.read().encode()).hexdigest())

    assert "".join(checksums_before) == "".join(checksums_after)
