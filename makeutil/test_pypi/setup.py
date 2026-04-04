from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mini-http",
    version="0.0.4",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/groknut/fossdev/tree/homework/test_pypi_release/makeutil/test_pypi",
    description="Минимальный HTTP-сервер на порту 8080",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="groknut",
)
