# Contributor's Guide

## Prerequisites

  + Git
  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork the repo from [GitHub source](https://github.com/s2t2/game-utils-py), then clone / download your fork onto your local machine.

Then navigate into the repository from the command-line:

```sh
cd game-utils-py/
```

## Setup

Create an activate an Anaconda virtual environment:

```sh
conda create -n game-utils-env python=3.7 # (first time only)
conda activate game-utils-env
```




## Developing

After installing, should be able to:

```py
from game_utils import *

print(INIT_MESSAGE) #> Initializing...
```

```py
from game_utils.rock_paper_scissors import *

print(WELCOME_MESSAGE) #> Hi. Welcome to my Rock-Paper-Scissors game!
```

## Testing

Install pytest (first time only):

```sh
pip install pytest
```

```sh
pytest
```
