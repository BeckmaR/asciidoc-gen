import asciidoc_gen as adg


def test_lists():
    with adg.List() as l:
        adg.Title(text="Lists are awesome")
        adg.UnorderedListItem("Cucumbers")
        adg.UnorderedListItem("Tomatoes")
        adg.UnorderedListItem("Bacon")

        assert (
            str(l) == ".Lists are awesome\n"
            "* Cucumbers\n"
            "* Tomatoes\n"
            "* Bacon\n"
        ) # fmt: skip


def test_nested_lists():
    with adg.List() as l:
        adg.Title(text="Lists are awesome")
        adg.UnorderedListItem("Veggies")
        adg.UnorderedListItem("Cucumbers", level=2)
        adg.UnorderedListItem("Tomatoes", level=2)
        adg.UnorderedListItem("Deli")
        adg.UnorderedListItem("Bacon", level=2)

        assert (
            str(l) == ".Lists are awesome\n"
            "* Veggies\n"
            "** Cucumbers\n"
            "** Tomatoes\n"
            "* Deli\n"
            "** Bacon\n"
        ) # fmt: skip
