import pathlib
from Irelia.__init__ import __version__
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="lolesports-lib",
    version=__version__,
    packages=["Irelia"],
    url="https://github.com/bgraver/Irelia",
    author="Brandon Graver",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    include_package_data=True
)
