from setuptools import setup
import app

setup(
    name="Vocautils",
    description="Useful command line tool for VOCALOID.",
    version=app.__version__,
    license="MIT License",
    author="Fami",
    url="https://github.com/kotonefami/vocautils",
    entry_points={
        "console_scripts": [
            "voca = app:main"
        ]
    }
)
