"""Test suite for the subtraction operation using the AAA pattern."""
from calculator import subtract


def test_subtract():
    # Arrange
    first, second = 5, 2
    expected = 3
    
    # Act
    result = subtract(first, second)
    
    # Assert
    assert result == expected


def test_subtract_negative_numbers():
    # Arrange
    first, second = -5, -2
    expected = -3
    
    # Act
    result = subtract(first, second)
    
    # Assert
    assert result == expected


def test_subtract_to_zero():
    # Arrange
    first, second = 5, 5
    expected = 0
    
    # Act
    result = subtract(first, second)
    
    # Assert
    assert result == expected
