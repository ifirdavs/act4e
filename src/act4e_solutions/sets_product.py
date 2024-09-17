from typing import Any, Collection, Sequence, List, TypeVar, Iterator, cast

import act4e_interfaces as I

C = TypeVar("C")    # A, B, C sets
E = TypeVar("E")    # Element of the Product: E = List[C]

# Interfaces are ALL in act4e_interfaces/set_product.py

# Implementations
class MyFiniteSetProduct(I.FiniteSetProduct):    # Also, can be written inheriting MyFiniteSet class (every method of MyFiniteSet fits the following imlpementation).
    _components: Sequence[I.FiniteSet[C]]
    _elements: List[E]

    def __init__(self, components: Collection[I.FiniteSet[C]]):
        self._components = list(components)

        result = [[]]
        for comp in self._components:
            temp_result = []

            for item in result:
                for elem in comp.elements():
                    temp_result.append(item + [elem])
            result = temp_result
        
        self._elements = result

    # FiniteSet
    def size(self) -> int:
        return len(self._elements)
    def elements(self) -> Iterator[E]:
        for _ in self._elements:
            yield _
    
    # Setoid
    def contains(self, x: E) -> bool:
        for y in self._elements:
            if self.equal(x, y):
                return True
        return False
    def save(self, h: I.IOHelper, x: E) -> I.ConcreteRepr:
        return cast(I.ConcreteRepr, x)
    def load(self, h: I.IOHelper, o: I.ConcreteRepr) -> E:
        return cast(E, o)
    
    # SetProduct
    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self._components
    def pack(self, args: Sequence[C]) -> E:
        return list(args)
    def unpack(self, args: E) -> Sequence[C]:
        return args


class SolFiniteMakeSetProduct(I.FiniteMakeSetProduct):
    def product(self, components: Sequence[I.FiniteSet[C]]) -> I.FiniteSetProduct[C, Any]:
        return MyFiniteSetProduct(components)