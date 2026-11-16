import pytest

import asciidoc_gen as adg


def test_document(tmp_path):
    doc = adg.AsciiDocDocument(path=tmp_path / "doc.adoc")
    assert doc.path == tmp_path / "doc.adoc"
    doc.render()
    assert doc.path.read_text() == ""


def test_multiple_elements(tmp_path):
    with adg.AsciiDocDocument(path=tmp_path / "doc.adoc") as doc:
        adg.Section(text="Hello AsciiDoc")
        with adg.Paragraph():
            adg.Text("This is a test document.")
            adg.Text("It showcases multiple AsciiDoc syntax elements.")
        with adg.List():
            adg.Title("Lists!")
            adg.UnorderedListItem("Lists")
            adg.UnorderedListItem("Lists")
            adg.UnorderedListItem("Lists")
        
        adg.IncludeMacro(target="includeme.adoc")
        
        doc.render()
        assert (
            doc.path.read_text() == ""
                "= Hello AsciiDoc\n"
                "\n"
                "This is a test document.\n"
                "It showcases multiple AsciiDoc syntax elements.\n"
                "\n"
                ".Lists!\n"
                "* Lists\n"
                "* Lists\n"
                "* Lists\n"
                "\n"
                "include::includeme.adoc[]\n"
        )
