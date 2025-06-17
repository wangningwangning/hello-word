#!/usr/bin/env python3
"""
Main script to demonstrate the hello_world module functionality.
"""

from hello_world import hello_world, hello_name, hello_multiple, format_greeting


def main():
    """Main function to demonstrate the greeting functions."""
    print("=== Hello World Demo ===")
    
    # Basic hello world
    print(f"1. Basic greeting: {hello_world()}")
    
    # Personalized greeting
    print(f"2. Personalized greeting: {hello_name('Python Developer')}")
    
    # Multiple greetings
    names = ["Alice", "Bob", "Charlie"]
    greetings = hello_multiple(names)
    print("3. Multiple greetings:")
    for greeting in greetings:
        print(f"   {greeting}")
    
    # Formatted greetings
    print("4. Uppercase greetings:")
    for greeting in greetings:
        print(f"   {format_greeting(greeting, uppercase=True)}")


if __name__ == "__main__":
    main()