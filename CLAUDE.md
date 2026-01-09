# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python learning and practice repository organized into four main areas:

- **classes/** - Object-oriented programming examples and patterns
- **funcprogramming/** - Functional programming concepts and custom data structures
- **problem-solutions/** - Algorithm challenges and practical utilities
- **server-automation/** - System monitoring and automation scripts

## Running Code

This repository contains standalone Python scripts and modules. Execute them directly:

```bash
# Run individual scripts
python path/to/script.py

# Run modules with __main__.py
python -m classes
```

## Testing

The repository includes unit tests using Python's `unittest` framework:

```bash
# Run specific test file
python -m unittest funcprogramming.test_sorted_frozen_set

# Run with verbose output
python -m unittest funcprogramming.test_sorted_frozen_set -v

# Run all tests in a directory
python -m unittest discover -s funcprogramming -p "test_*.py"
```

## Key Architecture Patterns

### Custom Collection Implementation (funcprogramming/)

The `SortedFrozenSet` class (funcprogramming/sorted_frozen_set.py) demonstrates a complete implementation of Python's collection protocols:

- Inherits from `Sequence` and `Set` from collections.abc
- Implements immutable, sorted, deduplicated collections
- Full protocol support: Container, Sized, Iterable, Sequence, Hashable, Set
- Binary operations: union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`)
- Comprehensive test suite in test_sorted_frozen_set.py with 100+ test cases

### Object-Oriented Design (classes/)

The classes/ directory demonstrates inheritance hierarchies and abstract base classes:

- **Subscription System**: Abstract base class pattern with `abs_subscription.py` as the parent, concrete implementations in monthly/annual variants, and further specialization for corporate/student types
- **Aircraft System**: airtravel.py shows composition (Flight contains Aircraft), polymorphism (AirbusA319 and Boeing777 inherit from Aircraft), and encapsulation (private attributes with underscore prefix)
- **Main Entry Point**: __main__.py demonstrates module execution with subscription object instantiation

### Server Automation (server-automation/)

Scripts use `psutil` and `prettytable` libraries for system monitoring:

- serverhealth.py: Real-time dashboard showing OS info, network status, memory/disk usage, and top CPU processes
- Platform-specific modules for Windows (WMI) and cross-platform monitoring

## Dependencies

External libraries used in this codebase:

- `psutil` - System and process utilities (server-automation/)
- `prettytable` - Terminal table formatting (server-automation/)
- `wmi` - Windows Management Instrumentation (Windows-specific scripts)
- `requests` - HTTP library (problem-solutions/astros.py, funcprogramming/weatherapi.py)

Install dependencies as needed based on the script you're running.

## Code Conventions

- Private attributes/methods use single underscore prefix (e.g., `_items`, `_parse_seat()`)
- Docstrings follow Google style with Args/Raises sections
- Test classes group related test cases (e.g., TestConstruction, TestContainerProtocol)
- Validation happens in `__init__` methods with descriptive ValueError messages
