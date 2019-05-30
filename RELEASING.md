## Build and Release Process

### Prerequisites

  + Sign up for a [PyPI Account](https://pypi.org)
  + Sign up for a [PyPI Test Server Account](https://test.pypi.org)

### Setup

Create and activate a virtual environment from which to issue twine commands:

```sh
conda create -n twine-env python=3.7 # first time only
conda activate twine-env

pip install twine
```

### Building

Generate / build package distribution files:

```sh
python setup.py sdist bdist_wheel
```

Check the distribution:

```sh
twine check dist/*
```

If there is an error in the distribution, need to re-generate it and re-check it.

### Releasing

Otherwise, push to the PYPI Test Server:

```sh
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```

Finally, if everything looks good, release to PyPI:

```sh
twine upload --skip-existing dist/*
```
