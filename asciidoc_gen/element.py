from dataclasses import dataclass, field, InitVar
from contextvars import ContextVar

_current_context = ContextVar("adg_context", default=None)


@dataclass
class RootElement:
    _children: list["Element"] = field(default_factory=list, init=False)

    def add(self, other: "Element"):
        self._children.append(other)
        other._parent = self

    def __enter__(self):
        self._context_token = _current_context.set(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _current_context.reset(self._context_token)

    @property
    def children(self):
        return list(self._children)
    
    def _children_by_type(self, cls):
        return filter(lambda c: isinstance(c, cls), self._children)

    def _last_child_by_type(self, cls):
        items = list(self._children_by_type(cls))
        if not items:
            return None
        return items[-1]

@dataclass
class ChildElement:
    parent: RootElement | None = field(default=None, kw_only=True)

    def __post_init__(self):
        self.parent = self.parent or _current_context.get()
        if self.parent is not None:
            self.parent.add(self)


@dataclass
class Text(ChildElement):
    text: str

    def __str__(self):
        return str(self.text)


@dataclass
class Element(RootElement, ChildElement):
    def _render(self):
        raise NotImplementedError("Must be overridden in child classes")

    def __str__(self):
        raise NotImplementedError("Must be overridden in child classes")


@dataclass
class SimpleTextElement(Element):
    text: InitVar[str | None] = None

    def __post_init__(self, text):
        super().__post_init__()
        if text:
            Text(text, parent=self)


@dataclass
class InlineElement(SimpleTextElement):
    def _render(self):
        return "".join(str(c) for c in self._children)

    def __str__(self):
        text = self._render()
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        text = text.strip()
        return text


@dataclass
class LineElement(SimpleTextElement):
    def _render(self):
        return "".join(str(c) for c in self._children)

    def __str__(self):
        text = self._render()
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        text = text.strip()
        return text + "\n"


class BlockElement(SimpleTextElement):
    def _render(self):
        raise NotImplementedError("Must be overridden in child classes")

    def __str__(self):
        text = self._render()
        if text is None:
            return ""
        if text and not text[-1] == "\n":
            text += "\n"
        return text
