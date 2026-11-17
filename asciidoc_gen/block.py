from .element import Element, ChildElement, RootElement, InlineElement, LineElement, BlockElement, SimpleTextElement
from .attr import AttrList, BlockStyleAttribute, ElementAttribute, IDAttribute, NamedAttribute, OptionAttribute, PositionalAttribute, RoleAttribute
from dataclasses import dataclass, field



class Title(LineElement):
    def _render(self):
        return f".{super()._render()}"


@dataclass
class AsciiDocBlock(BlockElement):
    _delimiter: str = ""

    def add(self, element: Element):
        if isinstance(element, ElementAttribute):
            if not self.attrlist:
                self.add(AttrList(parent=self))
            self.attrlist.add(element)
            
        else:
            super().add(element)
    
    def option(self, value):
        OptionAttribute(value, parent=self)
        return self
    
    def id(self, value):
        IDAttribute(value, parent=self)
        return self
    
    def style(self, value):
        BlockStyleAttribute(value, parent=self)
        return self
    
    def role(self, value):
        RoleAttribute(value, parent=self)
        return self
    
    def pos_attr(self, value):
        PositionalAttribute(value, parent=self)
        return self

    def named_attr(self, name, value):
        NamedAttribute(value, name, parent=self)
        return self
    
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
        return self._ensure_oneline(self.title)
    
    def _render_attr_list(self):
        return self._ensure_oneline(self.attrlist)
    
    def _render_block_content(self):
        return "\n".join(str(s).strip() for s in self.block_content)

    def _render(self):
        return ( 
                self._render_block_title() +
                self._render_attr_list() +
                self._ensure_oneline(self._delimiter) +
                self._ensure_endline(self._render_block_content()) +
                self._ensure_oneline(self._delimiter)
        )


@dataclass
class Section(AsciiDocBlock):
    level: int = 1

    def _render_block_content(self):
        return f"{self.level*'='} {"".join(str(s) for s in self.block_content)}"


@dataclass
class Paragraph(AsciiDocBlock):
    pass


@dataclass
class ExampleBlock(AsciiDocBlock):
    _delimiter: str = "===="


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
