
# Acadia
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Tool for creating stickers and selling on Redbubble.

## Setup
The steps below walk you through an initial setup and a clean Python environment.
I use [`Pipenv`](https://realpython.com/pipenv-guide/) to manage our project environment
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

6. Run virtual environment (after setting environment variables)
```bash
pipenv shell
```


# ENV VARIABLES

Make sure to create a .env file

The following environment variables must be set:
* ENV_OPENAI_KEY
* ENV_OPENAI_ORG
* ENV_CHROME_PROFILE

For more information on setting openai variables see: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key

For ENV_CHROME_PROFILE see *First Time Setup* Selenium step below.

# Run Generator
Run the main file in the desired sub-project directory.

Currently: run main.py in Sticker_Generator with option args -n (number of stickers), -size (256, 512, 1024) to generate stickers.

# Run Selenium
--- --- --- ---
 ### FIRST TIME SETUP
Open up your chrome and go to chrome://version/ and identify the default profile. Set this as your ENV_CHROME_PROFILE variable.

Go to RedBubble.com and login with the chrome browser you are planning to use with Selenium.
--- --- --- ---

### Running Selenium

Run the Selenium driver
```bash
python Selenium/driver.py
```

# Clean up
run clean_up.py in the base directory to remove generated stickers in Sticker_Generator/data
