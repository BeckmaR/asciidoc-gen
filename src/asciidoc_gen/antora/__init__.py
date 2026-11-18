from ..doc import AsciiDocDocument

import pathlib


class AntoraResource(AsciiDocDocument):
    family_dir = None
    family_coordinate = ""

    def __init__(self, module_path, relpath):
        if not self.family_dir:
            raise NotImplementedError("Only use subclassed types")

        self._module_path = module_path
        self._relpath = relpath
        super().__init__(pathlib.Path(module_path) / self.family_dir / relpath)

    @property
    def resource_coordinate(self):
        return f"{self.family_coordinate}{self._relpath}"


class Partial(AntoraResource):
    family_dir = "partials"
    family_coordinate = "partial$"


class Page(AntoraResource):
    family_dir = "pages"
