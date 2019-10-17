from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as readme_md:
    long_description = readme_md.read()

extras_require = {
    "develop": [
        "pre-commit",
        "black;python_version>='3.6'",  # Black is Python3 only
        "pytest",
        "twine",
    ]
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    name="ansatz",
    version="0.0.1",
    description="A physics Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthewfeickert/ansatz",
    author="Matthew Feickert",
    author_email="matthew.feickert@cern.ch",
    license="Apache",
    keywords=["physics"],
    packages=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require=extras_require,
)
