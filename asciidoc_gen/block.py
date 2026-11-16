from .element import Element, ChildElement, RootElement, InlineElement, LineElement, BlockElement, SimpleTextElement
from dataclasses import dataclass, field



class Title(LineElement):
    def _render(self):
        return f".{super()._render()}"


@dataclass
class AsciiDocBlock(BlockElement):
    _title: Title | str = field(default="", init=False)

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
    level: int = 1
    custom_id: str = None

    def _render(self):
        text = ""
        if self.custom_id:
            text = f"[#{self.custom_id}]\n"

        text += f"{self.level*'='} {"".join(str(s) for s in self._children)}"
        return text


@dataclass
class Paragraph(AsciiDocBlock):
    pass


@dataclass
class IncludeMacro(LineElement):
    target: str = None
    leveloffset: str = None

    def _render(self):
        attributes = []
        if self.leveloffset:
            attributes.append(f"leveloffset={self.leveloffset}")
        return f"include::{self.target}[{",".join(attributes)}]"


@dataclass
class ListItem(BlockElement):
    level: int = 1


@dataclass
class UnorderedListItem(ListItem):
    
    def _render(self):
        return f"{self.level * "*"} {"\n".join(str(c) for c in self._children)}"


@dataclass
class List(AsciiDocBlock):
    def _render_block_content(self):
        return "\n".join(str(s).strip() for s in self._children_by_type(ListItem))
