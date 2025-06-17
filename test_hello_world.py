"""
Unit tests for the hello_world module.
"""

import pytest
from hello_world import (
    hello_world,
    hello_name,
    hello_multiple,
    get_greeting_count,
    format_greeting
)


class TestHelloWorld:
    """Test cases for the hello_world function."""
    
    def test_hello_world_returns_correct_string(self):
        """Test that hello_world returns the expected greeting."""
        result = hello_world()
        assert result == "Hello, World!"
    
    def test_hello_world_return_type(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)


class TestHelloName:
    """Test cases for the hello_name function."""
    
    def test_hello_name_with_simple_name(self):
        """Test hello_name with a simple name."""
        result = hello_name("Alice")
        assert result == "Hello, Alice!"
    
    def test_hello_name_with_name_containing_spaces(self):
        """Test hello_name with a name that has leading/trailing spaces."""
        result = hello_name("  Bob  ")
        assert result == "Hello, Bob!"
    
    def test_hello_name_with_complex_name(self):
        """Test hello_name with a complex name."""
        result = hello_name("Mary Jane")
        assert result == "Hello, Mary Jane!"
    
    def test_hello_name_with_non_string_raises_type_error(self):
        """Test that hello_name raises TypeError for non-string input."""
        with pytest.raises(TypeError, match="Name must be a string"):
            hello_name(123)
        
        with pytest.raises(TypeError, match="Name must be a string"):
            hello_name(None)
        
        with pytest.raises(TypeError, match="Name must be a string"):
            hello_name([])
    
    def test_hello_name_with_empty_string_raises_value_error(self):
        """Test that hello_name raises ValueError for empty string."""
        with pytest.raises(ValueError, match="Name cannot be empty or only whitespace"):
            hello_name("")
    
    def test_hello_name_with_whitespace_only_raises_value_error(self):
        """Test that hello_name raises ValueError for whitespace-only string."""
        with pytest.raises(ValueError, match="Name cannot be empty or only whitespace"):
            hello_name("   ")
        
        with pytest.raises(ValueError, match="Name cannot be empty or only whitespace"):
            hello_name("\t\n")


class TestHelloMultiple:
    """Test cases for the hello_multiple function."""
    
    def test_hello_multiple_with_single_name(self):
        """Test hello_multiple with a single name."""
        result = hello_multiple(["Alice"])
        assert result == ["Hello, Alice!"]
    
    def test_hello_multiple_with_multiple_names(self):
        """Test hello_multiple with multiple names."""
        result = hello_multiple(["Alice", "Bob", "Charlie"])
        expected = ["Hello, Alice!", "Hello, Bob!", "Hello, Charlie!"]
        assert result == expected
    
    def test_hello_multiple_with_names_having_spaces(self):
        """Test hello_multiple with names that have spaces."""
        result = hello_multiple(["  Alice  ", "Bob"])
        expected = ["Hello, Alice!", "Hello, Bob!"]
        assert result == expected
    
    def test_hello_multiple_with_non_list_raises_type_error(self):
        """Test that hello_multiple raises TypeError for non-list input."""
        with pytest.raises(TypeError, match="Names must be a list"):
            hello_multiple("Alice")
        
        with pytest.raises(TypeError, match="Names must be a list"):
            hello_multiple(123)
    
    def test_hello_multiple_with_empty_list_raises_value_error(self):
        """Test that hello_multiple raises ValueError for empty list."""
        with pytest.raises(ValueError, match="Names list cannot be empty"):
            hello_multiple([])
    
    def test_hello_multiple_propagates_hello_name_errors(self):
        """Test that hello_multiple propagates errors from hello_name."""
        with pytest.raises(TypeError, match="Name must be a string"):
            hello_multiple([123])
        
        with pytest.raises(ValueError, match="Name cannot be empty or only whitespace"):
            hello_multiple([""])


class TestGetGreetingCount:
    """Test cases for the get_greeting_count function."""
    
    def test_get_greeting_count_with_valid_names(self):
        """Test get_greeting_count with valid names."""
        result = get_greeting_count(["Alice", "Bob", "Charlie"])
        assert result == 3
    
    def test_get_greeting_count_with_empty_list(self):
        """Test get_greeting_count with empty list."""
        result = get_greeting_count([])
        assert result == 0
    
    def test_get_greeting_count_with_mixed_types(self):
        """Test get_greeting_count with mixed types in list."""
        result = get_greeting_count(["Alice", 123, "Bob", None])
        assert result == 2
    
    def test_get_greeting_count_with_empty_strings(self):
        """Test get_greeting_count with empty strings."""
        result = get_greeting_count(["Alice", "", "  ", "Bob"])
        assert result == 2
    
    def test_get_greeting_count_with_non_list(self):
        """Test get_greeting_count with non-list input."""
        result = get_greeting_count("not a list")
        assert result == 0
        
        result = get_greeting_count(123)
        assert result == 0
        
        result = get_greeting_count(None)
        assert result == 0


class TestFormatGreeting:
    """Test cases for the format_greeting function."""
    
    def test_format_greeting_normal_case(self):
        """Test format_greeting with normal case."""
        result = format_greeting("Hello, World!")
        assert result == "Hello, World!"
    
    def test_format_greeting_with_uppercase(self):
        """Test format_greeting with uppercase flag."""
        result = format_greeting("Hello, World!", uppercase=True)
        assert result == "HELLO, WORLD!"
    
    def test_format_greeting_with_uppercase_false(self):
        """Test format_greeting with uppercase explicitly set to False."""
        result = format_greeting("Hello, World!", uppercase=False)
        assert result == "Hello, World!"
    
    def test_format_greeting_with_empty_string(self):
        """Test format_greeting with empty string."""
        result = format_greeting("")
        assert result == ""
        
        result = format_greeting("", uppercase=True)
        assert result == ""
    
    def test_format_greeting_with_non_string(self):
        """Test format_greeting with non-string input."""
        result = format_greeting(123)
        assert result == ""
        
        result = format_greeting(None)
        assert result == ""
        
        result = format_greeting([])
        assert result == ""
    
    def test_format_greeting_preserves_whitespace(self):
        """Test that format_greeting preserves whitespace."""
        result = format_greeting("  Hello, World!  ")
        assert result == "  Hello, World!  "
        
        result = format_greeting("  Hello, World!  ", uppercase=True)
        assert result == "  HELLO, WORLD!  "


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_complete_workflow(self):
        """Test a complete workflow using multiple functions."""
        names = ["Alice", "Bob", "Charlie"]
        greetings = hello_multiple(names)
        count = get_greeting_count(names)
        formatted_greetings = [format_greeting(g, uppercase=True) for g in greetings]
        
        assert count == 3
        assert len(greetings) == 3
        assert len(formatted_greetings) == 3
        assert formatted_greetings[0] == "HELLO, ALICE!"
        assert formatted_greetings[1] == "HELLO, BOB!"
        assert formatted_greetings[2] == "HELLO, CHARLIE!"
    
    def test_workflow_with_mixed_input(self):
        """Test workflow with mixed valid and invalid input."""
        names = ["Alice", "", "Bob", "  Charlie  "]
        valid_count = get_greeting_count(names)
        
        # Filter out invalid names before processing
        valid_names = [name for name in names if isinstance(name, str) and name.strip()]
        greetings = hello_multiple(valid_names)
        
        assert valid_count == 3
        assert len(greetings) == 3
        assert "Hello, Alice!" in greetings
        assert "Hello, Bob!" in greetings
        assert "Hello, Charlie!" in greetings