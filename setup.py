import os

from setuptools import find_packages, setup


def read(fname):
    return open(
        os.path.join(os.path.dirname(__file__), fname), encoding="utf-8"
    ).read()


try:
    long_description = read("README.md")
except FileNotFoundError:
    long_description = (
        "A Python wrapper for the Internet Archive's Save Page Now API."
    )
    print("WARNING: README.md not found. Using a short description.")


setup(
    name="save-page-now-api",
    version="0.1.1",
    author="bac0id",
    author_email="ji2b13y6i@mozmail.com",
    description="A Python wrapper for the Internet Archive's Save Page Now API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bac0id/save-page-now-api",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    keywords="internet archive save page now api web archiving",
)
