import asciidoc_gen as adg


def test_lazytext():
    t = adg.LazyText(str, (1,))
    assert str(t) == "1"

    l = [1, 2, 3]
    t = adg.LazyText(str, (l,))
    l.append(4)
    assert str(t) == "[1, 2, 3, 4]"

    assert str(adg.LazyText(lambda: "Hello World")) == "Hello World"
