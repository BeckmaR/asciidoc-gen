from .element import Element, ChildElement, RootElement, InlineElement, LineElement, BlockElement, SimpleTextElement
from .attr import AttrList, Attribute, NamedAttribute
from dataclasses import dataclass, field



class Title(LineElement):
    def _render(self):
        return f".{super()._render()}"


@dataclass
class AsciiDocBlock(BlockElement):
    def add(self, element: Element):
        if isinstance(element, Attribute):
            if not self.attrlist:
                self.add(AttrList(parent=self))
            self.attrlist.add(element)
            
        else:
            super().add(element)
    
    @property
    def title(self):
        return self._last_child_by_type(Title)
    
    @property
    def attrlist(self):
        return self._last_child_by_type(AttrList)
    
    @property
    def block_content(self):
        exclude_types = [AttrList, Title]
        return (c for c in self._children if not any(isinstance(c, et) for et in exclude_types))
    
    def _render_block_title(self):
        if not self.title:
            return ""
        return str(self.title)
    
    def _render_attr_list(self):
        if not self.attrlist:
            return ""
        return str(self.attrlist) + "\n"
    
    def _render_block_content(self):
        return "\n".join(str(s).strip() for s in self.block_content)

    def _render(self):
        return self._render_block_title() + self._render_attr_list() + self._render_block_content()


@dataclass
class Section(AsciiDocBlock):
    level: int = 1

    def _render_block_content(self):
        return f"{self.level*'='} {"".join(str(s) for s in self.block_content)}"


@dataclass
class Paragraph(AsciiDocBlock):
    pass


@dataclass
class IncludeMacro(LineElement):
    target: str = None
    leveloffset: str = None
    attrs: AttrList = field(default=None, init=False)
    
    def __post_init__(self, text):
        super().__post_init__(text)
        self.attrs = AttrList(parent=self)

    def _render(self):
        if self.leveloffset:
            NamedAttribute(parent=self.attrs, name="leveloffset", value=self.leveloffset)
        return f"include::{self.target}{str(self.attrs)}"


@dataclass
class ListItem(BlockElement):
    level: int = 1


@dataclass
class UnorderedListItem(ListItem):
    
    def _render(self):
        return f"{self.level * "*"} {"\n".join(str(c) for c in self._children)}"


@dataclass
class List(AsciiDocBlock):
    @property
    def block_content(self):
        return self._children_by_type(ListItem)
