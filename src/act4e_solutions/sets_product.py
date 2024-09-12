from typing import Any, Collection, Sequence, TypeVar
import itertools

import act4e_interfaces as I

C = TypeVar("C")
E = TypeVar("E")    # E = List[C]

# Interfaces are ALL in act4e_interfaces/set_product.py

# Implementations
from .sets_representation import MyFiniteSet
class MyFiniteMakeSetProduct(I.FiniteMakeSetProduct, MyFiniteSet):
    _components: Sequence[I.FiniteSet[C]]

    def __init__(self, elements: Collection[I.FiniteSet[C]]):
        self._components = list(elements)

    # SetProduct
    def components(self) -> Sequence[I.FiniteSet[C]]:
        return self._components
    def pack(self, args: Sequence[C]) -> E:
        return list(args)
    def unpack(self, args: E) -> Sequence[C]:
        return args


class SolFiniteMakeSetProduct(I.FiniteMakeSetProduct):
    def product(self, components: Sequence[I.FiniteSet[C]]) -> I.FiniteSetProduct[C, Any]:
        return MyFiniteMakeSetProduct(itertools.product(*components))