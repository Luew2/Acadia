# Acadia

Tool for creating stickers and selling on Redbubble.

## Setup
The steps below walk you through an initial setup and a clean Python environment.
We use [`Pipenv`](https://realpython.com/pipenv-guide/) to manage our project environment
and [`pre-commit`](https://pre-commit.com) to run CI actions both locally and in PR checks.

1. Install Python 3.10 - https://www.python.org/downloads/

2. Install Virtualenv - https://pypi.org/project/virtualenv/

3. Make sure your virtual environment is running - `which python`

4. Install pipenv within your running virtualenv
```bash
pip install pipenv
```

5. Install dependencies
```bash
pipenv sync
```

# Run
Run the main file in the desired sub-project directory.

Currently: run main.py in sticker_generator with option args -n (number of stickers), -size (256, 512, 1024) to generate stickers.

#Clean up
run cleanUp.py in the base directory to remove generated stickers in Sticker_Generator/data
