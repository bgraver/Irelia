import pathlib
from Irelia.__init__ import __version__
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="lolesports-lib",
    version=__version__,
    url=""

)
