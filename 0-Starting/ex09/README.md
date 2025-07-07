# ft_package

A sample test package for counting occurrences of an element in a list.

## Installation

You can build and install the package locally using the following steps:

```bash
# Build the package (requires 'build' module)
python -m build

# Install the package (use one of the generated files)
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
# or
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package.my_module import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
