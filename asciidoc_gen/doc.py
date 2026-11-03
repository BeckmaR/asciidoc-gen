import pathlib
import re

from .block import AsciiDocBlock


class Document:
    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return pathlib.Path(self._path)

    @property
    def filename(self):
        return self.path.name

    @classmethod
    def escape_as_filename(cls, name):
        value = re.sub(r"[^\w\s-]", "", name.lower())
        return re.sub(r"[-\s]+", "-", value).strip("-_")

    def write_text(self, text):
        self.path.parent.mkdir(exist_ok=True, parents=True)
        self.path.write_text(text)


class AsciiDocDocument(Document):
    def __init__(self, path):
        super().__init__(path)
        self._blocks = []

    @classmethod
    def adoc(cls, name):
        return str(pathlib.Path(cls.escape_as_filename(name)).with_suffix(".adoc"))

    def add_block(self, block: AsciiDocBlock):
        self._blocks.append(block)

    def render(self):
        text = "\n".join(str(b) for b in self._blocks)
        self.write_text(text)
