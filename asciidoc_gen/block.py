from .element import Element, ChildElement, RootElement, InlineElement, LineElement, BlockElement, SimpleTextElement
from dataclasses import dataclass, field



class Title(LineElement):
    def _render(self):
        return f".{super()._render()}"


@dataclass
class AsciiDocBlock(BlockElement):
    _title: Title | str = ""

    def add(self, element: Element):
        if isinstance(element, Title):
            self._title = element
        else:
            super().add(element)
    
    def _render_block_title(self):
        if not self._title:
            return ""
        return str(self._title)
    
    def _render_block_content(self):
        return "\n".join(str(s).strip() for s in self._children)

    def _render(self):
        return self._render_block_title() + self._render_block_content()


@dataclass
class Section(BlockElement):
    _level: int = 1
    _custom_id: str = None

    def level(self, level: int):
        self._level = level
        return self

    def custom_id(self, id):
        self._custom_id = id
        return self

    def _render(self):
        text = ""
        if self._custom_id:
            text = f"[#{self._custom_id}]\n"

        text += f"{self._level*'='} {"".join(str(s) for s in self._children)}"
        return text


@dataclass
class Paragraph(AsciiDocBlock):
    pass


@dataclass
class IncludeMacro(LineElement):
    _target: str = None
    _leveloffset: str = None

    def target(self, target):
        self._target = target
        return self

    def leveloffset(self, offset):
        self._leveloffset = offset
        return self

    def _render(self):
        attributes = []
        if self._leveloffset:
            attributes.append(f"leveloffset={self._leveloffset}")
        return f"include::{self._target}[{",".join(attributes)}]"


@dataclass
class UnorderedListItem(BlockElement):
    level: int = 1
    
    def _render(self):
        return f"{self.level * "*"} {"\n".join(str(c) for c in self._children)}"


@dataclass
class List(AsciiDocBlock):
    pass
