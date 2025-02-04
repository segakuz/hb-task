# Homebuddy test task
Testing quiz on the HVAC page

## Requirements installing:
```sh
pip install -r requirements.txt
```
Running tests
```sh
pytest -v --tb=line
```
Running tests with html report generation
```sh
pytest -v --capture=sys --tb=line --html=report.html
```
Running tests with mark
```sh
pytest -v --tb=line -m smoke
pytest -v --tb=line -m acceptance
```
