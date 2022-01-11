from pathlib import Path
from datetime import datetime
from typing import Union
from typing_extensions import TypeAlias

YamlElement: TypeAlias = Union[str, bool, int, float, None, datetime]
SimpleYaml: TypeAlias = Union[
    YamlElement,
    list['SimpleYaml'],
    dict[str, 'SimpleYaml']
]


a: SimpleYaml = "a"
b: SimpleYaml = 1
c: SimpleYaml = True
d: SimpleYaml = None
e: SimpleYaml = datetime.now()

f: SimpleYaml = ["a", True, 1, None, datetime.now()]
g: SimpleYaml = {"a": "b", "b": 1, "c": True, "d": None, "e": datetime.now()}
h: SimpleYaml = {1: 2}  # assume keys have string type

i: SimpleYaml = {
    'mode': 'single',
    "dict": {
        "ddict": {
            'list': [0, 2],
            'path': 'path'
        }
    },
    "list": [
        [0, 2, 4],
        {
            'ddict': {'hello': 'world'},
            'list': ['a', None],
            'data': datetime.now()
        }
    ],
}


def update_path_in_yaml(d: SimpleYaml) -> None:
    """make '*path*' absolute
    """
    if isinstance(d, list):
        for item in d:
            update_path_in_yaml(item)
    if isinstance(d, dict):
        for key, value in d.items():
            if 'path' in key:
                assert isinstance(value, str)
                d[key] = str(Path(value).resolve())
