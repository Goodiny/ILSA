from .feature import Feature
from .ins import In
from typing import List

class Specification(Feature):
    def __init__(self, name: str, value: str, base: bool, ins: List[In]):
        super().__init__(name)
        super().value = value
        super().base = base
        super().ins = ins