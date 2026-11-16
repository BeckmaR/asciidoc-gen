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
