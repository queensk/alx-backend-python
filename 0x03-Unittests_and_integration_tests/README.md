# 0x03. Unittests and Integration Tests
This project is about writing and running unittests and integration tests in Python. Unittests are used to verify the functionality of individual components or units of code, while integration tests are used to check how different components work together.

## Learning Objectives
- What are unittests and why are they important
- How to write unittests using the unittest module
- How to run and interpret unittest results
- What are integration tests and why are they important
- How to write integration tests using requests-mock
- How to mock responses from an API

## Requirements
- Python 3.7 or higher
- requests and requests-mock modules installed

## Files
`utils.py`: Contains utility functions for manipulating strings and numbers
`client.py`: Contains a class that interacts with an external API
`test_utils.py`: Contains unittests for the functions in utils.py
`test_client.py`: Contains unittests and integration tests for the class in client.py

## Usage
To run the unittests, execute:
```
python -m unittest discover tests
```
To run a specific test file, execute:
```
python -m unittest tests/test_utils.py
```
To run a specific test case or test method, execute:
```
python -m unittest tests.test_utils.TestAccessNestedMap.test_access_nested_map_exception
```