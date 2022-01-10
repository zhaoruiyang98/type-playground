from typing import (
    Protocol,
)


class Readable(Protocol):
    def read(self, __x): ...


class Test:
    def read(self, x):
        pass


class Test2:
    def read(self, t):
        pass


def foo(x: Readable):
    x.read(x=3)  # error


foo(Test())
foo(Test2())
