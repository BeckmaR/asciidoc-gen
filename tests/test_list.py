import asciidoc_gen as adg


def test_lists(tmp_path):
    doc = adg.AsciiDocDocument(tmp_path / "doc.adoc")
    (
        adg.UnorderedList(doc)
        .title("Lists are awesome")
        .add_item("Cucumbers")
        .add_item("Tomatoes")
        .add_item("Bacon")
    )
    doc.render()
    assert (
        doc.path.read_text() == ".Lists are awesome\n"
        "* Cucumbers\n"
        "* Tomatoes\n"
        "* Bacon\n"
    )


def test_nested_lists(tmp_path):
    doc = adg.AsciiDocDocument(tmp_path / "doc.adoc")
    (
        adg.UnorderedList(doc)
        .title("Lists are awesome")
        .add_item("Veggies")
        .add_item("Tomatoes", level=2)
        .add_item("Cucumbers", level=2)
        .add_item("Deli")
        .add_item("Bacon", level=2)
    )
    doc.render()
    assert (
        doc.path.read_text() == ".Lists are awesome\n"
        "* Veggies\n"
        "** Tomatoes\n"
        "** Cucumbers\n"
        "* Deli\n"
        "** Bacon\n"
    )
