from dataclasses import dataclass

from .element import ChildElement, InlineElement

@dataclass
class Attribute(ChildElement):
    value: str
        
    def _render(self):
        return self.value

    def __str__(self):
        return self._render().strip()


@dataclass
class PositionalAttribute(Attribute):
    pass


@dataclass
class ShortHandAttribute(Attribute):
    pass


@dataclass
class BlockStyleAttribute(ShortHandAttribute):
    pass


@dataclass
class RoleAttribute(ShortHandAttribute):
    def _render(self):
        return f".{super()._render()}"


@dataclass
class IDAttribute(ShortHandAttribute):
    def _render(self):
        return f"#{super()._render()}"


@dataclass
class OptionAttribute(ShortHandAttribute):
    def _render(self):
        return f"%{super()._render()}"


@dataclass
class NamedAttribute(Attribute):
    name: str

    def _render(self):
        return f"{self.name}={super()._render()}"


@dataclass
class AttrList(InlineElement):
    def _render(self):
        attrs = []
        
        shorthand_attribute = ""
        for cls in [BlockStyleAttribute, IDAttribute, RoleAttribute, OptionAttribute]:
            for item in self._children_by_type(cls):
                shorthand_attribute += str(item)
        if shorthand_attribute:
            attrs.append(shorthand_attribute)
        
        attrs.extend(self._children_by_type(PositionalAttribute))
        attrs.extend(self._children_by_type(NamedAttribute))
        
        return f"[{",".join(str(a) for a in attrs)}]"
