from typing import Any, overload, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SetOfFiniteSubsets(Generic[C, E], Setoid[E], ABC):
    """A set of subsets."""
    


    @abstractmethod
    def contents(self, e: E) -> Iterator[C]:
        """Returns the contents of an element representing a subset."""
        pass

    @abstractmethod
    def construct(self, elements: Collection[C]) -> E:
        """Get the element representing the given subset."""
        pass

class FiniteSetOfFiniteSubsets(Generic[C, E], SetOfFiniteSubsets[C, E], FiniteSet[E], ABC):
    pass

class SolFiniteMakePowerSet(I.FiniteMakePowerSet):
    def powerset(self, s: I.FiniteSet[X]) -> I.FiniteSetOfFiniteSubsets[X, Any]:
        raise NotImplementedError() # implement here

