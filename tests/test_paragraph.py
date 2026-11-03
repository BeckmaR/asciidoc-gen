import pytest
import asciidoc_gen as adg


def test_paragraph(tmp_path):
    page = adg.AsciiDocDocument(tmp_path / "doc.adoc")
    p = adg.Paragraph(page)
    p.add_text("Hello World!")
    page.render()
    
    assert page.path.read_text() == "Hello World!\n"

def test_multiple_paragraphs(tmp_path):
    page = adg.AsciiDocDocument(tmp_path / "doc.adoc")
    adg.Paragraph(page).add_text("To be, or not to be, that is the question.").add_text("(Socrates)")
    page.render()
    assert page.path.read_text() == "To be, or not to be, that is the question.\n(Socrates)\n"
