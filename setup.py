from setuptools import setup
from pathlib import Path


def read_long_description():
    with open(Path(__file__).parent / 'README.md', encoding='utf-8') as f:
        text = f.read()
    return text


install_requires = [
    'typing_extensions>=3.10',
    'numpy>=2.0'
]

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.9",
    "Typing :: Typed",
]

setup(
    name='type_playground',
    version='0.0.1',
    description='python type hint playground',
    url='https://github.com/zhaoruiyang98/type-playground',
    project_urls={
        'Source': 'https://github.com/zhaoruiyang98/type-playground',
        'Tracker': 'https://github.com/zhaoruiyang98/type-playground/issues',
        'Licensing': 'https://github.com/zhaoruiyang98/type-playground/blob/main/LICENSE'
    },
    author='Ruiyang Zhao',
    author_email='zhaoruiyang19@mails.ucas.edu.cn',
    license='MIT',
    python_requires='>=3.9, <3.10',
    keywords='python typing',
    classifiers=classifiers,
    zip_safe=False,
)
