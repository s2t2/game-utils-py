# Credits, Notes, and Reference

  + https://github.com/s2t2/python-utils
  + https://stackoverflow.com/a/8256424/670433
  + https://stackoverflow.com/a/20043907/670433
  + https://github.com/github/gitignore/blob/master/Python.gitignore
  + https://fernandofreitasalves.com/pip-installing-package-from-private-repository/

## PYPI

  + https://pypi.org/manage/projects/
  + https://packaging.python.org/
  + https://packaging.python.org/tutorials/packaging-projects/
  + https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/

"Now that we have our built package, we can proceed to upload our code. PyPA recommends using Twine rather than setup.py commands, as setup.py may transmit your passwords in plaintext. So we will need to install Twine: Settings | Project | Project Interpreter, and add Twine."

  + https://realpython.com/pypi-publish-python-package/
  + https://pypi.org/search/
  + https://twine.readthedocs.io/en/latest/





Generating distribution files (building the package):

```sh
python setup.py sdist bdist_wheel
```

Checking the distrubution:

```sh
twine check dist/*
```

Pushing distribution to PYPI:

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
