# AsciiDoc-Gen

This is a library to generate [AsciiDoc](https://docs.asciidoctor.org/asciidoc/latest/) sources written in Python.

The API of this library is inspired by [NiceGUI](https://nicegui.io). Documents are created as ASTs using Python context managers:

```Python
with adg.AsciiDocDocument(path=doc_path) as doc:
    with adg.Section(text="Hello AsciiDoc"):
        adg.IDAttribute("custom_id")
    with adg.Paragraph():
        adg.Text("This is a test document.")
        adg.Text("It showcases multiple AsciiDoc syntax elements.")
    with adg.List():
        adg.Title("Lists!")
        adg.UnorderedListItem("Lists")
        adg.UnorderedListItem("Lists")
        adg.UnorderedListItem("Lists")

    doc.render()
```

The document is rendered like this:

```AsciiDoc
[#custom_id]
= Hello AsciiDoc

This is a test document.
It showcases multiple AsciiDoc syntax elements.

.Lists!
* Lists
* Lists
* Lists
```
