from dataclasses import dataclass

from .block import AsciiDocBlock
from .element import InlineElement, LineElement


class TableCell(InlineElement):
    def _render(self):
        return f"|{super()._render()}"


class TableRow(LineElement):
    def _render(self):
        return "".join(str(c) for c in self._children_by_type(TableCell))


@dataclass
class Table(AsciiDocBlock):
    _delimiter: str = "|==="

    def header(self):
        return self.option("header")

    def cols(self, value):
        if isinstance(value, list):
            value = ",".join(str(i) for i in value)
        if isinstance(value, str):
            value = f'"{value}"'
        return self.named_attr("cols", value)

    @property
    def block_content(self):
        return self._children_by_type(TableRow)
