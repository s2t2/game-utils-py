# Credits, Notes, and Reference

  + https://github.com/s2t2/python-utils
  + https://stackoverflow.com/a/8256424/670433
  + https://stackoverflow.com/a/20043907/670433
  + https://github.com/github/gitignore/blob/master/Python.gitignore
  + https://fernandofreitasalves.com/pip-installing-package-from-private-repository/
  + https://github.com/s2t2/rock-paper-scissors-inclass/blob/master/game.py
  + http://data-creative.info/reference-docs/2019/05/30/how-to-publish-python-package-pypi/

## PYPI

  + https://pypi.org/manage/projects/
  + https://packaging.python.org/
  + https://packaging.python.org/tutorials/packaging-projects/
  + https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/

"Now that we have our built package, we can proceed to upload our code. PyPA recommends using Twine rather than setup.py commands, as setup.py may transmit your passwords in plaintext. So we will need to install Twine: Settings | Project | Project Interpreter, and add Twine."

  + https://realpython.com/pypi-publish-python-package/
  + https://pypi.org/search/
  + https://twine.readthedocs.io/en/latest/
  + https://packaging.python.org/guides/distributing-packages-using-setuptools/
  + https://stackoverflow.com/a/52130985/670433
  + https://packaging.python.org/guides/using-testpypi/#setting-up-testpypi-in-pypirc

## Setup Tools

  + https://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2/14753678
  + https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
  + https://github.com/pypa/twine
  + https://github.com/takluyver/flit
  + https://github.com/audreyr/cookiecutter

## Documenting

  + https://realpython.com/documenting-python-code/








<hr>

## Build and Release Process

```sh
conda create -n twine-env python=3.7
conda activate twine-env
pip install twine
```

Generating distribution files (building the package):

```sh
python setup.py sdist bdist_wheel
#> ...
#> adding 'game_utils/__init__.py'
#> adding 'game_utils/rock_paper_scissors.py'
#> adding 's2t2_game_utils-0.8.dist-info/LICENSE.md'
#> adding 's2t2_game_utils-0.8.dist-info/METADATA'
#> adding 's2t2_game_utils-0.8.dist-info/WHEEL'
#> adding 's2t2_game_utils-0.8.dist-info/top_level.txt'
#> adding 's2t2_game_utils-0.8.dist-info/RECORD'
```

Checking the distribution:

```sh
twine check dist/*
#> Checking distribution dist/s2t2_game_utils-0.8-py3-none-any.whl: Passed
#> Checking distribution dist/s2t2-game-utils-0.8.tar.gz: Passed
```

Push to GitHub.

If there is an error in the distribution, need to re-generate it and re-check it. Otherwise, try pushing to PYPI Test Server:

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#> Enter your username: s2t2
#> Enter your password:
#> Uploading distributions to https://test.pypi.org/legacy/
#> Uploading s2t2_game_utils-0.8-py3-none-any.whl
#> 100%|███████████████████████████████████████████████████████████████████| #> 6.55k/6.55k [00:00<00:00, 40.9kB/s]
#> Uploading s2t2-game-utils-0.8.tar.gz
#> 100%|███████████████████████████████████████████████████████████████████| #> 5.14k/5.14k [00:01<00:00, 4.71kB/s]
```

This creates / updates https://test.pypi.org/project/s2t2-game-utils/.
