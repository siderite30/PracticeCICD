# PracticeCICD

A small Python command-line calculator with unit tests and a GitHub Actions
workflow, ready for CI/CD practice.

## Run the app

```bash
python calculator.py add 2 3
```

Supported operations are `add`, `subtract`, `multiply`, and `divide`. Each
operation accepts two numbers.

## Run the tests

Python 3.12 or newer is recommended. No third-party packages are required.

```bash
python -m unittest discover -s tests -v
```

The `Python tests` GitHub Actions workflow runs this command on pushes and pull
requests.

TestTest
