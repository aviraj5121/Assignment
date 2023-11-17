# Django Project with CI Integration

This repository contains a Django project with Continuous Integration (CI) integration for automated testing. The CI workflow is configured using GitHub Actions, and test results are displayed on GitHub Pages.

## Project Overview

This Django project is designed to [briefly describe your project's purpose and features].

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python [version]
- Django [version]

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aviraj5121/Assignment.git
    ```

2. Change into the project directory:

    ```bash
    cd hello_world
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test

This project uses GitHub Actions for continuous integration. The workflow is defined in the .testing.yml file.

The CI workflow includes steps for:

Setting up Python environment
Installing dependencies
Running tests with coverage
Generating coverage report
Test results and coverage report will be visible on GitHub Pages.

GitHub Pages
The CI workflow generates a GitHub Pages site with the test results and coverage report. You can access it at:


