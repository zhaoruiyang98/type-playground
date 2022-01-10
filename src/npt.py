import numpy as np
from numpy.typing import ArrayLike, NBitBase
from typing import TypeVar, TYPE_CHECKING, Union


def foo(x: ArrayLike):
    return np.array(x)


T1 = TypeVar('T1', bound=NBitBase)
T2 = TypeVar('T2', bound=NBitBase)


def bar(a: np.floating[T1], b: np.integer[T2]) -> np.floating[Union[T1, T2]]:
    return a + b


if __name__ == '__main__':
    a = (1, 2, 3)
    foo(a)
    foo(x**2 for x in range(10))  # error

    a = np.float16()
    b = np.int64()
    out = bar(a, b)
    if TYPE_CHECKING:
        reveal_type(out)  # it seems that NBitBase not yet supported in pylance
