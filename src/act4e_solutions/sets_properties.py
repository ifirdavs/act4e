from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")

# Ex B.2
class SolFiniteSetProperties(I.FiniteSetProperties):
    def is_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        """True if `a` is a subset of `b`."""

        for x in a.elements():
            if not b.contains(x):
                return False
        return True
        
    def equal(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        return self.is_subset(a, b) and self.is_subset(b, a)

    def is_strict_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        return self.is_subset(a, b) and not self.is_subset(b, a)


class SolFiniteMakeSetUnion(I.FiniteMakeSetUnion):
    def union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetUnion[X, Any]:
        raise NotImplementedError() # implement here


class SolFiniteMakeSetIntersection(I.FiniteMakeSetIntersection):
    def intersection(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSet[X]:
        raise NotImplementedError()
