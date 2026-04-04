from setuptools import find_packages, setup

setup(
    name="mini-http",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/groknut/fossdev/tree/homework/test_pypi_release",
)
