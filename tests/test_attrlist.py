import asciidoc_gen as adoc


def test_attrlist_empty():
    with adoc.AttrList() as l:
        assert str(l) == "[]"


def test_shorthand_attributes():
    with adoc.AttrList() as l:
        adoc.OptionAttribute("headers")
        assert str(l) == "[%headers]"

        adoc.BlockStyleAttribute(value="appendix")
        assert str(l) == "[appendix%headers]"

        adoc.RoleAttribute(value="big")
        assert str(l) == "[appendix.big%headers]"

        adoc.RoleAttribute(value="verybig")
        assert str(l) == "[appendix.big.verybig%headers]"

        adoc.IDAttribute(value="custom_id")
        assert str(l) == "[appendix#custom_id.big.verybig%headers]"


def test_positionals():
    with adoc.AttrList() as l:
        adoc.PositionalAttribute("cookies")
        adoc.PositionalAttribute("320")
        adoc.PositionalAttribute("640")
        adoc.PositionalAttribute("sunset")

        assert str(l) == "[cookies,320,640,sunset]"


def test_named():
    with adoc.AttrList() as l:
        adoc.NamedAttribute(name="favorite_food", value="cookies")
        adoc.NamedAttribute(name="fur_color", value="blue")

        assert str(l) == "[favorite_food=cookies,fur_color=blue]"


def test_everything():
    with adoc.AttrList() as l:
        adoc.NamedAttribute(name="favorite_food", value="cookies")
        adoc.NamedAttribute(name="fur_color", value="blue")

        adoc.PositionalAttribute("cookies")
        adoc.PositionalAttribute("320")
        adoc.PositionalAttribute("640")
        adoc.PositionalAttribute("sunset")

        adoc.OptionAttribute("headers")

        adoc.BlockStyleAttribute(value="appendix")

        adoc.RoleAttribute(value="big")

        adoc.RoleAttribute(value="verybig")

        adoc.IDAttribute(value="sesame_street")

        assert (
            str(l)
            == "[appendix#sesame_street.big.verybig%headers,cookies,320,640,sunset,favorite_food=cookies,fur_color=blue]"
        )
