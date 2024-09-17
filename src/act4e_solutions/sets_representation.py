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

from .sets_product import MyFiniteSetProduct
class SolFiniteSetRepresentation(I.FiniteSetRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteSet_desc) -> I.FiniteSet[Any]:
        if not isinstance(data, dict):
            raise I.InvalidFormat()
        if "elements" in data:
            if not isinstance(data["elements"], list):
                raise I.InvalidFormat()
            elements = data["elements"]
            return MyFiniteSet(elements)
        elif "product" in data:
            if not isinstance(data["product"], list):
                raise I.InvalidFormat()
            components = [self.load(h, comp) for comp in data["product"]]
            return MyFiniteSetProduct(components)
        else:
            raise I.InvalidFormat()
        
    def save(self, h: I.IOHelper, f: I.FiniteSet[Any]) -> I.FiniteSet_desc:
        if isinstance(f, I.FiniteSetProduct):
            result = [self.save(h, comp) for comp in f.components()]
            return {"product": result}
        all_elements = [f.save(h, e) for e in f.elements()]
        return {"elements": all_elements}




# # Test
# obj = SolFiniteSetRepresentation()
# print(obj.load(None, {"elements": [1, 2, 3]}))