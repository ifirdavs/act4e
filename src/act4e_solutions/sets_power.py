from abc import ABC, abstractmethod
from typing import Any, TypeVar, Collection, Iterator, cast

import act4e_interfaces as I

C = TypeVar("C")
E = TypeVar("E")

# Interfaces are ALL in act4e_interfaces/set_power.py

# Implementations
class MyFiniteSetOfFiniteSubsets(I.FiniteSetOfFiniteSubsets):
    _elements: Collection[C]

    def __init__(self, elements: Collection[C]):
        self._elements = list(elements)

    # SetOfFiniteSubsets
    def contents(self, e: E) -> Iterator[C]:
        return iter(e)
    def construct(self, elements: Collection[C]) -> E:
        return elements

    # FiniteSet
    def size(self) -> int:
        return len(self._elements)
    def elements(self) -> Iterator[E]:
        return iter(self._elements)
    
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


class SolFiniteMakePowerSet(I.FiniteMakePowerSet):
    def powerset(self, s: I.FiniteSet[C]) -> I.FiniteSetOfFiniteSubsets[C, Any]:
        elems = list(s.elements())

        def powset(elems):
            if len(elems) <= 1:
                yield elems
                yield []
            else:
                for item in powset(elems[1:]):
                    yield [elems[0]] + item
                    yield item
        
        return MyFiniteSetOfFiniteSubsets([e for e in powset(elems)])




# Test
# obj = SolFiniteMakePowerSet()
# print(obj.powerset(MyFiniteSetOfFiniteSubsets([1, 2, 3])))

# for i in obj.powerset(MyFiniteSetOfFiniteSubsets([1, 2, 3])).elements():
#     print(i, end=" ")
