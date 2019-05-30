## Build and Release Process

### Prerequisites

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
twine upload dist/*
```

<hr>

## Verifying Ability to Install

Choose one of the following installation commands, as desired:

```sh
# from PyPI:
pip install s2t2-game-utils

# from PyPI Test server:
pip install -i https://test.pypi.org/simple/ s2t2-game-utils

# from GitHub source (HTTPS version):
pip install git+https://github.com/s2t2/game-utils-py.git

# from GitHub source (SSH version):
pip install git+ssh://git@github.com/s2t2/game-utils-py.git

# from local source (after downloading the repo):
pip install -e path/to/game-utils-py/
```

After installing, should be able to:

```py
from game_utils import *

print(INIT_MESSAGE) #> Initializing...
```

```py
from game_utils.rock_paper_scissors import *

print(WELCOME_MESSAGE) #> Hi. Welcome to my Rock-Paper-Scissors game!
```
