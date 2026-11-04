from dataclasses import dataclass, field
from contextvars import ContextVar

_current_context = ContextVar("adg_context", default=None)


@dataclass
class Element:
    parent: "Element | None" = None
    _children: list["Element"] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.parent = self.parent or _current_context.get()
        if self.parent is not None:
            self.parent.add(self)

    def add(self, other: "Element"):
        self._children.append(other)

    @property
    def children(self):
        return list(self._children)

    def render(self):
        raise NotImplementedError("Must be overridden in child classes")

    def __str__(self):
        raise NotImplementedError("Must be overridden in child classes")

    def __enter__(self):
        self._context_token = _current_context.set(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _current_context.reset(self._context_token)
