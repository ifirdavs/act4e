from typing import cast, Any, Collection, Iterator, List, TypeVar

import act4e_interfaces as I

E = TypeVar("E")
class MyFiniteSet(I.FiniteSet[E]):
    _elements: List[E]
    def __init__(self, elements: Collection[E]):
        self._elements = list(elements)
    def size(self) -> int:
        return len(self._elements)
    def contains(self, x: E) -> bool:
        for y in self._elements:
            if self.equal(x, y):
                return True
        return False
    def elements(self) -> Iterator[E]:
        return iter(self._elements)
        # for _ in self._elements:
        #     yield _

    def save(self, h: I.IOHelper, x: E) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)

    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> E:
        return cast(E, o)


class SolFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[Any]:
        if not isinstance(data, dict):
            raise I.InvalidFormat()
        # note: later on the format will be extended
        if not "elements" in data:
            raise I.InvalidFormat()
        if not isinstance(data["elements"], list):
            raise I.InvalidFormat()
        return MyFiniteSet(data["elements"])

    def save(self, h: I.IOHelper, f: I.FiniteSet[Any]) -> I.FiniteSet_desc:
        all_elements = [f.save(h, _) for _ in f.elements()]
        return {"elements": all_elements}
