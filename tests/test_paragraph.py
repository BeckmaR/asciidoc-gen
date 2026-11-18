import pytest
import asciidoc_gen as adg


def test_paragraph():
    with adg.Paragraph() as p:
        adg.Text("Hello World")

        assert len(p.children) == 1

        assert str(p) == "Hello World\n"


def test_long_paragraph():
    with adg.Paragraph() as p:
        adg.Text("To be, or not to be, that is the question.")
        adg.Text("(William Shakespeare)")

        assert len(p.children) == 2
        assert (str(p) ==
                "To be, or not to be, that is the question.\n"
                "(William Shakespeare)\n"
                ) # fmt: skip


def test_paragraph_title():
    with adg.Paragraph() as p:
        adg.Title(text="Famous quote")
        adg.Text("To be, or not to be, that is the question.")
        adg.Text("(William Shakespeare)")

        assert p.title

        assert (str(p) ==
                ".Famous quote\n"
                "To be, or not to be, that is the question.\n"
                "(William Shakespeare)\n"
                ) # fmt: skip

def test_paragraph_title_shorthand():
    with adg.Paragraph().title("Famous quote") as p:
        adg.Text("To be, or not to be, that is the question.")
        adg.Text("(William Shakespeare)")

        assert p.title

        assert (str(p) ==
                ".Famous quote\n"
                "To be, or not to be, that is the question.\n"
                "(William Shakespeare)\n"
                ) # fmt: skip


def test_paragraph_title_out_of_order():
    with adg.Paragraph() as p:
        adg.Text("To be, or not to be, that is the question.")
        adg.Text("(William Shakespeare)")
        adg.Title(text="Famous quote")

        assert p.title

        assert (str(p) ==
                ".Famous quote\n"
                "To be, or not to be, that is the question.\n"
                "(William Shakespeare)\n"
                ) # fmt: skip


def test_paragraph_title_twice():
    with adg.Paragraph() as p:
        adg.Text("To be, or not to be, that is the question.")
        adg.Text("(William Shakespeare)")
        adg.Title(text="First title")
        adg.Title(text="Famous quote")

        assert p.title

        assert (str(p) ==
                ".Famous quote\n"
                "To be, or not to be, that is the question.\n"
                "(William Shakespeare)\n"
                ) # fmt: skip
