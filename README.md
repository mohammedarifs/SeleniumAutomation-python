# SeleniumAutomation-python

Welcome! This repository contains a Python test automation framework for testing the [Sauce Demo](https://www.saucedemo.com/) website. It uses **Selenium WebDriver** to control Chrome and **pytest** to organize and run browser tests. The included scenarios cover login, adding a product to the cart, and beginning checkout.

This README is saved at the **root of the repository**. GitHub automatically displays a root `README.md` on the repository's main page when someone opens the repo.

## Selenium introduction

Selenium is a browser automation tool. A test uses a WebDriver to open a browser, find page elements, and perform actions such as entering text or clicking buttons. In this project, Selenium drives Chrome while pytest runs the tests and reports their results.

The project uses the **Page Object Model (POM)**: page-specific Python classes keep browser actions separate from test scenarios. Element locators are stored in a configuration file, and login inputs for the parameterized test are stored in a CSV file.

## Important directories and files

```text
.
├── README.md                         # Project introduction and usage guide
├── conftest.py                       # Shared pytest fixtures; starts and closes Chrome
├── pytest.ini                        # pytest settings and marker declarations
├── requirements.txt                  # Python package dependencies
├── DemoProject/
│   ├── config.properties             # Project, environment, and browser settings
│   ├── pages/                        # Page Object Model classes
│   │   ├── loginPage.py              # Login and logout actions
│   │   ├── dashboardPage.py          # Inventory and cart actions
│   │   └── cartPage.py               # Checkout page actions
│   ├── tests/
│   │   └── Add_toCart_test.py        # Login, add-to-cart, and checkout tests
│   ├── testdata/
│   │   ├── conf.ini                  # Page element locators grouped by page
│   │   └── testdata.csv              # CSV inputs for the data-driven login test
│   └── reports/
│       ├── report.html               # Included HTML test report
│       └── assets/style.css          # Stylesheet for the included report
└── utils/
    └── configReader.py               # Reads conf.ini settings and CSV test data
```

### How the pieces work together

1. `conftest.py` provides the `Configure` fixture. It starts Chrome in incognito mode, opens Sauce Demo, and closes the browser after each test.
2. `DemoProject/tests/Add_toCart_test.py` defines pytest test cases and calls the page objects.
3. Classes in `DemoProject/pages/` perform page-specific browser actions using Selenium.
4. `utils/configReader.py` reads locators from `DemoProject/testdata/conf.ini` and login rows from `DemoProject/testdata/testdata.csv`.

`DemoProject/config.properties` contains project metadata; the current page objects read their locators from `DemoProject/testdata/conf.ini`.

## Installation

### Prerequisites

- Python 3.10 or later
- Google Chrome
- Internet access to reach Sauce Demo and install Python packages

Selenium 4 uses Selenium Manager to locate or manage a compatible ChromeDriver in supported environments. If automatic driver setup is unavailable in your environment, install a ChromeDriver version compatible with your Chrome browser and ensure it is on your `PATH`.

### Windows (PowerShell)

Run these commands from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell does not allow virtual-environment activation, use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS or Linux

Run these commands from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the tests

From the repository root, run:

```bash
python -m pytest DemoProject/tests
```

The tests launch a real Chrome browser and access `https://www.saucedemo.com/`. The login test reads its input rows from `DemoProject/testdata/testdata.csv`.

## Included HTML report

The framework includes an HTML test report at:

**`DemoProject/reports/report.html`**

The report's stylesheet is at **`DemoProject/reports/assets/style.css`**. Open `report.html` in a browser to view the saved report. The report is a checked-in artifact and may represent an earlier test run; regenerate it after running tests if you need up-to-date results.

To create or replace the report, install the optional `pytest-html` plugin and run pytest with the report options:

```bash
python -m pip install pytest-html
python -m pytest DemoProject/tests --html=DemoProject/reports/report.html --self-contained-html
```

`pytest-html` is not currently included in `requirements.txt`. The `reports` directory is ignored by `.gitignore` for untracked files, but the existing report and stylesheet are already tracked in this repository.
