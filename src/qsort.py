# https://github.com/python/typing/issues/59
from typing import (
    TypeVar,
    Any,
    Protocol,
)
from collections.abc import Iterable

_C = TypeVar("_C", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, __other: Any) -> bool: ...
    def __ne__(self, __other: Any) -> bool: ...
    def __lt__(self: _C, __other: _C) -> bool: ...
    def __le__(self: _C, __other: _C) -> bool: ...
    def __gt__(self: _C, __other: _C) -> bool: ...
    def __ge__(self: _C, __other: _C) -> bool: ...


def qsort(t: Iterable[_C]) -> list[_C]:
    return qsort_kernel(list(t))


def qsort_kernel(t: list[_C]) -> list[_C]:
    if not t:
        return []
    ref = t[0]
    left = qsort([x for x in t[1:] if x <= ref])
    right = qsort([x for x in t[1:] if x > ref])
    return left + [ref] + right


if __name__ == '__main__':
    ex1 = (1, 1, 4, 5, 1, 4)
    qsort(ex1)

    # both qsort and sorted can pass this
    ex2 = (1, '42')
    qsort(ex2)
    sorted(ex2)
