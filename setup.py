from os import path

from setuptools import setup

REQUIREMENTS_FILE = "requirements.txt"
REQUIREMENTS_PATH = path.join(path.abspath(__file__), REQUIREMENTS_FILE)

with open(REQUIREMENTS_FILE) as f:
    requirements = f.read().splitlines()

setup(
    name="dsdl",
    version="0.1.1",
    description="Dataset Downloader",
    long_description_content_type="text/markdown",
    url="https://github.com/fkunstner/dataset-downloader",
    author="fkunstner",
    author_email="frederik.kunstner@gmail.com",
    packages=["dsdl"],
    install_requires=requirements,
)
