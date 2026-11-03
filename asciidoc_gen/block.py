class AsciiDocBlock:
    def __init__(self, document):
        self._doc = document
        document.add_block(self)

    def render(self):
        raise NotImplementedError("Must be overridden in child classes")

    def __str__(self):
        text = self.render()
        if text and not text[-1] == "\n":
            text += "\n"
        return text


class Section(AsciiDocBlock):
    def __init__(self, document):
        super().__init__(document)
        self._level = 1
        self._custom_id = None
        self._title = None

    def level(self, level: int):
        self._level = level
        return self

    def custom_id(self, id):
        self._custom_id = id
        return self

    def title(self, title):
        self._title = title
        return self

    def render(self):
        text = ""
        if self._custom_id:
            text = f"[#{self._custom_id}]\n"

        text += f"{self._level*'='} {self._title}"
        return text


class Paragraph(AsciiDocBlock):
    def __init__(self, document):
        super().__init__(document)
        self._text_items = []

    def add_text(self, text):
        self._text_items.append(text)
        return self

    def render(self):
        return "\n".join(str(s) for s in self._text_items)


class IncludeMacro(AsciiDocBlock):
    def __init__(self, document):
        super().__init__(document)
        self._target = None
        self._leveloffset = None

    def target(self, target):
        self._target = target
        return self

    def leveloffset(self, offset):
        self._leveloffset = offset
        return self

    def render(self):
        attributes = []
        if self._leveloffset:
            attributes.append(f"leveloffset={self._leveloffset}")
        return f"include::{self._target}[{",".join(attributes)}]"


class UnorderedList(AsciiDocBlock):
    def __init__(self, document):
        super().__init__(document)
        self._items = []
        self._title = None

    def title(self, title):
        self._title = title
        return self

    def add_item(self, item, level=1):
        self._items.append((level, item))
        return self

    def render(self):
        text = ""
        if self._title:
            text += f".{str(self._title)}\n"
        for level, item in self._items:
            text += f"{level*"*"} {str(item)}\n"
        return text
