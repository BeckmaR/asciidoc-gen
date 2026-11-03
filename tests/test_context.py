import pytest
import asciidoc_gen as adg


def test_paragraph(tmp_path):
    with adg.AsciiDocDocument(path=tmp_path / "doc.adoc") as page:
        p = adg.Paragraph()
        p.add_text("Hello World!")
        page.render()

        assert page.path.read_text() == "Hello World!\n"


def test_multiple_paragraphs(tmp_path):
    with adg.AsciiDocDocument(path=tmp_path / "doc.adoc") as page:
        adg.Paragraph().add_text("To be, or not to be, that is the question.").add_text(
            "(William Shakespeare)"
        )
        adg.Paragraph().add_text(
            "Your time is limited, so don't waste it living someone else's life."
        ).add_text("(Steve Jobs)")
        page.render()

        assert (
            page.path.read_text() == "To be, or not to be, that is the question.\n"
            "(William Shakespeare)\n"
            "\n"
            "Your time is limited, so don't waste it living someone else's life.\n"
            "(Steve Jobs)\n"
        )
