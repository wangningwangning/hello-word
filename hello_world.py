"""
A simple Hello World module with various greeting functions.
"""


def hello_world():
    """Return a simple hello world greeting."""
    return "Hello, World!"


def hello_name(name):
    """Return a personalized greeting.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A personalized greeting
        
    Raises:
        TypeError: If name is not a string
        ValueError: If name is empty or only whitespace
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not name.strip():
        raise ValueError("Name cannot be empty or only whitespace")
    
    return f"Hello, {name.strip()}!"


def hello_multiple(names):
    """Return greetings for multiple names.
    
    Args:
        names (list): List of names to greet
        
    Returns:
        list: List of personalized greetings
        
    Raises:
        TypeError: If names is not a list
        ValueError: If names list is empty
    """
    if not isinstance(names, list):
        raise TypeError("Names must be a list")
    
    if not names:
        raise ValueError("Names list cannot be empty")
    
    return [hello_name(name) for name in names]


def get_greeting_count(names):
    """Get the count of greetings that would be generated.
    
    Args:
        names (list): List of names
        
    Returns:
        int: Number of greetings
    """
    if not isinstance(names, list):
        return 0
    
    return len([name for name in names if isinstance(name, str) and name.strip()])


def format_greeting(greeting, uppercase=False):
    """Format a greeting with optional uppercase.
    
    Args:
        greeting (str): The greeting to format
        uppercase (bool): Whether to convert to uppercase
        
    Returns:
        str: The formatted greeting
    """
    if not isinstance(greeting, str):
        return ""
    
    if uppercase:
        return greeting.upper()
    
    return greeting