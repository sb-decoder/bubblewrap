from setuptools import setup, find_packages
from pathlib import Path

project_dir = Path(__file__).parent
long_description = (project_dir / "README.md").read_text()

setup(
    name="bubblewrap-cli",
    url="https://github.com/TechWiz-3/bubblewrap",
    author="Zac the Wise aka TechWiz-3",
    version='0.1.2',
    description="A Python library that makes beautiful text bubbles in your terminal using NerdFont icons.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_dir={'': 'src'},
    py_modules=["bubblewrap"],
    entry_points='''
        [console_scripts]
        bubblewrap=src.bubblewrap:cli
    ''',
    instal_requires=["rich"],
)
