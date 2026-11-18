import asciidoc_gen as adg


def test_empty_table():
    with adg.Table() as table:
        assert (str(table) == ""
                "|===\n"
                "|===\n"
                ) # fmt: skip


def test_table():
    with adg.Table() as table:
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_title():
    with adg.Table() as table:
        adg.Title("Fancy table")
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                ".Fancy table\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_attributes():
    with adg.Table() as table:
        adg.OptionAttribute("header")
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "[%header]\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_headers():
    with adg.Table().header() as table:
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "[%header]\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_cols_str():
    with adg.Table().cols("1,1") as table:
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "[cols=\"1,1\"]\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_cols_list():
    with adg.Table().cols([1, 1]) as table:
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "[cols=\"1,1\"]\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip


def test_table_combined():
    with adg.Table().header().cols([1, 1]) as table:
        with adg.TableRow():
            adg.TableCell("Hello")
            adg.TableCell("World")
        assert (str(table) == ""
                "[%header,cols=\"1,1\"]\n"
                "|===\n"
                "|Hello|World\n"
                "|===\n"
                ) # fmt: skip
