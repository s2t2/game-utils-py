
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="s2t2-game-utils",
    version="0.8",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="Gameplay logic for Rock-Paper-Scissors",
    long_description=long_description,
    license="MIT",
    url="https://github.com/s2t2/game-utils",
    #packages=["game_utils"]
    packages=setuptools.find_packages()
)
