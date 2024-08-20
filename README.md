# Trumio: Selenium Automation for SauceDemo Application

This README file provides a comprehensive overview of the Selenium-based automation project for testing the SauceDemo application. The project covers various test scenarios, including login functionality, product interactions, sorting, the checkout process, and navbar features.

## Project Overview

### Selenium Automation Workflow

To ensure code maintainability and clarity, the project is organized into a structured directory. Here’s an overview of the key components:

1. **Project Root:**
   - The project root directory contains the primary automation codebase.
  
2. **Directory Structure:**
   - **`Locators`**: Contains all web element locators used throughout the project.
   - **`Functions`**: Houses reusable functions for different automation tasks.
   - **`Tests`**: Contains the test cases that execute various scenarios within the SauceDemo application.
     - **`Logs`**: Stores log files for each test case in a timestamped format.
     - **`Report`**: Contains HTML reports that display the test case results in a browser-friendly format.
       - *Note*: If the `Logs` or `Report` folders do not exist, they are automatically created by the `conftest.py` script.
   - **`Utils`**: Includes utility functions and helper scripts to support the automation framework.
  
3. **Configuration Files:**
   - **`config.ini`**: Defines constants and values used across the project.
   - **`pytest.ini`**: Contains configuration for pytest, including markers for suite creation. 
     - *Note*: This file can be modified based on user requirements.

4. **Other Key Files:**
   - **`conftest.py`**: Initializes the automation workflow, including setting up and tearing down WebDriver instances.
   - **`requirements.txt`**: Lists the Python packages necessary to run the automation code. Ensure these dependencies are installed before running the tests.

### Log Files

Log files are generated for each test case, recording detailed execution logs. These logs are stored in the `Logs` folder and help in diagnosing test failures.

### HTML Reports

HTML reports provide a visual representation of the test results. These reports are generated using the `pytest-html` plugin. To generate an HTML report, execute the following command:
```bash
pytest --html=<report_name>.html --self-contained-html
```
This command will create an HTML report in the current working directory.

### Running Selected Test Suites

The `run_selected_suites.py` script enables running specific test suites or test cases, which is helpful when dealing with a large number of tests. The test suites to be executed are defined in the `suite_config.json` file.

### Commands to Run Tests

- **Run All Test Cases:**
  ```bash
  pytest
  ```
  This command runs all the test cases in the project.

- **Run a Specific Test Suite:**
  ```bash
  pytest -m <suite_name>
  ```
  This command runs a specific test suite by referencing the suite name (e.g., `sanity`, `regression`), which is marked in the `pytest.ini` file and test cases.

## Observations During Testing

The SauceDemo application was tested with various user profiles. Below are the key observations for each username:

### Username: `locked_out_user`

- **Login**: Unsuccessful
- **Glitch**: No
- **Pictures of Products**: Not available (due to failed login)
- **Alignment of Data**: Not applicable
- **Products Clickable**: No
- **Products Removable**: No
- **Sorting of Products**: Not applicable
- **Product Details on Main Page**: Not applicable
- **Navbar Functionality**: Not applicable
- **Checkout Process**: Not applicable

### Username: `problem_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: Not visible on the homepage but appear after clicking on a product.
- **Alignment of Data**: Correct
- **Products Clickable**: Only a few items are clickable.
- **Products Removable**: Only clickable items can be removed from the cart page.
- **Sorting of Products**: Sorting options are non-functional.
- **Product Details on Main Page**: Incorrect product is displayed (e.g., clicking on Sauce Labs Backpack shows Sauce Labs Fleece Jacket).
- **Navbar Functionality**: Working correctly
- **Checkout Button**: Issues with field behavior (e.g., the last name field overwrites the first name field).
- **Continue Button**: Not working due to field validation issues.
- **Finish Button**: Not applicable as the continue button fails.

### Username: `performance_glitch_user`

- **Login**: Successful
- **Glitch**: Yes, reloading is slow.
- **Pictures of Products**: All images are visible.
- **Alignment of Data**: Correct
- **Products Clickable**: All items are clickable.
- **Products Removable**: All items can be removed from the main page.
- **Sorting of Products**: All sorting options work as expected.
- **Product Details on Main Page**: Correct product is displayed.
- **Navbar Functionality**: Working correctly
- **Checkout Process**: All fields work correctly.
  
### Username: `error_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: All images are visible.
- **Alignment of Data**: Correct
- **Products Clickable**: Only a few items are clickable.
- **Products Removable**: Only clickable items can be removed from the cart page.
- **Sorting of Products**: Sorting options are non-functional.
- **Product Details on Main Page**: Correct product is displayed.
- **Navbar Functionality**: Working correctly
- **Checkout Button**: Last name field remains empty (a bug).
- **Continue Button**: Working despite the last name field being empty (another bug).
- **Finish Button**: Not clickable due to the last name field issue.

### Username: `visual_user`

- **Login**: Successful
- **Glitch**: No
- **Pictures of Products**: All images are visible except Sauce Labs Backpack on the homepage.
- **Alignment of Data**: Misaligned elements (e.g., Cart button, Hamburger Menu).
- **Products Clickable**: All items are clickable.
- **Products Removable**: All items can be removed from the main page.
- **Sorting of Products**: Sorting appears to be incorrect due to price value inconsistencies (sorted based on original prices).
- **Product Details on Main Page**: Correct product is displayed with original pricing.
- **Navbar Functionality**: Prices on the main page change with every click.
- **Checkout Process**: All fields work correctly.

---
