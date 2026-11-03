import pytest

import asciidoc_gen as adg


def test_document(tmp_path):
    doc = adg.AsciiDocDocument(path=tmp_path / "doc.adoc")
    assert doc.path == tmp_path / "doc.adoc"
    doc.render()
    assert doc.path.read_text() == ""
