import pathlib
from dataclasses import dataclass
import re

from .element import Element


@dataclass
class Document(Element):
    path: pathlib.Path | None = None

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
    @classmethod
    def adoc(cls, name):
        return str(pathlib.Path(cls.escape_as_filename(name)).with_suffix(".adoc"))

    def render(self):
        text = "\n".join(str(b) for b in self._children)
        self.write_text(text)
