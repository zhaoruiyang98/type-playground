from typing import (
    Any,
    Dict,
    cast,
    Optional,
    Type,
)


class ConstrainedNumberMeta(type):
    def __new__(cls, name: str, bases: Any, dct: Dict[str, Any]) -> "ConstraintInt": # type: ignore
        new_cls = cast('ConstrainedInt', type.__new__(cls, name, bases, dct))

        if new_cls.gt is not None and new_cls.ge is not None:
            raise Exception(
                'bounds gt and ge cannot be specified at the same time'
            )
        if new_cls.lt is not None and new_cls.le is not None:
            raise Exception(
                'bounds lt and le cannot be specified at the same time'
            )

        return new_cls


class ConstrainedInt(int, metaclass=ConstrainedNumberMeta):
    strict: bool = False
    gt: Optional[int] = None
    ge: Optional[int] = None
    lt: Optional[int] = None
    le: Optional[int] = None


def conint(
    *, strict: bool = False, gt: int = None, ge: int = None, lt: int = None, le: int = None
) -> Type[int]:
    namespace = dict(strict=strict, gt=gt, ge=ge, lt=lt, le=le)
    return type('ConstrainedIntValue', (ConstrainedInt,), namespace)


class Foo:
    x: conint(gt=3)  # type: ignore
