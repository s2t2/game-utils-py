
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="s2t2-game-utils",
    version="0.8",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="Gameplay logic for Rock-Paper-Scissors",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/game-utils",
    #packages=["game_utils"]
    packages=find_packages()
)
