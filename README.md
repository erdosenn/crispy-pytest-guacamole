# crispy-pytest-guacamole
Frontend tests written in Python with Pytest and Playwright for [test ecommerce website](automationpractice.com/index.php).

# Intro
Tests were written using Python 3.8, Playwright, keeping the POM. I used the Pytest runner.

# Install enviroment
1. Install Python on your computer.
2. Open terminal. Install with `pip` command `pipenv` library:
```shell
pip install pipenv
```
3. Go to project location. Initialize virtual enviroment:
```shell
pipenv install
```
It will create virtual enviroment in your local files. In this process all libraries incluided in `Pipfile` file should be installed.
4. Enter to pipenv shell:
```shell
pipenv shell
```
5. Install Playwright in your env:
```shell
playwright install
```
It will download all necessary drivers for browsers.