# hello-word

A simple Python Hello World application with comprehensive unit tests.

## Features

- Basic "Hello, World!" greeting
- Personalized greetings for individual names
- Multiple greetings for lists of names
- Greeting count functionality
- Greeting formatting options (uppercase)
- Comprehensive error handling and validation

## Files

- `hello_world.py` - Main module with greeting functions
- `test_hello_world.py` - Comprehensive unit tests (100% coverage)
- `main.py` - Demo script showing functionality
- `requirements.txt` - Python dependencies
- `pytest.ini` - Test configuration

## Usage

### Running the demo:
```bash
python main.py
```

### Running tests:
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=hello_world --cov-report=term-missing
```

### Using the module:
```python
from hello_world import hello_world, hello_name, hello_multiple

print(hello_world())  # "Hello, World!"
print(hello_name("Alice"))  # "Hello, Alice!"
print(hello_multiple(["Alice", "Bob"]))  # ["Hello, Alice!", "Hello, Bob!"]
```

## Test Coverage

The project has 100% test coverage with 27 comprehensive unit tests covering:
- Normal functionality
- Edge cases
- Error conditions
- Input validation
- Integration scenarios
