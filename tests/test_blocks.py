import asciidoc_gen as adoc

def test_example_block():
    with adoc.ExampleBlock() as b:
        adoc.Text("Text")
        adoc.Text("Text")
        
        assert (str(b) == ""
                "====\n"
                "Text\n"
                "Text\n"
                "====\n"
                )


def test_example_block_id():
    with adoc.ExampleBlock().id("custom_id") as b:
        adoc.Text("Text")
        adoc.Text("Text")
        
        assert (str(b) == ""
                "[#custom_id]\n"
                "====\n"
                "Text\n"
                "Text\n"
                "====\n"
                )


def test_example_block_role():
    with adoc.ExampleBlock().role("blue") as b:
        adoc.Text("Text")
        adoc.Text("Text")
        
        assert (str(b) == ""
                "[.blue]\n"
                "====\n"
                "Text\n"
                "Text\n"
                "====\n"
                )
